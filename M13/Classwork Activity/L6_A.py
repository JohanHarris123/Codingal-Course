import pandas as pd
import sqlite3

database = 'database.sqlite'
conn = sqlite3.connect(database)

tables = pd.read_sql("""SELECT name
                    FROM sqlite_master 
                     WHERE type='table';""", conn)

print(tables)

match = pd.read_sql("""SELECT *
                    FROM Match""", conn)
print("match", match)

venue = pd.read_sql("""SELECT *
                    FROM Venue""", conn)
print("venue", venue)

city = pd.read_sql("""SELECT *
                    FROM City""", conn)
print("city", city)

team = pd.read_sql("""SELECT *
                    FROM Team""", conn)
print("team", team)

match_details = pd.read_sql("""SELECT m.Season_Id, m.Match_Id,
v.Venue_Name, c.City_Name, t.Team_Name AS Winner
FROM Match AS m
INNER JOIN Venue AS v ON m.Venue_Id = v.Venue_Id
INNER JOIN City AS c ON v.City_Id = c.City_Id
INNER JOIN Team AS t ON m.Match_Winner = t.Team_Id;""",
conn)

print(match_details)
print(match.columns)