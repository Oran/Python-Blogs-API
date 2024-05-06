from fastapi import FastAPI
from database.add_records import add_post, add_user
from database.read import get_posts, get_users
from functions import hash_password

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/db/user/get")
async def getUsers():
    data = get_users()
    return {"data": data}

@app.post("/db/user/add")
async def addUser(body: dict):
    hashed_password = hash_password(body["password"])
    print(hashed_password)
    add_user(body["name"], body["email"], hashed_password)
    return {"message": f"Added to the database"}

@app.post("/db/post/add")
async def addPost(body: dict):
    add_post(body["title"], body["body"], body["userId"])
    print("Added post")
    return {"message": f"Added post for user {body['userId']} to the database"}

@app.get("/db/post/get")
async def getPosts():
    data = get_posts()
    return {"data": data}