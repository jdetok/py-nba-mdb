# source nba/wnba data using nba_api python package

this code feeds the backend database that serves the nba/wnba stats website i built. 
see the site at https://jdeko.me/bball or the source code at https://github.com/jdetok/go-api-jdeko.me

## running the project
this project is run nightly in a cronjob. the cronjob executes run.sh, which builds, runs, and removes the docker container this source code is designed for. the container is configured to connect to my backend docker network, which allows communication with the database

## database 
the mariadb database this python project interacts with is run in an indpendent docker container, which is configured with the contents of this repo: https://github.com/jdetok/docker-mdb-nba

### short desc. of .py files (in /src)
- fetch.py - uses the nba-api package to call the nba stats website and fetch data
- clean.py - cleans team and player game log data. two classes, TeamData and PlayerData return dataframes formatted the same as my database tables
- main.py - file that will be run nightly with a cron job
- run.py - contains process flow functions
- conn.py - database connection/operations
- batch.py - run program for a range of dates
- logs.py - central logger to projectroot/logs in the container
