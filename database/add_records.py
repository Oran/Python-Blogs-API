from database.connect import *
from functions import generate_api_key

def add_user(name, email, password):
    dbCursor.execute("INSERT INTO Users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
    dbCursor.execute("INSERT INTO APIKeys (key, userId) VALUES (?, ?)", (generate_api_key(), dbCursor.lastrowid))
    conn.commit()

def add_post(title, body, userId):
    dbCursor.execute("INSERT INTO Posts (title, body, userId) VALUES (?, ?, ?)", (title, body, userId))
    conn.commit()