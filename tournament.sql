-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

 CREATE DATABASE tournament;
 \c tournament;
 CREATE TABLE Players(id SERIAL PRIMARY KEY,
			name VARCHAR(30));
 CREATE TABLE Matches(winner integer references Players(id),
					loser integer references Players(id),
					PRIMARY KEY(winner, loser));