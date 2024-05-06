from database.connect import *

def add_user(name, email, password):
    dbCursor.execute("INSERT INTO Users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
    conn.commit()

def add_post(title, body, userId):
    dbCursor.execute("INSERT INTO Posts (title, body, userId) VALUES (?, ?, ?)", (title, body, userId))
    conn.commit()