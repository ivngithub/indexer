import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")


if __name__ == '__main__':
    django.setup()

    from indexer.models import Network, Contract

    abi = [
        {
            "name": "PunkTransfer",
            "type": "event",
            "inputs": [
                {"name": "from", "type": "address", "indexed": True},
                {"name": "to", "type": "address", "indexed": True},
                {"name": "punkIndex", "type": "uint256", "indexed": False}
            ],
            "anonymous": False
        }
    ]
    start_block = sys.argv[1]
    end_block = sys.argv[2]

    network = Network.objects.get(network_id=Network.NetworkId.MAINNET)
    contract = Contract(
        contract_type=Contract.ContractType.TOKEN,
        name='CryptoPunks',
        address='0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB',
        abi=abi,
        start_block=sys.argv[1],
        end_block=sys.argv[2],
        network=network,
    )
    contract.save()
    print(contract.id)
