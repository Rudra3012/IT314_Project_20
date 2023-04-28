from django.shortcuts import redirect
from django_unicorn.components import UnicornView
import CrosswordGenerator as cg
from crosswordApp.Classes.Crossword import Crossword, gridCell
from pymongo import MongoClient

client = MongoClient("mongodb+srv://Group20:Group20@cluster0.vl47pk0.mongodb.net/?retryWrites=true&w=majority")
db = client['CrossWordManagement']

class CreatecrosswordautoView(UnicornView):
    title: str = ""
    description: str = ""
    step: int = 1
    word: str = ""
    clue: str = ""
    wordsInserted: int = 0
    clues_and_words = []
    canSave: bool = False
    crossword_grid = []
    wordsHorizontalStart = []
    wordsVerticalStart = []
    wordsHorizontal = []
    wordsVertical = []
    verClues = {}
    horClues = {}
    wordCluesMap = {}
    rows: int = 0
    columns: int = 0
    username = "None"
    message_content: str = ""
    message_type = ""
    displayMessage: str = "no"

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        username = kwargs.get("username")

    def previousStep(self):
        if self.step  > 1:
            self.step -= 1

    def nextStep(self):

        if self.step == 1:
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

        self.step += 1

    def add_clue_and_word(self):
        print(f'add clue and word: {self.clue} {self.word}')

        if self.word == "":
            self.message_content = "Please enter a word"
            self.message_type = "errorMessage"
            self.displayMessage = "yes"
            return
        if self.clue == "":
            self.message_content = "Please enter a clue"
            self.message_type = "errorMessage"
            self.displayMessage = "yes"
            return

        if len(self.word) > 15:
            self.message_content = "Word is too long"
            self.message_type = "errorMessage"
            self.displayMessage = "yes"
            return

        if len(self.clue) > 50:
            self.message_content = "Clue is too long"
            self.message_type = "errorMessage"
            self.displayMessage = "yes"
            return

        self.clues_and_words.append((self.clue, self.word))
        self.wordsInserted += 1
        self.word = ""
        self.clue = ""

    def generate(self):
        print("Generate crossword")
        print("Title: " + self.title)
        print("Description: " + self.description)
        print("Words and clues: " + str(self.clues_and_words))

        words = [word for clue, word in self.clues_and_words]

        grid = cg.generate_crossword(words)

        print(grid)
        row = []
        self.crossword_grid = []
        for i in range(len(grid)):
            if grid[i] != '\n':
                row.append(grid[i])
            else:
                self.crossword_grid.append(row)
                row = []

        for i in range(len(self.crossword_grid)):
            for j in range(len(self.crossword_grid[i])):
                if self.crossword_grid[i][j] == '-':
                    self.crossword_grid[i][j] = '_'

        print(self.crossword_grid)
        self.rows = len(self.crossword_grid)
        self.columns = len(self.crossword_grid[0])

        self.canSave = True

    def getWordVerticalHelper(self, start):
        print("Get word vertical helper called")
        print("Start: ", start)
        word = ""
        for i in range(start[0], self.rows):
            if self.crossword_grid[i][start[1]] != '_':
                word += self.crossword_grid[i][start[1]]
            else:
                break
        return word

    def getWordHorizontalHelper(self, start):
        print("Get word horizontal helper called")
        print("Start: ", start)
        word = ""
        for i in range(start[1], self.columns):
            if self.crossword_grid[start[0]][i] != '_':
                word += self.crossword_grid[start[0]][i]
            else:
                break
        return word

    def getWordOrient(self):
        self.wordsHorizontalStart = []
        self.wordsVerticalStart = []
        self.wordsHorizontal = []
        self.wordsVertical = []

        for i in range(0, self.rows):
            for j in range(0, self.columns):
                if self.crossword_grid[i][j] != '_':
                    if i == 0 and j == 0:
                        if self.crossword_grid[i][j + 1] != '_':
                            self.wordsHorizontalStart.append([i, j])
                        if self.crossword_grid[i + 1][j] != '_':
                            self.wordsVerticalStart.append([i, j])
                    elif i == 0:
                        if j+1>=0 and self.crossword_grid[i][j - 1] == '_' and j+1<self.columns and self.crossword_grid[i][j + 1] != '_':
                            self.wordsHorizontalStart.append([i, j])
                        if self.crossword_grid[i + 1][j] != '_':
                            self.wordsVerticalStart.append([i, j])
                    elif j == 0:
                        if i-1>=0 and self.crossword_grid[i - 1][j] == '_' and i+1<self.rows and self.crossword_grid[i + 1][j] != '_':
                            self.wordsVerticalStart.append([i, j])
                        if self.crossword_grid[i][j + 1] != '_':
                            self.wordsHorizontalStart.append([i, j])
                    else:
                        print("i: ", i, " j: ", j)
                        if self.crossword_grid[i][j - 1] == '_' and j+1< self.columns and self.crossword_grid[i][j + 1] != '_':
                            self.wordsHorizontalStart.append([i, j])
                        if self.crossword_grid[i - 1][j] == '_' and i+1< self.rows and self.crossword_grid[i + 1][j] != '_':
                            self.wordsVerticalStart.append([i, j])
        # print("Horizontal: ", self.wordsHorizontalStart)
        # print("Vertical: ", self.wordsVerticalStart)

        for i in range(0, len(self.wordsHorizontalStart)):
            self.wordsHorizontal.append(self.getWordHorizontalHelper(self.wordsHorizontalStart[i]))

        for i in range(0, len(self.wordsVerticalStart)):
            self.wordsVertical.append(self.getWordVerticalHelper(self.wordsVerticalStart[i]))

        print("Horizontal: ", self.wordsHorizontal)
        print("Vertical: ", self.wordsVertical)


    def save_crossword(self):
        print("Save crossword")
        print("Title: " + self.title)
        print("Description: " + self.description)
        print("Words and clues: " + str(self.clues_and_words))
        print("Crossword grid: " + str(self.crossword_grid))
        grid_dict = {}
        gridList = []
        crosswordStr = ""
        words = [word for clue, word in self.clues_and_words]
        for i in range(len(self.crossword_grid)):
            for j in range(len(self.crossword_grid[i])):
                grid_dict[(i, j)] = self.crossword_grid[i][j]
                crosswordStr += self.crossword_grid[i][j]
                gridList.append(gridCell(i, j, self.crossword_grid[i][j]).__dict__)
            crosswordStr += '\n'
        print(words)
        print(crosswordStr)
        wordsHor, wordsVer = cg.getWordOrient(crosswordStr, words)
        print(f'wordsHor: {wordsHor}')
        print(f'wordsVer: {wordsVer}')
        collections = db['crosswordApp_crossword']

        self.getWordOrient()

        for i in range(len(self.clues_and_words)):
            # print(self.clues_and_words[i][1].upper())
            self.wordCluesMap[self.clues_and_words[i][1].upper()] = self.clues_and_words[i][0]

        verClues= {}
        horClues = {}

        print("wordCluesMap: ", self.wordCluesMap)

        print(self.wordCluesMap)

        for i in range(len(self.wordsHorizontal)):
            horClues[str(i)] = self.wordCluesMap[self.wordsHorizontal[i].upper()]

        for i in range(len(self.wordsVertical)):
            verClues[str(i)] = self.wordCluesMap[self.wordsVertical[i]]

        verClues = dict(sorted(verClues.items()))
        horClues = dict(sorted(horClues.items()))

        print("wordCluesMap: ", self.wordCluesMap)
        print("title: " + self.title)
        print("description: " + self.description)
        print("Rows: " + str(self.rows))
        print("Columns: " + str(self.columns))
        print("grid: " + str(self.crossword_grid    ))
        print("Horizontal Clues: " + str(verClues))
        print("Vertical Clues: " + str(horClues))

        print("WordsHorizontal: " + str(self.wordsHorizontal))
        print("WordsVertical: " + str(self.wordsVertical))
        print("WordsHorizontalStart: " + str(self.wordsHorizontalStart))
        print("WordsVerticalStart: " + str(self.wordsVerticalStart))
        print("username: " + self.username)

        # newCrossword = Crossword(title=self.title, description=self.description, width=len(self.crossword_grid[0]),
        #                          height=len(self.crossword_grid), cluesUp=[], cluesDown=[], WordsUp=wordsVer,
        #                          WordsDown=wordsHor, gridList=gridList)
        # print(newCrossword.__dict__)
        # collections.insert_one(newCrossword.__dict__)

        newCrossword = Crossword(self.username, self.title, self.description, self.columns, self.rows, verClues,horClues, self.wordsHorizontal, self.wordsVertical, self.crossword_grid, self.wordsHorizontalStart, self.wordsVerticalStart)
        print("New crossword: ", newCrossword)
        collections.insert_one(newCrossword.__dict__)

        self.displayMessage = "yes"
        self.message_type = "successMessage"
        self.message_content = "Crossword saved successfully!"
        self.step = 3
        # Title: sample
        # Description: sample1
        # Rows: 10
        # Columns: 10
        # Grid: [['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        #        ['_', 'S', 'O', 'F', 'T', 'W', 'A', 'R', 'E', '_'], ['_', '_', '_', '_', 'E', '_', '_', '_', 'R', '_'],
        #        ['_', '_', '_', '_', 'S', '_', '_', '_', 'R', '_'], ['_', '_', '_', '_', 'T', '_', '_', '_', 'O', '_'],
        #        ['_', '_', '_', '_', 'I', '_', '_', '_', 'R', '_'], ['_', '_', '_', '_', 'N', '_', '_', '_', '_', '_'],
        #        ['_', '_', '_', '_', 'G', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]
        # Words
        # horizontal: ['SOFTWARE']
        # Words
        # vertical: ['TESTING', 'ERROR']
        # Words
        # horizontal
        # start: [[2, 1]]
        # Words
        # vertical
        # start: [[2, 4], [2, 8]]
        # Vertical
        # clues: {'0': 'How do you detect errors', '1': 'Mistakes in code output'}
        # Horizontal
        # clues: {'0': 'First Name of Course'}
        # New
        # crossword: Crossword: sample

    def hideMessage(self):
        print("hide message called")
        self.displayMessage = "no"

    def goHome(self):
        print("go home called")
        return redirect("/home")

    def createAnother(self):
        print("create another called")
        return redirect("/create_crossword_automatic/")