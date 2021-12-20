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
        name='Mutant Ape Yacht Club',
        address='0x60E4d786628Fea6478F785A6d7e704777c86a7c6',
        abi=abi,
        start_block=sys.argv[1],
        end_block=sys.argv[2],
        network=network,
    )
    contract.save()
    print(contract.id)
