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
        name='Bored Ape Kennel Club',
        address='0xba30E5F9Bb24caa003E9f2f0497Ad287FDF95623',
        abi=abi,
        start_block=sys.argv[1],
        end_block=sys.argv[2],
        network=network,
    )
    contract.save()
    print(contract.id)
