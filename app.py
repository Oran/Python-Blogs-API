from fastapi import Depends, FastAPI, HTTPException
from database.add_records import add_post, add_user
from database.read_records import get_api_keys, get_posts, get_users
from database.truncate import delete_post, delete_user
from database.create_tables import *
from functions import check_api_key, hash_password

app = FastAPI()

@app.get("/test")
async def test(key: str):
    isThere = check_api_key(key)

    if isThere:
        return {"message": f"API Key is valid -> {isThere}"}
    else:
        return HTTPException(status_code=401, detail="Invalid API Key")


# Get All Users
@app.get("/db/get/user")
async def getUsers(key: str):
    if check_api_key(key):
        data = get_users()
        return {"data": data}
    else:
        return HTTPException(status_code=401, detail="Invalid API Key")

# Get All Posts
@app.get("/db/get/post")
async def getPosts(key: str):
    if check_api_key(key):
        data = get_posts()
        return {"data": data}
    else:
        return HTTPException(status_code=401, detail="Invalid API Key")

# Add User
@app.post("/db/add/user")
async def addUser(body: dict, key: str):

    if check_api_key(key):
        hashed_password = hash_password(body["password"])
        add_user(body["name"], body["email"], hashed_password)
        return {"message": f"Added to the database"}
    else:
        return HTTPException(status_code=401, detail="Invalid API Key")

# Add Post to specific user
@app.post("/db/add/post")
async def addPost(body: dict, key: str):
    if check_api_key(key):
        add_post(body["title"], body["body"], body["userId"])
        return {"message": f"Added post for user {body['userId']} to the database"}
    else:
        return HTTPException(status_code=401, detail="Invalid API Key")

# Delete Specific Post
@app.post("/db/delete/post={id}")
async def deletePost(id: int, key: str):
    if check_api_key(key):
        delete_post(id)
        return {"message": f"Deleted post with id {id}"}
    else:
        return HTTPException(status_code=401, detail="Invalid API Key")
    
# Delete Specific User
@app.post("/db/delete/user")
async def deleteUser(id: int, key: str):
    if check_api_key(key):
        delete_user(id)
        return {"message": f"Deleted user with id {id}"}
    else:
        return HTTPException(status_code=401, detail="Invalid API Key")