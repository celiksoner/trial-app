import jwt

key = "test"

users = {
    "soner": "123"
}

def check_user(username, password):
    if username in users and users[username] == password:
        token = jwt.encode({"username": username}, key)
        return token
    return False 