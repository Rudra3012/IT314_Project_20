from django_unicorn.components import UnicornView
import CrosswordGenerator as cg
from crosswordApp.Classes.Crossword import Crossword, gridCell
from pymongo import MongoClient
import json

client = MongoClient('mongodb+srv://Group20:Group20@cluster0.fi05hgc.mongodb.net/test')
db = client['CrossWordManagement']


class CreateCrosswordView(UnicornView):
    title: str = ""
    description: str = ""
    word: str = ""
    clue: str = ""
    clues_and_words = []
    crossword_grid = []

    def add_clue_and_word(self):
        print(f'add clue and word: {self.clue} {self.word}')
        self.clues_and_words.append((self.clue, self.word))
        self.word = ""
        self.clue = ""

    def reset_page(self):
        self.title = ""
        self.description = ""
        self.word = ""
        self.clue = ""
        self.clues_and_words = []
        self.crossword_grid = []

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

        print(self.crossword_grid)

    def save_crossword(self):
        # print("Save crossword")
        # print("Title: " + self.title)
        # print("Description: " + self.description)
        # print("Words and clues: " + str(self.clues_and_words))
        # print("Crossword grid: " + str(self.crossword_grid))
        grid_dict = {}
        gridList = []
        crosswordStr = ""
        words = [word.upper() for clue, word in self.clues_and_words]
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
        newCrossword = Crossword(title=self.title, description=self.description, width=len(self.crossword_grid[0]),
                                 height=len(self.crossword_grid), cluesUp=[], cluesDown=[], WordsUp=wordsVer,
                                 WordsDown=wordsHor, gridList=gridList)
        print(newCrossword.__dict__)
        collections.insert_one(newCrossword.__dict__)
