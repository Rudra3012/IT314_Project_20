import uuid
import datetime
class User:

    id=0
    username=""
    password=""
    email=""
    dateOfJoining=""

    def __init__(self, username, password, email):
        unique_id = uuid.uuid4()
        print("unique_id: " + str(unique_id))
        self.id=unique_id
        self.username=username
        self.password=password
        self.email=email
        self.dateOfJoining = datetime.datetime.now()

    def __str__(self):
        return f"User: {self.username}"