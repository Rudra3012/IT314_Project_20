from bson import ObjectId
from django_unicorn.components import UnicornView

from crosswordApp.Classes.Crossword import Crossword
from crosswordApp.Classes.User import User
from pymongo import MongoClient
from django.contrib import messages
import json

client = MongoClient('mongodb+srv://Group20:Group20@cluster0.agetwho.mongodb.net/?retryWrites=true&w=majority')
db = client['CrossWordManagement']
collections = db['crosswordApp_crossword']


class SolvecrosswordView(UnicornView):
    username = ""
    crosswordId = ""
    cluesHor = []
    cluesVer = []
    horAnswers = []
    verAnswers = []
    grid= []

    HorAnswer1 = ""
    HorAnswer2 = ""
    HorAnswer3 = ""
    HorAnswer4 = ""
    HorAnswer5 = ""
    HorAnswer6 = ""
    HorAnswer7 = ""
    HorAnswer8 = ""
    HorAnswer9 = ""
    HorAnswer10 = ""
    HorAnswer11 = ""
    HorAnswer12 = ""
    HorAnswer13 = ""
    HorAnswer14 = ""
    HorAnswer15 = ""

    VerAnswer1 = ""
    VerAnswer2 = ""
    VerAnswer3 = ""
    VerAnswer4 = ""
    VerAnswer5 = ""
    VerAnswer6 = ""
    VerAnswer7 = ""
    VerAnswer8 = ""
    VerAnswer9 = ""
    VerAnswer10 = ""
    VerAnswer11 = ""
    VerAnswer12 = ""
    VerAnswer13 = ""
    VerAnswer14 = ""
    VerAnswer15 = ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.username = kwargs.get("username")
        self.crosswordId = kwargs.get("crosswordId")
        self.cluesHor = []
        self.cluesVer = []
        reply = collections.find_one({"_id": ObjectId(self.crosswordId)})

        repliedCluesHor = reply['cluesHor']
        repliedCluesVer = reply['cluesVer']
        self.grid = reply['grid']

        for key, value in repliedCluesHor.items():
            self.cluesHor.append((key, value))

        for key, value in repliedCluesVer.items():
            self.cluesVer.append((key, value))

        print(self.cluesHor)
        print(self.cluesVer)