-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

 DROP DATABASE IF EXISTS tournament;
 CREATE DATABASE tournament;
 \c tournament;
 CREATE TABLE Players(id SERIAL PRIMARY KEY,
			name VARCHAR(30));
 CREATE TABLE Matches(winner integer references Players(id),
					loser integer references Players(id),
					PRIMARY KEY(winner, loser));
 DROP VIEW IF EXISTS vw_pl_stand;
 CREATE VIEW vw_pl_stand AS
	SELECT p.id, p.name,
            (SELECT count(*) FROM Matches AS m WHERE m.winner = p.id) AS wins,
            (SELECT count(*) FROM Matches AS mm WHERE mm.winner = p.id or mm.loser = p.id) AS matches
            FROM Players AS p
            ORDER BY wins DESC;