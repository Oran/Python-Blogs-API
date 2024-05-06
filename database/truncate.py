from database.connect import *

def truncate_users():
    dbCursor.execute("TRUNCATE TABLE Users")
    conn.commit()

def truncate_posts():
    dbCursor.execute("TRUNCATE TABLE Posts")
    conn.commit()

def delete_user(id):
    dbCursor.execute(f"DELETE FROM Users WHERE id = {id}")
    conn.commit()

def delete_post(id):
    dbCursor.execute(f"DELETE FROM Posts WHERE id = {id}")
    conn.commit()