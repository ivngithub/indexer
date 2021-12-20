import logging
import os
import sys

import django
from web3 import Web3

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)8s %(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')


def adjust_step(target_events_per_request, step, events):
    if step > 300000:
        adjusted_step = step // 4
    elif events > 1:
        adjusted_step = min(int(step * target_events_per_request / events), int(step * 1.1))
    else:
        adjusted_step = int(step * 1.1)
    logging.info(f'Adjusted step: {adjusted_step}')
    return adjusted_step


def error_parsing(e):
    for arg in e.args:
        if type(arg) is dict:
            if arg.get('code') == -32005 and arg.get('message') == 'query returned more than 10000 results':
                return arg.get('message')


if __name__ == '__main__':
    django.setup()
    from django.core.exceptions import ObjectDoesNotExist
    from indexer.models import Contract, Indexer, RangeBlock, Trade, Mapping

    logging.info(f'start indexer-{sys.argv[3]} from {sys.argv[1]} to {sys.argv[2]}')
    try:
        indexer = Indexer.objects.get(indexer_id=sys.argv[3], contract_id=sys.argv[4])
    except ObjectDoesNotExist:
        contract = Contract.objects.get(id=sys.argv[4])
        indexer = Indexer(
            start_block=int(sys.argv[1]),
            end_block=int(sys.argv[2]),
            indexer_id=int(sys.argv[3]),
            last_block=int(sys.argv[1])-1,
            step=25000,
            target_events_per_request=8500
        )
        indexer.contract = contract
        indexer.save()

    w3 = Web3(Web3.HTTPProvider(
        'https://mainnet.infura.io/v3/79ce5829e4e14a7bbcce780dbc28dd14',
        request_kwargs={'timeout': 120}
    ))

    token_contract = w3.eth.contract(abi=indexer.contract.abi, address=indexer.contract.address)

    while indexer.end_block != indexer.last_block:

        logging.info(f'last block: {indexer.last_block}')
        logging.info(f'Get events')

        to_block = indexer.last_block + indexer.step \
            if indexer.last_block + indexer.step <= indexer.end_block else indexer.end_block

        from_block = indexer.last_block + 1
        logging.info(f'from_block: {from_block}')
        logging.info(f'end_block: {to_block}')
        try:
            filter_ = token_contract.events.PunkTransfer.createFilter(
                fromBlock=from_block, toBlock=to_block
            )
            events = filter_.get_all_entries()
        except ValueError as e:
            if error_parsing(e) == 'query returned more than 10000 results':
                logging.warning(f'step {indexer.step} must be reduced')
                indexer.step = int(indexer.step // 1.5) or 1
                indexer.save()
                logging.warning(f'next step will be {indexer.step}')
            raise e

        mappers = list()
        range_block = RangeBlock(
            first_block=from_block,
            last_block=to_block,
            step=to_block-from_block,
            count_events=len(events),
            indexer=indexer,
            contract=indexer.contract
        )
        logging.info(f'Got {len(events)} events.')
        logging.info('events processing: start')
        for event in events:
            tx = event.transactionHash.hex()
            try:
                trade = Trade.objects.get(tx=tx)
                mapping = Mapping(
                    exchange=trade.range_block.contract,
                    token=indexer.contract,
                    trade=trade
                )
                mappers.append(mapping)
                logging.info(f'find token {indexer.contract.name} for mapping with trade Tx: {tx} ')
            except ObjectDoesNotExist:
                pass
        logging.info('events processing: end')
        logging.info('save data: start')
        range_block.save()
        if mappers:
            logging.info('save all mappers: start')
            Mapping.objects.bulk_create(mappers,  ignore_conflicts=True)
            logging.info('save all mappers: end')
        indexer.step = adjust_step(indexer.target_events_per_request, indexer.step, len(events))
        indexer.last_block = to_block
        indexer.save()
        range_block.save()
        logging.info('save data: end')

    logging.info('done.')
