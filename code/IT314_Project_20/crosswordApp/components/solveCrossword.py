from bson import ObjectId
from django_unicorn.components import UnicornView, PollUpdate

from django.utils.timezone import now
from pymongo import MongoClient
from django.contrib import messages
import json
import time

client = MongoClient("mongodb+srv://Group20:Group20@cluster0.vl47pk0.mongodb.net/?retryWrites=true&w=majority")
db = client['CrossWordManagement']
collections = db['crosswordApp_crossword']


class SolvecrosswordView(UnicornView):
    username = ""
    crosswordId = ""
    cluesHor = []
    cluesVer = []
    height = 0
    width = 0
    horAnswers = []
    verAnswers = []
    grid = []
    AnswersHorStart = []
    AnswersVerStart = []
    correctGrid = []
    HorAnswersDict = {}
    VerAnswersDict = {}
    startTime: float = 0
    endTime: float = 0
    current_time = time.time()
    timeElapsed: float = 0
    attemptNumber: int = 0
    status: str = "presolve"
    message_content: str = ""
    message_type = ""
    displayMessage : str = "no"

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

    def mount(self):
        self.displayMessage = "no"
        self.cluesHor = []
        self.cluesVer = []
        self.grid = []
        self.horAnswers = []
        self.verAnswers = []
        self.AnswersHorStart = []
        self.AnswersVerStart = []
        self.startTime: float = 0
        self.endTime: float = 0
        self.current_time = time.time()
        self.timeElapsed: float = 0
        reply = collections.find_one({"_id": ObjectId(self.crosswordId)})

        repliedCluesHor = reply['cluesHor']
        repliedCluesVer = reply['cluesVer']
        repliedAnswersHor = reply['AnswersHor']
        repliedAnswersVer = reply['AnswersVer']
        self.AnswersHorStart = reply['AnswersHorStart']
        self.AnswersVerStart = reply['AnswersVerStart']
        self.horAnswers = reply['AnswersHor']
        self.verAnswers = reply['AnswersVer']
        self.height = reply['height']
        self.width = reply['width']

        self.correctGrid = reply['grid']

        for key, value in repliedCluesHor.items():
            self.cluesHor.append((len(repliedAnswersHor[int(key)]), key, value))

        for key, value in repliedCluesVer.items():
            self.cluesVer.append((len(repliedAnswersVer[int(key)]), key, value))

        print(self.height)
        print(self.width)
        print(self.AnswersHorStart)
        print(self.AnswersVerStart)
        print(repliedAnswersHor)
        print(repliedAnswersVer)
        row = []

        for i in range(self.height):
            for j in range(self.width):
                if self.correctGrid[i][j] == "_":
                    row.append("_")
                else:
                    row.append(" ")
            self.grid.append(row)
            row = []

        print(self.grid)

        self.HorAnswersDict = {
            "0": self.HorAnswer1,
            "1": self.HorAnswer2,
            "2": self.HorAnswer3,
            "3": self.HorAnswer4,
            "4": self.HorAnswer5,
            "5": self.HorAnswer6,
            "6": self.HorAnswer7,
            "7": self.HorAnswer8,
            "8": self.HorAnswer9,
            "9": self.HorAnswer10,
            "10": self.HorAnswer11,
            "11": self.HorAnswer12,
            "12": self.HorAnswer13,
            "13": self.HorAnswer14,
            "14": self.HorAnswer15
        }

        self.VerAnswersDict = {
            "0": self.VerAnswer1,
            "1": self.VerAnswer2,
            "2": self.VerAnswer3,
            "3": self.VerAnswer4,
            "4": self.VerAnswer5,
            "5": self.VerAnswer6,
            "6": self.VerAnswer7,
            "7": self.VerAnswer8,
            "8": self.VerAnswer9,
            "9": self.VerAnswer10,
            "10": self.VerAnswer11,
            "11": self.VerAnswer12,
            "12": self.VerAnswer13,
            "13": self.VerAnswer14,
            "14": self.VerAnswer15
        }

    def current_grid(self):

        tempgrid = []
        row = []

        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == "_":
                    row.append("_")
                else:
                    row.append(" ")
            tempgrid.append(row)
            row = []

        if len(self.horAnswers) > 0:
            if self.HorAnswer1 != "":
                for i in range(len(self.HorAnswer1)):
                    tempgrid[self.AnswersHorStart[0][0]][self.AnswersHorStart[0][1] + i] = self.HorAnswer1[i]

        if len(self.horAnswers) > 1:
            if self.HorAnswer2 != "":
                for i in range(len(self.HorAnswer2)):
                    tempgrid[self.AnswersHorStart[1][0]][self.AnswersHorStart[1][1] + i] = self.HorAnswer2[i]

        if len(self.horAnswers) > 2:
            if self.HorAnswer3 != "":
                for i in range(len(self.HorAnswer3)):
                    tempgrid[self.AnswersHorStart[2][0]][self.AnswersHorStart[2][1] + i] = self.HorAnswer3[i]

        if len(self.horAnswers) > 3:
            if self.HorAnswer4 != "":
                for i in range(len(self.HorAnswer4)):
                    tempgrid[self.AnswersHorStart[3][0]][self.AnswersHorStart[3][1] + i] = self.HorAnswer4[i]

        if len(self.horAnswers) > 4:
            if self.HorAnswer5 != "":
                for i in range(len(self.HorAnswer5)):
                    tempgrid[self.AnswersHorStart[4][0]][self.AnswersHorStart[4][1] + i] = self.HorAnswer5[i]

        if len(self.horAnswers) > 5:
            if self.HorAnswer6 != "":
                for i in range(len(self.HorAnswer6)):
                    tempgrid[self.AnswersHorStart[5][0]][self.AnswersHorStart[5][1] + i] = self.HorAnswer6[i]

        if len(self.horAnswers) > 6:
            if self.HorAnswer7 != "":
                for i in range(len(self.HorAnswer7)):
                    tempgrid[self.AnswersHorStart[6][0]][self.AnswersHorStart[6][1] + i] = self.HorAnswer7[i]

        if len(self.horAnswers) > 7:
            if self.HorAnswer8 != "":
                for i in range(len(self.HorAnswer8)):
                    tempgrid[self.AnswersHorStart[7][0]][self.AnswersHorStart[7][1] + i] = self.HorAnswer8[i]

        if len(self.horAnswers) > 8:
            if self.HorAnswer9 != "":
                for i in range(len(self.HorAnswer9)):
                    tempgrid[self.AnswersHorStart[8][0]][self.AnswersHorStart[8][1] + i] = self.HorAnswer9[i]

        if len(self.horAnswers) > 9:
            if self.HorAnswer10 != "":
                for i in range(len(self.HorAnswer10)):
                    tempgrid[self.AnswersHorStart[9][0]][self.AnswersHorStart[9][1] + i] = self.HorAnswer10[i]

        if len(self.verAnswers) > 0:
            if self.VerAnswer1 != "":
                for i in range(len(self.VerAnswer1)):
                    tempgrid[self.AnswersVerStart[0][0] + i][self.AnswersVerStart[0][1]] = self.VerAnswer1[i]

        if len(self.verAnswers) > 1:
            if self.VerAnswer2 != "":
                for i in range(len(self.VerAnswer2)):
                    tempgrid[self.AnswersVerStart[1][0] + i][self.AnswersVerStart[1][1]] = self.VerAnswer2[i]

        if len(self.verAnswers) > 2:
            if self.VerAnswer3 != "":
                for i in range(len(self.VerAnswer3)):
                    tempgrid[self.AnswersVerStart[2][0] + i][self.AnswersVerStart[2][1]] = self.VerAnswer3[i]

        if len(self.verAnswers) > 3:
            if self.VerAnswer4 != "":
                for i in range(len(self.VerAnswer4)):
                    tempgrid[self.AnswersVerStart[3][0] + i][self.AnswersVerStart[3][1]] = self.VerAnswer4[i]

        if len(self.verAnswers) > 4:
            if self.VerAnswer5 != "":
                for i in range(len(self.VerAnswer5)):
                    tempgrid[self.AnswersVerStart[4][0] + i][self.AnswersVerStart[4][1]] = self.VerAnswer5[i]

        if len(self.verAnswers) > 5:
            if self.VerAnswer6 != "":
                for i in range(len(self.VerAnswer6)):
                    tempgrid[self.AnswersVerStart[5][0] + i][self.AnswersVerStart[5][1]] = self.VerAnswer6[i]

        if len(self.verAnswers) > 6:
            if self.VerAnswer7 != "":
                for i in range(len(self.VerAnswer7)):
                    tempgrid[self.AnswersVerStart[6][0] + i][self.AnswersVerStart[6][1]] = self.VerAnswer7[i]

        if len(self.verAnswers) > 7:
            if self.VerAnswer8 != "":
                for i in range(len(self.VerAnswer8)):
                    tempgrid[self.AnswersVerStart[7][0] + i][self.AnswersVerStart[7][1]] = self.VerAnswer8[i]

        if len(self.verAnswers) > 8:
            if self.VerAnswer9 != "":
                for i in range(len(self.VerAnswer9)):
                    tempgrid[self.AnswersVerStart[8][0] + i][self.AnswersVerStart[8][1]] = self.VerAnswer9[i]

        if len(self.verAnswers) > 9:
            if self.VerAnswer10 != "":
                for i in range(len(self.VerAnswer10)):
                    tempgrid[self.AnswersVerStart[9][0] + i][self.AnswersVerStart[9][1]] = self.VerAnswer10[i]

        for i in range(self.height):
            for j in range(self.width):
                if tempgrid[i][j] != " " and tempgrid[i][j] != "_":
                    tempgrid[i][j] = tempgrid[i][j].upper()
                print(tempgrid[i][j], end=" ")
            print()

        return tempgrid

    def submitClicked(self):
        inputCorrect = True
        if len(self.horAnswers) > 0:
            if self.HorAnswer1.upper() == self.horAnswers[0]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.horAnswers) > 1:
            if self.HorAnswer2.upper() == self.horAnswers[1]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.horAnswers) > 2:
            if self.HorAnswer3.upper() == self.horAnswers[2]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.horAnswers) > 3:
            if self.HorAnswer4.upper() == self.horAnswers[3]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.horAnswers) > 4:
            if self.HorAnswer5.upper() == self.horAnswers[4]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.horAnswers) > 5:
            if self.HorAnswer6.upper() == self.horAnswers[5]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.horAnswers) > 6:
            if self.HorAnswer7.upper() == self.horAnswers[6]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.horAnswers) > 7:
            if self.HorAnswer8.upper() == self.horAnswers[7]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.horAnswers) > 8:
            if self.HorAnswer9.upper() == self.horAnswers[8]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.horAnswers) > 9:
            if self.HorAnswer10.upper() == self.horAnswers[9]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.verAnswers) > 0:
            if self.VerAnswer1.upper() == self.verAnswers[0]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.verAnswers) > 1:
            if self.VerAnswer2.upper() == self.verAnswers[1]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.verAnswers) > 2:
            if self.VerAnswer3.upper() == self.verAnswers[2]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.verAnswers) > 3:
            if self.VerAnswer4.upper() == self.verAnswers[3]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.verAnswers) > 4:
            if self.VerAnswer5.upper() == self.verAnswers[4]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.verAnswers) > 5:
            if self.VerAnswer6.upper() == self.verAnswers[5]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.verAnswers) > 6:
            if self.VerAnswer7.upper() == self.verAnswers[6]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.verAnswers) > 7:
            if self.VerAnswer8.upper() == self.verAnswers[7]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.verAnswers) > 8:
            if self.VerAnswer9.upper() == self.verAnswers[8]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if len(self.verAnswers) > 9:
            if self.VerAnswer10.upper() == self.verAnswers[9]:
                print("Correct")
            else:
                inputCorrect = False
                print("Incorrect")

        if inputCorrect:
            self.status = "solved"
            print("Congratulations, you have completed the crossword")
        else:
            self.displayMessage = "yes"
            self.message_type = "errorMessage"
            self.message_content = "Answers are not correct. Try again."
            self.attemptNumber += 1
            print(f'Attempt number: {self.attemptNumber}')
            print(f'message type: {self.message_type}')
            print(f'message content: {self.message_content}')
            print("Sorry, you have not completed the crossword")

    def beginSolving(self):
        self.startTime = time.time()
        self.status = "unsolved"
        self.call("startTimer")

    def hideMessage(self):
        print("hide message called")
        self.displayMessage = "no"