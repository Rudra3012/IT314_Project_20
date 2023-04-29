from django.shortcuts import redirect
from django_unicorn.components import UnicornView

from crosswordApp.Classes.Crossword import Crossword
from crosswordApp.Classes.User import User
from pymongo import MongoClient

import json

client = MongoClient("mongodb+srv://Group20:Group20@cluster0.vl47pk0.mongodb.net/?retryWrites=true&w=majority")
db = client['CrossWordManagement']
collections = db['crosswordApp_crossword']


class CreatecrosswordmanualView(UnicornView):
    username = ""

    title = ""
    description = ""

    rows: str = '0'
    cols: str = '0'
    grid = []
    characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z', '_']
    activeChar = '_'
    activeStep = 1
    roadMapStatusLabel1 = ""
    roadMapStatusLabel2 = "Empty"
    roadMapStatusLabel3 = "Empty"
    roadMapStatusLabel4 = "Empty"
    roadMapStatusLabel5 = "Empty"

    wordsHorizontalStart = []
    wordsVerticalStart = []
    wordsHorizontal = []
    wordsVertical = []

    horClue1 = ""
    horClue2 = ""
    horClue3 = ""
    horClue4 = ""
    horClue5 = ""
    horClue6 = ""
    horClue7 = ""
    horClue8 = ""
    horClue9 = ""
    horClue10 = ""
    horClue11 = ""
    horClue12 = ""
    horClue13 = ""
    horClue14 = ""
    horClue15 = ""
    horClues = {}
    verClue1 = ""
    verClue2 = ""
    verClue3 = ""
    verClue4 = ""
    verClue5 = ""
    verClue6 = ""
    verClue7 = ""
    verClue8 = ""
    verClue9 = ""
    verClue10 = ""
    verClue11 = ""
    verClue12 = ""
    verClue13 = ""
    verClue14 = ""
    verClue15 = ""
    verClues = {}
    currentStep:str = 'Enter Title and Description'
    message_content: str = ""
    message_type = ""
    displayMessage: str = "no"

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        username = kwargs.get("username")


    def incrementStep(self):
        if self.activeStep == 1:
            if self.title == "":
                self.message_content = "Please enter a title"
                self.message_type = "errorMessage"
                self.displayMessage = "yes"
                return
            if self.description == "":
                self.message_content = "Please enter a description"
                self.message_type = "errorMessage"
                self.displayMessage = "yes"
                return
        self.activeStep += 1
        if self.activeStep == 2:
            self.roadMapStatusLabel2 = ""
            self.displayMessage = "no"
            self.currentStep = "Generate Grid"
        if self.activeStep == 3:
            self.roadMapStatusLabel3 = ""
            self.displayMessage = "no"
            self.currentStep = "Fill Grid"
        if self.activeStep == 4:
            self.roadMapStatusLabel4 = ""
            self.displayMessage = "no"
            self.currentStep = "Enter Clues"
        if self.activeStep == 5:
            self.roadMapStatusLabel5 = ""
            self.currentStep = "Saved Successfully"
            self.displayMessage = "no"
        print(self.activeStep)

    def roadMapBack(self):
        if self.activeStep == 2:
            self.roadMapStatusLabel2 = "Empty"
        if self.activeStep == 3:
            self.roadMapStatusLabel3 = "Empty"
        if self.activeStep == 4:
            self.roadMapStatusLabel4 = "Empty"
        if self.activeStep == 5:
            self.roadMapStatusLabel5 = "Empty"
        if self.activeStep > 1:
            self.activeStep -= 1

    def create_crossword(self):
        print(self.title)
        print(self.description)
        print(self.rows)
        print(self.cols)

    def createGrid(self):
        print("Create grid called")
        gridRow = []
        self.grid = []
        print(type(self.rows))
        print(type(self.cols))

        # if self.rows == '':
        #     self.message_content = "Please enter a number of rows"
        #     self.message_type = "errorMessage"
        #     self.displayMessage = "yes"
        #     return
        #
        # if self.cols == '':
        #     self.message_content = "Please enter a number of columns"
        #     self.message_type = "errorMessage"
        #     self.displayMessage = "yes"
        #     return

        if not self.rows.isnumeric():
            self.message_content = "Number of rows must be an integer"
            self.message_type = "errorMessage"
            self.displayMessage = "yes"
            return
        if not self.cols.isnumeric():
            self.message_content = "Number of columns must ba an integer"
            self.message_type = "errorMessage"
            self.displayMessage = "yes"
            return

        if type(self.rows) != int:
            print("rows is not an int")
            rowsInt = int(self.rows)
            print("number of rows is: " + str(rowsInt))
            if rowsInt<3:
                self.message_content = "Number of rows must be greater than 3"
                self.message_type = "errorMessage"
                self.displayMessage = "yes"
                return
            if rowsInt>12:
                self.message_content = "Number of rows must be less than 12"
                self.message_type = "errorMessage"
                self.displayMessage = "yes"
                return

        if type(self.cols) != int:
            colsInt = int(self.cols)
            print("number of cols is: " + str(colsInt))
            if colsInt<3:
                self.message_content = "Number of columns must be greater than 3"
                self.message_type = "errorMessage"
                self.displayMessage = "yes"
                return
            if colsInt>12:
                self.message_content = "Number of columns must be less than 12"
                self.message_type = "errorMessage"
                self.displayMessage = "yes"
                return

        rowsInt = int(self.rows)
        colsInt = int(self.cols)
        print(type(self.rows))
        print(type(self.cols))


        for i in range(0, rowsInt):
            for j in range(0, colsInt):
                gridRow.append('_')
            self.grid.append(gridRow)
            gridRow = []
        print(self.grid)

        self.incrementStep()

    def cellClicked(self, cell):
        rowIndex, colIndex = cell[0], cell[1]
        print("Cell clicked at: ", rowIndex, colIndex)
        self.grid[rowIndex][colIndex] = self.activeChar

    def setActiveChar(self, clickChar):
        print("Active char: ", clickChar)
        self.activeChar = clickChar
        print("Active char: ", self.activeChar)

    def getWordVerticalHelper(self, start):
        print("Get word vertical helper called")
        print("Start: ", start)
        word = ""
        for i in range(start[0], int(self.rows)):
            if self.grid[i][start[1]] != '_':
                word += self.grid[i][start[1]]
            else:
                break
        return word

    def getWordHorizontalHelper(self, start):
        print("Get word horizontal helper called")
        print("Start: ", start)
        word = ""
        for i in range(start[1], int(self.cols)):
            if self.grid[start[0]][i] != '_':
                word += self.grid[start[0]][i]
            else:
                break
        return word

    def getWordOrient(self):
        self.wordsHorizontalStart = []
        self.wordsVerticalStart = []
        self.wordsHorizontal = []
        self.wordsVertical = []
        rowsInt = int(self.rows)
        colsInt = int(self.cols)
        for i in range(0, int(self.rows)):
            for j in range(0, int(self.cols)):
                if self.grid[i][j] != '_':
                    if i == 0 and j == 0:
                        if self.grid[i][j + 1] != '_':
                            self.wordsHorizontalStart.append([i, j])
                        if self.grid[i + 1][j] != '_':
                            self.wordsVerticalStart.append([i, j])
                    elif i == 0:
                        if j-1 >=0 and self.grid[i][j - 1] == '_' and j+1<colsInt and self.grid[i][j + 1] != '_':
                            self.wordsHorizontalStart.append([i, j])
                        if self.grid[i + 1][j] != '_':
                            self.wordsVerticalStart.append([i, j])
                    elif j == 0:
                        if i-1>=0 and self.grid[i - 1][j] == '_' and i+1 < rowsInt and self.grid[i + 1][j] != '_':
                            self.wordsVerticalStart.append([i, j])
                        if self.grid[i][j + 1] != '_':
                            self.wordsHorizontalStart.append([i, j])
                    else:
                        if j-1>=0 and self.grid[i][j - 1] == '_' and j+1<colsInt and self.grid[i][j + 1] != '_':
                            self.wordsHorizontalStart.append([i, j])
                        if i-1>=0 and self.grid[i - 1][j] == '_' and i+1<rowsInt and self.grid[i + 1][j] != '_':
                            self.wordsVerticalStart.append([i, j])
        print("Horizontal: ", self.wordsHorizontalStart)
        print("Vertical: ", self.wordsVerticalStart)

        for i in range(0, len(self.wordsHorizontalStart)):
            self.wordsHorizontal.append(self.getWordHorizontalHelper(self.wordsHorizontalStart[i]))

        for i in range(0, len(self.wordsVerticalStart)):
            self.wordsVertical.append(self.getWordVerticalHelper(self.wordsVerticalStart[i]))

        print("Horizontal: ", self.wordsHorizontal)
        print("Vertical: ", self.wordsVertical)

        for i in range(rowsInt):
            for j in range(colsInt):
                if self.grid[i][j] != '_':
                    hasAdjacent= False
                    if i+1<rowsInt:
                        if self.grid[i+1][j]!='_':
                            hasAdjacent = True
                    if i-1>=0:
                        if self.grid[i-1][j]!='_':
                            hasAdjacent = True
                    if j+1<colsInt:
                        if self.grid[i][j+1]!='_':
                            hasAdjacent = True
                    if j-1>=0:
                        if self.grid[i][j-1]!='_':
                            hasAdjacent = True

                    if hasAdjacent == False:
                        self.message_content = f"Cell {i+1}, {j+1} is not adjacent to any other cell"
                        self.message_type = "errorMessage"
                        self.displayMessage = "yes"
                        return

        if self.wordsHorizontal == [] and self.wordsVertical == []:
            self.message_content = "At least two cells must be adjacent"
            self.message_type = "errorMessage"
            self.displayMessage = "yes"
            return

        self.incrementStep()

    def getClues(self):

        if self.verClue1 != "":
            self.verClues['0'] = self.verClue1
        if self.verClue2 != "":
            self.verClues['1'] = self.verClue2
        if self.verClue3 != "":
            self.verClues['2'] = self.verClue3
        if self.verClue4 != "":
            self.verClues['3'] = self.verClue4
        if self.verClue5 != "":
            self.verClues['4'] = self.verClue5

        if self.horClue1 != "":
            self.horClues['0'] = self.horClue1
        if self.horClue2 != "":
            self.horClues['1'] = self.horClue2
        if self.horClue3 != "":
            self.horClues['2'] = self.horClue3
        if self.horClue4 != "":
            self.horClues['3'] = self.horClue4
        if self.horClue5 != "":
            self.horClues['3'] = self.horClue5

        self.verClues = dict(sorted(self.verClues.items()))
        self.horClues = dict(sorted(self.horClues.items()))


        print("Username in get clues: ", self.username)
        print("Get clues called")
        print("Title: ", self.title)
        print("Description: ", self.description)
        print("Rows: ", self.rows)
        print("Columns: ", self.cols)
        print("Grid: ", self.grid)
        print("Words horizontal: ", self.wordsHorizontal)
        print("Words vertical: ", self.wordsVertical)
        print("Words horizontal start: ", self.wordsHorizontalStart)
        print("Words vertical start: ", self.wordsVerticalStart)
        print("Vertical clues: ", self.verClues)
        print("Horizontal clues: ", self.horClues)
        newCrossword = Crossword(self.username, self.title, self.description, int(self.rows), int(self.cols), self.verClues,self.horClues, self.wordsHorizontal, self.wordsVertical, self.grid, self.wordsHorizontalStart, self.wordsVerticalStart)
        print("New crossword: ", newCrossword)

        if newCrossword.check():
            collections.insert_one(newCrossword.__dict__)
            self.message_content = "Crossword saved successfully"
            self.message_type = "successMessage"
            self.displayMessage = "yes"
            self.incrementStep()
        else:
            self.message_content = newCrossword.message
            self.message_type = "errorMessage"
            self.displayMessage = "yes"

    def hideMessage(self):
        print("hide message called")
        self.displayMessage = "no"

    def goHome(self):
        print("go home called")
        return redirect("/home")

    def createAnother(self):
        print("create another called")
        return redirect("/create_crossword_manual/")