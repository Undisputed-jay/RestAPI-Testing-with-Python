def createUserPayload():
    body = {
        "name": "morpheus",
        "job": "leader"
    }
    return body

def updateUser():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    return body

def registerUser():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    return body

def registerUserIncomplete():
    body = {
        "email": "sydney@fife"
    }
    return body

def loginUser():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    return body

def loginWrongUser():
    body = {
        "email": "peter@klaven"
    }
    return body
