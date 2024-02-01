# Munster Stats
#### Video Demo: https://youtu.be/D0hPRuV6b_0
#### Description: 
Munster Stats is a Flask web application that compiles various datapoints pulled from a local PostgreSql database. Using the program you can view a brief summary of player details, such as their name, date of birth, position, points scored, match appearances etc. You can also view match reports which summarise the opponent, venue, competition, and points scored by each team, as well as the named team for Munster

The Injury Reports tab allows you to add new injuries, update existing ones, or remove current ones that have since expired. All of this causes a dynamic change in the data that appears to you on the website while concurrently carrying out SQL queries to the local database to reflect the changes that the user made on the front-end. 

Contracts works in much the same way as Injury Reports. Users can update, amend, and remove contract information here. Only players with existing contracts can have contracts edited, while any player can have a new contract added. 

Add Data is the most involved section of the site. It allows users to add new players to the database, edit existing players, and add new matches to the Match Report section. Adding a new player causes their data to appear in the Player Base section of the site, while adding new Match Reports causes the match to appear on that same Match Report section of the site. 

This dynamic Flask application supplies concise datapoints to the user that, with tweaks to various data fields, could be ammended to be used for not just any rugby team, but any sports team in general. 

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