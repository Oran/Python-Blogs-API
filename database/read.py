from database.connect import *

def get_users():
    try:
        dbCursor.execute("SELECT * FROM Users")
        data = dbCursor.fetchall()
        return data
    except sql.OperationalError as e:
        print("Error connecting to the database:", e)

def get_posts():
    try:
        dbCursor.execute("SELECT * FROM Posts")
        data = dbCursor.fetchall()
        return data
    except sql.OperationalError as e:
        print("Error connecting to the database:", e)

def get_posts_by_user(userId):
    try:
        dbCursor.execute("SELECT * FROM Posts WHERE userId = ?", (userId,))
        data = dbCursor.fetchall()
        return data
    except sql.OperationalError as e:
        print("Error connecting to the database:", e)