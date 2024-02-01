# Munster Stats
#### Video Demo: https://youtu.be/D0hPRuV6b_0
#### Description: 
Munster Stats is a Flask web application that compiles various datapoints pulled from a local PostgreSql database. 

## Features

* View Munster Rugby Player Base, which provides information on names, ages, positions, match appearances (caps), tries scored, last match played, injury status
* View ongoing player contracts, their status, contract issuer, expiry
* View injury status of players; the nature of the injury, expected return
* Add/update contracts
* Add/update/remove injuries from the injury reports
* Add new players to the database, edit existing players
* View match reports that provide information on opposition, venue, competition, stage of competition, and the team named
* Add match reports, filling in the team that played

## Build

* install pyscopg2 for Python/PostgreSQL integration
* install dotenv for .env file environmental variables
* install flask
* venv used to run virtual flask environment. Documention here; https://docs.python.org/3/library/venv.html
* copy and paste the SQL queries in 'init.db' to your local PostgreSQL application to create the database structure 

## Run 

* Navigate to project folder and run "source .venv/bin/acivate". 
* Then run flask run
* Follow the provided link

## Additional Notes

* This project was designed utilising a local postgresql database. In prinicple, it will work with any rugby team, or, with minor changes to datapoints, PostgreSQL columns, etc, any sport team at all.
* Bootstrap was used in the structuring of the nav bar, input fields, and forms