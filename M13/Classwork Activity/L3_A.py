import pandas as pd
import sqlite3
database = 'database.sqlite'
conn = sqlite3.connect(database)

tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type='table';""", conn)

print(tables)

matches = pd.read_sql("SELECT * FROM Match;", conn)
print(matches.head())

result1 = pd.read_sql("""SELECT AVG(Win_Margin) AS Avg_Margin,
                      Match_Winner
                        FROM Match
                        WHERE Season_Id = 9
                      GROUP BY Match_Winner
                      ORDER BY AVG(Win_Margin);""", conn)

print(result1)

result2 = pd.read_sql("""
                      SELECT COUNT(DISTINCT Venue_Id) as venue_count
                        FROM Match
                        WHERE Season_Id = 9;""", conn)

print(result2)

result3 = pd.read_sql("""
    SELECT MIN(Win_Margin) AS Min_Margin,
           MAX(Win_Margin) AS Max_Margin,
           AVG(Win_Margin) AS Avg_Margin,
           COUNT(DISTINCT Man_of_the_Match) AS unique_mom_players
    FROM Match;""", conn)

print(result3)

result4 = pd.read_sql("""
    SELECT SUM(Win_Margin) AS total_win_margin
    FROM Match
    WHERE Season_Id = 9;""", conn)

print(result4)