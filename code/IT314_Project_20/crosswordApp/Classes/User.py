

import uuid
import datetime

import bson
from pymongo.mongo_client import MongoClient

# Create a new client and connect to the server
client = MongoClient("mongodb+srv://Group20:Group20@cluster0.vl47pk0.mongodb.net/?retryWrites=true&w=majority")
db = client['CrossWordManagement']

class User:
    id: uuid
    username = ""
    email = ""
    password = ""

    def __init__(self, username, email, password):
        # unique_id = uuid.uuid4()

        # print("unique_id: " + str(unique_id))
        # self.id = unique_id
        self.username = username
        self.email = email
        self.password = password
        self.message = ""
        self.dateOfJoining = datetime.datetime.now()

        # print("")
    def __str__(self):
        return f"User: {self.username}"

    def check_username(self):

        if len(self.username) < 4:
            print("Username must be at least 4 characters long")
            self.message = "Username must be at least 4 characters long"
            return False

        print("Username is greater than 4 characters")

        if len(self.username) > 15:
            print("Username must be less than 15 characters long")
            self.message = "Username must be less than 15 characters long"
            return False

        print("Username is less than 15 characters")

        for i in self.username:
            if i!='_' and i.isalnum() == False:
                print(i)
                print("Username must be alphanumeric")
                self.message = "Username must be alphanumeric"
                return False

        print("Username is alphanumeric")

        reply = db['crosswordApp_user'].find_one({"username": self.username})

        if reply is not None:
            print("Username already exists")
            self.message = "Username already exists"
            return False

        print("Username is unique")

        return True

    def check_email(self):

        reply = db['crosswordApp_user'].find_one({"email": self.email})
        print(reply)
        if reply is not None:
            print("Email already exists")
            self.message = "Email already exists"
            return False
        return True
    def check_password(self):

        if len(self.password) < 8:
            print("Password must be at least 8 characters long")
            self.message = "Password must be at least 8 characters long"
            return False

        print("Password is greater than 8 characters")

        if len(self.password) > 24:
            print("Password must be less than 25 characters long")
            self.message = "Password must be less than 25 characters long"
            return False

        print("Password is less than 15 characters")

        upperCase = False
        lowerCase = False
        number = False
        aplhabet = False
        special = False

        for i in self.password:
            if i.isupper():
                upperCase = True
            elif i.islower():
                lowerCase = True
            elif i.isnumeric():
                number = True
            elif i.isalpha():
                alphabet = True
            else:
                special = True

        if not upperCase:
            print("Password must contain at least one uppercase letter")
            self.message = "Password must contain at least one uppercase letter"
            return False

        print("Password contains at least one uppercase letter")

        if not lowerCase:
            print("Password must contain at least one lowercase letter")
            self.message = "Password must contain at least one lowercase letter"
            return False

        print("Password contains at least one lowercase letter")

        if not number:
            print("Password must contain at least one number")
            self.message = "Password must contain at least one number"
            return False

        print("Password contains at least one number")

        if not special:
            print("Password must contain at least one special character")
            self.message = "Password must contain at least one special character"
            return False

        print("Password contains at least one special character")

        return True