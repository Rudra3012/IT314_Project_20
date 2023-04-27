import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IT314_Project_20.settings')
django.setup()


from crosswordApp.views import *

from crosswordApp.Classes.Crossword import Crossword

#test case 1 - user has given correct answers in the correct boxes
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

#test case 2 - user has given correct answers in the correct boxes
def test2():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 4
    height = 5
    grid = [["_", "_", "_", "T"],
            ["_", "C", "_", "R"],
            ["C", "A", "K", "E"],
            ["_", "R", "_", "E"],
            ["_", "_", "_", "_"]]
    AnswersHor = ["CAKE"]
    AnswersVer = ["CAR", "TREE"]
    AnswersHorStart = [(2, 0)]
    AnswersVerStart = [(1, 1), (0, 3)]
    cluesHor = ["A dessert"]
    cluesVer = ["vehicle", "a big plant"]

    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid,
                   AnswersHorStart, AnswersVerStart)

    assert c1.check() == True

#test case 3 - user has given correct answers in the correct boxes
def test3():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["_", "S", "I", "L", "K"],
            ["_", "O", "_", "_", "_"],
            ["P", "A", "I", "N", "T"],
            ["_", "P", "_", "_", "_"],
            ["_", "_", "_", "_", "_"]]
    AnswersHor = ["SILK", "PAINT"]
    AnswersVer = ["SOAP"]
    AnswersHorStart = [(0, 1), (2, 0)]
    AnswersVerStart = [(0, 1)]
    cluesHor = ["a smooth cloth", "art"]
    cluesVer = ["a cleanser"]

    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid,
                   AnswersHorStart, AnswersVerStart)

    assert c1.check() == True

#test case 4 - user has given incorrect answers
def test4():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["C", "L", "O", "C", "K"],
            ["H", "_", "V", "_", "_"],
            ["A", "_", "E", "_", "_"],
            ["I", "_", "N", "_", "_"],
            ["R", "_", "_", "_", "_"]]
    AnswersHor = ["WATCH"]
    AnswersVer = ["CHAIR", "TOOL"]
    AnswersHorStart = [(0, 0)]
    AnswersVerStart = [(0, 0,), (0, 1)  ]
    cluesHor = ["tells the time"]
    cluesVer = ["sitting", "baking"]

    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid,
                   AnswersHorStart, AnswersVerStart)

    assert c1.check() == False

#test case 5 - user has put input in the wrong box with wrong answers
def test5():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 6
    grid = [["M", "A", "P", "_", "_"],
            ["_", "_", "_", "I", "_"],
            ["_", "_", "_", "L", "_"],
            ["_", "B", "E", "L", "L"],
            ["_", "A", "_", "O", "_"],
            ["_", "T", "_", "W", "_"]]
    AnswersHor = ["MAP", "RIN"]
    AnswersVer = ["PILLOW", "BAL"]
    AnswersHorStart = [(0, 0), (3, 1)]
    AnswersVerStart = [(0, 2), (3, 1)]
    cluesHor = ["Navigation", "chimes in a tower"]
    cluesVer = ["cricket", "cushion"]

    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid,
                   AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


#test case 6 - user has given an incorrect input/ incorrect answer
def test6():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 6
    height = 6
    grid = [["_", "G", "_", "_", "_", "_"],
            ["_", "U", "_", "_", "_", "_"],
            ["_", "I", "N", "K", "_", "_"],
            ["_", "T", "_", "_", "_", "_"],
            ["C", "A", "L", "L", "_", "_"],
            ["_", "R", "_", "_", "_", "_"]]
    AnswersHor = ["INK", "CALL"]
    AnswersVer = ["ABCDAB"]
    AnswersHorStart = [(2, 1), (4, 0)]
    AnswersVerStart = [(0, 1)]
    cluesHor = ["Pen refill", "a phone"]
    cluesVer = ["a string instrument"]

    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid,
                   AnswersHorStart, AnswersVerStart)

    assert c1.check() == False

#test case 7 - user has not completed the puzzle
def test7():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 6
    height = 6
    grid = [["_", "P", "_", "_", "_", "_"],
            ["_", "E", "_", "_", "_", "_"],
            ["_", "N", "_", "P", "_", ""],
            ["_", "C", "E", "L", "L", "S"],
            ["_", "I", "_", "O", "_", "I"],
            ["_", "L", "_", "T", "_", "T"]]
    AnswersHor = ["CELLS"]
    AnswersVer = ["PENCIL"]
    AnswersHorStart = [(2, 1), (4, 0)]
    AnswersVerStart = [(0, 1), (2, 3)]
    cluesHor = ["Pen refill", "a phone"]
    cluesVer = ["writing", "screenplay", "not standing"]

    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid,
                   AnswersHorStart, AnswersVerStart)

    assert c1.check() == False

#test case 8 - user has not completed the puzzle
def test8():
    title = "Test"
    description = "Test"
    creator = "Test"

    width = 5
    height = 5
    grid = [["_", "M", "I", "L", "K"],
            ["_", "E", "_", "_", "_"],
            ["_", "T", "_", "_", "_"],
            ["_", "A", "_", "_", "_"],
            ["_", "L", "_", "_", "_"]]
    AnswersHor = ["MILK"]
    AnswersVer = []
    AnswersHorStart = [(0, 1)]
    AnswersVerStart = []
    cluesHor = ["cereal and "]
    cluesVer = ["iron, copper, brass"]

    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid,
                   AnswersHorStart, AnswersVerStart)

    assert c1.check() == False
    
def test4():
        
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 15
    height = 5
    grid = [["N","A","I","L","_","_","_","_","_","_","_","_","_","_","_"],
              ["_","_","R","_","_","_","_","_","_","_","_","_","_","_","_"],
              ["_","_","O","_","_","_","_","_","_","_","_","_","_","_","_"],
              ["_","_","N","_","_","_","_","_","_","_","_","_","_","_","_"],
              ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
    assert c1.check() == True

# for 1 size word : expected output false

def test51():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"]]
    wordsUp = ["N"]
    wordsDown = ["N"]
    AnswersHor = ["N"]
    AnswersVer = ["N"]
    AnswersHorStart = [(0, 0)]
    AnswersVerStart = [(0, 0)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


def test52():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "A"]]
    wordsUp = ["A"]
    wordsDown = ["A"]
    AnswersHor = ["A"]
    AnswersVer = ["A"]
    AnswersHorStart = [(4, 4)]
    AnswersVerStart = [(4, 4)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


def test53():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["_", "_", "W", "_", "_"],
            ["A", "_", "O", "_", "_"],
            ["_", "_", "R", "_", "_"],
            ["_", "_", "D", "_", "_"],
            ["_", "_", "_", "_", "_"]]
    wordsUp = ["A"]
    wordsDown = ["WORD"]
    AnswersHor = ["A"]
    AnswersVer = ["WORD"]
    AnswersHorStart = [(1, 0)]
    AnswersVerStart = [(0, 2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False