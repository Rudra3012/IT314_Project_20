

import uuid
import datetime

import bson


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

        self.dateOfJoining = datetime.datetime.now()

        # print("")
    def __str__(self):
        return f"User: {self.username}"
