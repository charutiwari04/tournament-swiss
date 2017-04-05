
## About - Tournament Results Database
This project showcases how to use Python code that uses the relational database PostgreSQL to keep track of players and matches in a game tournament. Here the game refers to Swiss Tournament where each player plays in every round even if the player is winner or loser in previous rounds.  

## How to Setup and Run the project
1. Install Vagrant Virtual Machine.
2. Vagrant VM has PostgreSQL installed and configured.
3. clone or download the project files in tournament folder under vagrant as /vagrant/tournament
4. Navigate to /vagrant/tournament which will have files as
    
    a. tournament.sql  - Code for setting up Database Schema

    b. tournament.py - Various functions to connect to database and also to manipulate database.

    c. tournament_test.py - client program to test the implementation of tournament.py


5.  Start the Vagrant VM by writing commands as "vagrant up" and "vagrant ssh"
6. Once the Database Schema queries are written in tournament.sql, Use command following command to execute them:

$ psql -i tournament.sql 

7. When all the functions in the tournament.py file are complete and ready to run. Run following command to test the implementation:

$ python tournament_test.py

If this command gives final result as "Success!  All tests pass!", it means code is good, Otherwise instructions will be given along with the error.

## Important points for coding SQL and Python files.
1. Create the Database Schema, Tables Or Views in tournament.sql, Tables should follow the relational database normal forms. This should be written in tournament.sql
2. Write various python function in tournament.py for:
    
    a.  connecting to the database. 
    
    b.  Manipulating the database by using SELECT or DELETE/TRUNCATE or INSERT SQL queries. 
    
    c.  Logic for pairing the players according to Swiss tournament rules.

## Skills involved
1. Python
2. Python-DB-API
3. PostgreSQL database
