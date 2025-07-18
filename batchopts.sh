#!/bin/bash

OPTSTRING=":b"

# cd into dir with compose.yaml
cd /home/jdeto/dkr/py-load

# compose up to run the script
while getopts ${OPTSTRING} opt; do
    case ${opt} in
        b) docker compose -f compose-batch.yaml up --build -d;;
        ?) docker compose -f compose-batch.yaml up -d;;
    esac
done

echo "python script running..."
docker wait pynba

# copy the logs
docker cp pynba:/usr/py/logs/. ./logs

# compose down after script is finished
docker compose -f compose-batch.yaml down