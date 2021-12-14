#!/bin/bash
python indexer_worker.py $((INDEXER_START_BLOCK)) $((INDEXER_END_BLOCK))
