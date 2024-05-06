from fastapi import FastAPI
from database.add_records import add_post, add_user
from database.read import get_posts, get_users
from database.truncate import delete_post
from functions import hash_password

app = FastAPI()

# Get All Users
@app.get("/db/user/get")
async def getUsers():
    data = get_users()
    return {"data": data}

# Get All Posts
@app.get("/db/post/get")
async def getPosts():
    data = get_posts()
    return {"data": data}

# Add User
@app.post("/db/user/add")
async def addUser(body: dict):
    hashed_password = hash_password(body["password"])
    print(hashed_password)
    add_user(body["name"], body["email"], hashed_password)
    return {"message": f"Added to the database"}

# Add Post to specific user
@app.post("/db/post/add")
async def addPost(body: dict):
    add_post(body["title"], body["body"], body["userId"])
    print("Added post")
    return {"message": f"Added post for user {body['userId']} to the database"}



# Delete Specific Post
@app.post("/db/post/delete")
async def deletePost(id: int):
    delete_post(id)
    return {"message": f"Deleted post with id {id}"}

# Delete Specific User
@app.get("/db/user/delete")
async def deleteUser(id: int):
    delete_post(id)
    return {"message": f"Deleted user with id {id}"}