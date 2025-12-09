import sqlite3
import pandas as pd

conn = sqlite3.connect('database.sqlite')
print("Opened database successfully")

conn.execute('''CREATE TABLE CLASS_10 
             (SNO INT PRIMARY KEY NOT NULL, 
             Roll_No INT NOT NULL, 
             Name TEXT NOT NULL, 
             AGE INT DEFAULT 15, 
             Gender TEXT NOT NULL,
             Email_ID TEXT NOT NULL,
             Contact_No REAL NOT NULL);''')

print("Table created successfully")

conn.execute("""INSERT INTO CLASS_10 (SNO, Roll_No, NAME, AGE, Gender, Email_ID, Contact_No)
VALUES (1, 1, 'Allen', 14, 'Male', 'allen@gmail.com', 8088900 );""")

conn.execute("""INSERT INTO CLASS_10 (SNO, Roll_No, NAME, AGE, Gender, Email_ID, Contact_No)
VALUES (2, 2, 'Aisha', 14, 'Female', 'aish@gmail.com', 9080900 );""")

conn.execute("""INSERT INTO CLASS_10 (SNO, Roll_No, NAME, AGE, Gender, Email_ID, Contact_No)
VALUES (3, 3, 'Jeff', 15, 'Male', 'allen@gmail.com', 9909000 );""")

conn.commit()
print("Records created successfully")

tables = pd.read_sql("""SELECT *
                     FROM sqlite_master
                     WHERE type='table';""", conn)

print(tables)

class_10d = pd.read_sql("""SELECT * FROM CLASS_10;""", conn)

print(class_10d.head())