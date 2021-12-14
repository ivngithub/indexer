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
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()
from django.core.exceptions import ObjectDoesNotExist   # noqa E402


from indexer.models import Indexer

if __name__ == '__main__':

    print('name', sys.argv[3])

    indexer = Indexer(
        start_block=sys.argv[1],
        end_block=sys.argv[2],
        indexer_id=sys.argv[3],
        current_block=sys.argv[1]
    )
    indexer.save()
