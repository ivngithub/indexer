import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")


if __name__ == '__main__':
    django.setup()

    from indexer.models import Network, Contract

    abi = [
        {
            "name": "OrdersMatched", "type": "event",
            "inputs": [
                {"name": "buyHash", "type": "bytes32", "indexed": False},
                {"name": "sellHash", "type": "bytes32", "indexed": False},
                {"name": "maker", "type": "address", "indexed": True},
                {"name": "taker", "type": "address", "indexed": True},
                {"name": "price", "type": "uint256", "indexed": False},
                {"name": "metadata", "type": "bytes32", "indexed": True}
            ],
            "anonymous": False
        }
    ]
    start_block = sys.argv[1]
    end_block = sys.argv[2]

    network = Network.objects.get(network_id=Network.NetworkId.MAINNET)
    contract = Contract(
        contract_type=Contract.ContractType.TOKEN,
        name='GM PUNKS',
        address='0x495f947276749Ce646f68AC8c248420045cb7b5e',
        abi=abi,
        start_block=sys.argv[1],
        end_block=sys.argv[2],
        network=network,
    )
    contract.save()
    print(contract.id)
