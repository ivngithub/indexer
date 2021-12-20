import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")


if __name__ == '__main__':
    django.setup()

    from indexer.models import Contract

    abi = [
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "name": "punkIndex", "type": "uint256"},
                {"indexed": False, "name": "value", "type": "uint256"},
                {"indexed": True, "name": "fromAddress", "type": "address"},
                {"indexed": True, "name": "toAddress", "type": "address"}
            ],
            "name": "PunkBought", "type": "event"
        }
    ]
    start_block = sys.argv[1]
    end_block = sys.argv[2]

    contract = Contract(
        name='CryptoPunksMarket',
        address='0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB',
        abi=abi,
        start_block=sys.argv[1],
        end_block=sys.argv[2],
    )
    contract.save()
    print(contract.id)
