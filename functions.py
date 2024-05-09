import bcrypt
import cuid2
from database.read_records import get_api_keys

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def generate_api_key():
    return str(cuid2.Cuid().generate())

def check_api_key(key):
    api_keys = get_api_keys()
    for i in range(len(api_keys)): # type: ignore
        if api_keys[i][1] == key: # type: ignore
            return True
    return False