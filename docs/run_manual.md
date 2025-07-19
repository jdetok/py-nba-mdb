# running the fetch/load script manually
## build the container
run `docker compose -f compose-batch.yaml up --build`
## entrypoint: batch.py
accepts list of two dates, fetches games for all dates between
```python
dates = ['06/01/2016', '06/01/2017']
```
had to change the season too to match, need to look into this

# running the container to a terminal (to run the script directly)
`docker compose -f compose-it.yaml  run --rm --build py-load-it`