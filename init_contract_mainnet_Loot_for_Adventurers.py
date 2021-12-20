import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")


if __name__ == '__main__':
    django.setup()

    from indexer.models import Network, Contract

    abi = [
        {
            "name": "Transfer",
            "type": "event",
            "inputs": [
                {"name": "from", "type": "address", "indexed": True, "internalType": "address"},
                {"name": "to", "type": "address", "indexed": True, "internalType": "address"},
                {"name": "tokenId", "type": "uint256", "indexed": True, "internalType": "uint256"}
            ],
            "anonymous": False
        }
    ]
    start_block = sys.argv[1]
    end_block = sys.argv[2]

    network = Network.objects.get(network_id=Network.NetworkId.MAINNET)
    contract = Contract(
        contract_type=Contract.ContractType.TOKEN,
        name='Loot (for Adventurers)',
        address='0xFF9C1b15B16263C61d017ee9F65C50e4AE0113D7',
        abi=abi,
        start_block=sys.argv[1],
        end_block=sys.argv[2],
        network=network,
    )
    contract.save()
    print(contract.id)
