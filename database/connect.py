import sqlite3 as sql

try:
    with sql.connect("database.db") as conn:
        dbCursor = conn.cursor()
        print("Connected to the database")

except sql.OperationalError as e:
    print("Error connecting to the database:", e)