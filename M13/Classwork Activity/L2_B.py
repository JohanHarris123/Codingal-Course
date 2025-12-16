import sqlite3
import pandas as pd

database = 'database.sqlite'

conn = sqlite3.connect(database)
print("Opened database successfully")

tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type='table';""", conn)

print("All Tables in the Database:")
print(tables)

teams = pd.read_sql("SELECT * FROM Team;", conn)

print("\nTeam Table (first 5 rows):")
print(teams.head())

matches = pd.read_sql("SELECT * FROM Match;", conn)

print("\nMatch Table (first 5 rows):")
print(matches.head())

MI_wins = pd.read_sql("""SELECT *
                      FROM Match
                      WHERE Match_Winner == 7;""", conn)

print("\n--- All MI Wins ---")
print(MI_wins)

MI_S8_S9 = pd.read_sql("""SELECT *
                       FROM Match
                          WHERE Match_Winner == 7 AND Season_Id IN (8, 9);""", conn)

print("\n--- MI Wins in Seasons 8 and 9 ---")
print(MI_S8_S9)

new_teams = pd.read_sql("""SELECT *
                        FROM Team
                        WHERE Team_Name LIKE 'De%';""", conn)

print("\n--- New Teams (Name starts with 'De') ---")
print(new_teams)

min_max_margin = pd.read_sql("""SELECT MIN(Win_Margin) AS Min_Margin, 
                             MAX(Win_Margin) AS Max_Margin
                             FROM Match;""", conn)

print("\n--- Minimum and Maximum Win Margins ---")
print(min_max_margin)