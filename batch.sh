#!/bin/bash

# cd into dir with compose.yaml
cd /home/jdeto/dkr/py-load

# compose up to run the script
docker compose -f compose-batch.yaml up --build -d

echo "python script running..."
docker wait pynba

# copy the logs
docker cp pynba:/usr/py/logs/. ./logs

# compose down after script is finished
docker compose -f compose-batch.yaml down