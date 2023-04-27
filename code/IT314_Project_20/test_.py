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
    grid = [["", "", "_", "T"],
            ["", "C", "", "R"],
            ["C", "A", "K", "E"],
            ["", "R", "", "E"],
            ["", "", "", ""]]
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
            ["", "O", "", "", ""],
            ["P", "A", "I", "N", "T"],
            ["", "P", "", "", ""],
            ["", "", "", "", "_"]]
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
            ["H", "", "V", "", "_"],
            ["A", "", "E", "", "_"],
            ["I", "", "N", "", "_"],
            ["R", "", "", "", "_"]]
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
    grid = [["M", "A", "P", "", ""],
            ["", "", "", "I", ""],
            ["", "", "", "L", ""],
            ["_", "B", "E", "L", "L"],
            ["", "A", "", "O", "_"],
            ["", "T", "", "W", "_"]]
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
    grid = [["", "G", "", "", "", "_"],
            ["", "U", "", "", "", "_"],
            ["", "I", "N", "K", "", "_"],
            ["", "T", "", "", "", "_"],
            ["C", "A", "L", "L", "", ""],
            ["", "R", "", "", "", "_"]]
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
    grid = [["", "P", "", "", "", "_"],
            ["", "E", "", "", "", "_"],
            ["", "N", "", "P", "", ""],
            ["_", "C", "E", "L", "L", "S"],
            ["", "I", "", "O", "_", "I"],
            ["", "L", "", "T", "_", "T"]]
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
            ["", "E", "", "", ""],
            ["", "T", "", "", ""],
            ["", "A", "", "", ""],
            ["", "L", "", "", ""]]
    AnswersHor = ["MILK"]
    AnswersVer = []
    AnswersHorStart = [(0, 1)]
    AnswersVerStart = []
    cluesHor = ["cereal and "]
    cluesVer = ["iron, copper, brass"]

    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid,
                   AnswersHorStart, AnswersVerStart)

    assert c1.check() == False