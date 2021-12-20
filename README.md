## indexer

This project is an attempt to make a fast indexer. The basic idea is to create more small indexers that are responsible for a small number of blocks. Each indexer is a python script placed in a docker container that interacts with a common database.

When creating a large number of containers, more RAM is required. 

use
`/swapfile  file  30G`

env
```
export POSTGRES_PASSWORD=<password>
export POSTGRES_USER=indexer
export POSTGRES_HOST=127.0.0.1
export POSTGRES_DB=indexer
```

run db
```
docker run -d -p 5432:5432 --name db -e POSTGRES_PASSWORD -e POSTGRES_USER -e POSTGRES_DB postgres -N 3000
```

install moduls 
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

run indexer

You need to specify the initialization script in runner.sh. Variable contact_id=
You need to specify the indexer script in start.sh.
`runner.sh`
