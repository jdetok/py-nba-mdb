Upon execution this project fetches game logs from the nba-api package, cleans & transforms the data, and inserts the data into a mariadb database hosted in a docker container locally on my raspberry pi 5. 

PY FILES: 
- fetch.py - uses the nba-api package to call the nba stats website and fetch data
- clean.py - cleans team and player game log data. two classes, TeamData and PlayerData return dataframes formatted the same as my database tables
- main.py - file that will be run nightly with a cron job
- run.py - contains process flow functions
- conn.py - database connection/operations
- batch.py - run program for a range of dates
- logs.py - central logger to projectroot/logs in the container

# TODO - BUILD IN PLAY BY PLAY FETCH/CLEAN
