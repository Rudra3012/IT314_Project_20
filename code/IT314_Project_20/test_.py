import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IT314_Project_20.settings')


from crosswordApp.views import *

from crosswordApp.Classes.Crossword import Crossword


def test1():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N", "A", "I", "L", "_"],
            ["_", "_", "R", "_", "_"],
            ["_", "_", "O", "_", "_"],
            ["_", "_", "N", "_", "_"],
            ["_", "_", "_", "_", "_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0, 0)]
    AnswersVerStart = [(0, 2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]

    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid,
                   AnswersHorStart, AnswersVerStart)

    assert c1.check() == True

