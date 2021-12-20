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
                {"indexed": True, "name": "makerAddress", "type": "address"},
                {"indexed": True, "name": "feeRecipientAddress", "type": "address"},
                {"indexed": False, "name": "makerAssetData", "type": "bytes"},
                {"indexed": False, "name": "takerAssetData", "type": "bytes"},
                {"indexed": False, "name": "makerFeeAssetData", "type": "bytes"},
                {"indexed": False, "name": "takerFeeAssetData", "type": "bytes"},
                {"indexed": True, "name": "orderHash", "type": "bytes32"},
                {"indexed": False, "name": "takerAddress", "type": "address"},
                {"indexed": False, "name": "senderAddress", "type": "address"},
                {"indexed": False, "name": "makerAssetFilledAmount", "type": "uint256"},
                {"indexed": False, "name": "takerAssetFilledAmount", "type": "uint256"},
                {"indexed": False, "name": "makerFeePaid", "type": "uint256"},
                {"indexed": False, "name": "takerFeePaid", "type": "uint256"},
                {"indexed": False, "name": "protocolFeePaid", "type": "uint256"},
            ],
            "name": "Fill", "type": "event"
        }
    ]
    start_block = sys.argv[1]
    end_block = sys.argv[2]

    contract = Contract(
        name='OpenSea Polygon',
        address='0xfede379e48C873C75F3cc0C81F7C784aD730a8F7',
        abi=abi,
        start_block=sys.argv[1],
        end_block=sys.argv[2],
    )
    contract.save()
    print(contract.id)
