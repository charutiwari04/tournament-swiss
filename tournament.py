#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Database Connection Error")

def deleteMatches():
    """Remove all the match records from the database."""
    conn, cursor = connect()
    query = """ TRUNCATE TABLE Matches; """
    cursor.execute(query)
    conn.commit()
    conn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    conn, cursor = connect()
    query = """ TRUNCATE TABLE Players CASCADE; """
    cursor.execute(query)
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn, cursor = connect()
    query = """ select count(*) from Players """
    cursor.execute(query)
    cnt = cursor.fetchone()
    return cnt[0]
    conn.close()
    

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn, cursor = connect()
    query = """ insert into Players (name) values(%s); """
    parameter = (name,)
    cursor.execute(query, parameter)
    conn.commit()
    conn.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn, cursor = connect()
    query = """select * from vw_pl_stand;"""
    cursor.execute(query)
    results = cursor.fetchall()
    return results
    conn.close()
    
def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn, cursor = connect()
    query = """ insert into Matches values(%s, %s); """
    parameter = (winner, loser)
    cursor.execute(query, parameter)
    conn.commit()
    conn.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    no_of_players = countPlayers()
    playerRecords = playerStandings()
    allPairs = []
    evenPairs = []
    oddPairs = []
    for i in range(len(playerRecords)):
        if i%2 == 0:
            evenPairs.append((playerRecords[i][0], playerRecords[i][1]))
        else:
            oddPairs.append((playerRecords[i][0], playerRecords[i][1]))
    for x, y in zip(evenPairs, oddPairs):
        allPairs.append(x+y)
    return allPairs
