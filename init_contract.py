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
                {"indexed": False, "name": "buyHash", "type": "bytes32"},
                {"indexed": False, "name": "sellHash", "type": "bytes32"},
                {"indexed": True, "name": "maker", "type": "address"},
                {"indexed": True, "name": "taker", "type": "address"},
                {"indexed": False, "name": "price", "type": "uint256"},
                {"indexed": True, "name": "metadata", "type": "bytes32"}
            ],
            "name": "OrdersMatched",
            "type": "event"
        }
    ]
    start_block = sys.argv[1]
    end_block = sys.argv[2]

    contract = Contract(
        name='OpenSea',
        address='0xF715bEb51EC8F63317d66f491E37e7BB048fCc2d',
        abi=abi,
        start_block=sys.argv[1],
        end_block=sys.argv[2],
    )
    contract.save()
    print(contract.id)
