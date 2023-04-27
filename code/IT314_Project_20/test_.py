import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IT314_Project_20.settings')
django.setup()


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

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == True


def test2():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 0
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

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


def test3():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = -1
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

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


# Output : False

def test4():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 15
    height = 5
    grid = [["N", "A", "I", "L", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "R", "_", "_", "_", "_", "_","_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "O", "_", "_", "_", "_", "_","_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "N", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0, 0)]
    AnswersVerStart = [(0, 2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == True


# Output : True

def test5():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 16
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

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


# Output : False

def test6():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 1.5
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

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


# Output : False


def test7():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = "abc"
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

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


# Output : False

def test8():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 0
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

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


# Output : False


def test9():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = -1
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

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


# Output : False


def test10():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 15
    grid = [["N", "A", "I", "L", "_"],
            ["_", "_", "R", "_", "_"],
            ["_", "_", "O", "_", "_"],
            ["_", "_", "N", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"],
            ["_", "_", "_", "_", "_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0, 0)]
    AnswersVerStart = [(0, 2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == True

# Output : True


def test11():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 16
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

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


# Output : False

def test12():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 1.5
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

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


# Output : False


def test13():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = "abc"
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

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


# Output : False

def test14():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 3
    height = 5
    grid = [["A", "S", "K"],
            ["_", "A", "_"],
            ["_", "N", "_"],
            ["_", "D", "_"],
            ["_", "_", "_"]]
    wordsUp = ["SAND"]
    wordsDown = ["ASK"]
    AnswersHor = ["ASK"]
    AnswersVer = ["SAND"]
    AnswersHorStart = [(0, 0)]
    AnswersVerStart = [(0, 1)]
    cluesHor = ["Questioning"]
    cluesVer = ["Part of earth "]

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == True


# Output : True

def test15():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 3
    grid = [["S", "A", "N", "D", "_"],
            ["_", "S", "_", "_", "_"],
            ["_", "K", "_", "_", "_"]]

    wordsUp = ["ASK"]
    wordsDown = ["SAND"]
    AnswersHor = ["SAND"]
    AnswersVer = ["ASK"]
    AnswersHorStart = [(0, 0)]
    AnswersVerStart = [(0, 1)]
    cluesHor = ["Part of Earth"]
    cluesVer = ["Questioning "]

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == True


# Output : True

def test16():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 2
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

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


# Output : False

def test17():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 3
    height = 2
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

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


# Output : False

def test18():
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
    cluesHor = []
    cluesVer = ["an element"]

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


# Output : False

def test19():
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
    cluesVer = []

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


# Output : False

def test20():
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

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == True

# Output : False


def test21():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N", "A", "I", "L"],
            ["_", "_", "R", "_"],
            ["_", "_", "O", "_"],
            ["_", "_", "N", "_"],
            ["_", "_", "_", "_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0, 0)]
    AnswersVerStart = [(0, 2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


# Output : False

def test22():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N", "A", "I", "L", "_"],
            ["_", "_", "R", "_", "_"],
            ["_", "_", "O", "_", "_"],
            ["_", "_", "N", "_", "_"]],

    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0, 0)]
    AnswersVerStart = [(0, 2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False


# Output : False

def test23():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N", "A", "I", "L"],
            ["_", "_", "R", "_"],
            ["_", "_", "O", "_"],
            ["_", "_", "N", "_"]],

    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0, 0)]
    AnswersVerStart = [(0, 2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]

    c1 = Crossword(creator, title, description, width, height, cluesVer,
                   cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)

    assert c1.check() == False

# new added
def test24():                              
    title = ""
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
        
    assert c1.check() == False

# Output : False


def test25():
    title = "dd%uvJsMq=@kgxwWHM%HEF2s)M VL290!f#rLbryppHnps3yZb"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
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
# Output : True


def test26():
    title = "dd%uvJsMq=@kgxwWHM%HEF2s)M VL290!f#rLbryppHnps3yZba"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
        
    assert c1.check() == False


# Output : False

def test27():
    title = "Test"
    description = ""
    creator = "Test"
    width = 5
    height = 5
    grid = [["N","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
        
    assert c1.check() == False


# Output : False

def test28():
    title = "Test"
    description = "rovG9k/#Hv9wmL2tr+u#lisX(!toTQMotbQDJ2l^_WH#Nd@a_&prZE9^hqGbuk+f(yBxN=7y@p@UoJ=vULKXU&C%Zqw@f0CO5yowSgIvNsb9Nz3R^jPZMhqLm8NG)dvjRkALGYhK)+EFYCIF9Ub+&NTI#(^W*)ph+Z$u%)K+ NX+d!ptf59tv9Wcl5OBtw1!KD NALpWeT@m&6wkhV)kpbby2R#8_ip1kEa#rO4!-w2%Dv8CDD5I5u&Bx0%4&%ZN&AAi#pP_uw4_xD*pBeps Ea)lpCE-n!gh7)BLA9M&vAbGsC7P5e@y)N3qRdBv-^ZvhcxX4FrFb0pgMDJfGV08oPPOqz=/F4giS9Dg(9 v)M A&b!K@WTmmUJiKxc_Q1y1=T(sBR-H#J+Ll_8d-hEsC%a8I7(kYsvl(d&^s!GAk0qHF@4gFG8uT7^DI7hnoofnZdl5Gz@Z%u23oN)$-65+B-oBa1k97lW!o$o)9XrP5HrcqvEyPOf"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
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
# Output : True


def test29():
    title = "Test"
    description = "rovG9k/#Hv9wmL2tr+u#lisX(!toTQMotbQDJ2l^_WH#Nd@a_&prZE9^hqGbuk+f(yBxN=7y@p@UoJ=vULKXU&C%Zqw@f0CO5yowSgIvNsb9Nz3R^jPZMhqLm8NG)dvjRkALGYhK)+EFYCIF9Ub+&NTI#(^W*)ph+Z$u%)K+ NX+d!ptf59tv9Wcl5OBtw1!KD NALpWeT@m&6wkhV)kpbby2R#8_ip1kEa#rO4!-w2%Dv8CDD5I5u&Bx0%4&%ZN&AAi#pP_uw4_xD*pBeps Ea)lpCE-n!gh7)BLA9M&vAbGsC7P5e@y)N3qRdBv-^ZvhcxX4FrFb0pgMDJfGV08oPPOqz=/F4giS9Dg(9 v)M A&b!K@WTmmUJiKxc_Q1y1=T(sBR-H#J+Ll_8d-hEsC%a8I7(kYsvl(d&^s!GAk0qHF@4gFG8uT7^DI7hnoofnZdl5Gz@Z%u23oN)$-65+B-oBa1k97lW!o$o)9XrP5HrcqvEyPOfa"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
        
    assert c1.check() == False


# Output : False


def test30():
    title = "Test"
    description = "Test"
    creator = ""
    width = 5
    height = 5
    grid = [["N","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
        
    assert c1.check() == False


# Output : False

def test31():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = []
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
        
    assert c1.check() == False


# Output : False


def test32():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = []
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
        
    assert c1.check() == False


# Output : false


def test33():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["FROG"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
        
    assert c1.check() == False
# Output : False


def test34():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["FROG"]
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
        
    assert c1.check() == False

# Output : False


def test35():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["IROG"]
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
        
    assert c1.check() == False

# Output : False


def test36():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["ZAIL"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
        
    assert c1.check() == False

# Output : False


def test37():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIZ"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
        
    assert c1.check() == False

# Output : False


def test38():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAQL"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
        
    assert c1.check() == False

# Output : False


def test39():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["QRON"]
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
        
    assert c1.check() == False

# Output : False


def test40():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["&","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
        
    assert c1.check() == False


# Output : False



def test41():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["N","5","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
        
    assert c1.check() == False


# Output : False



def test42():
    title = "Test"
    description = "Test"
    creator = "Test"
    width = 5
    height = 5
    grid = [["n","A","I","L","_"],
              ["_","_","R","_","_"],
              ["_","_","O","_","_"],
              ["_","_","N","_","_"],
              ["_","_","_","_","_"]]
    wordsUp = ["IRON"]
    wordsDown = ["NAIL"]
    AnswersHor = ["NAIL"]
    AnswersVer = ["IRON"]
    AnswersHorStart = [(0,0)]
    AnswersVerStart = [(0,2)]
    cluesHor = ["a body part"]
    cluesVer = ["an element "]
    
    c1 = Crossword(creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, grid, AnswersHorStart, AnswersVerStart)
        
    assert c1.check() == False


# Output : False
# 
#test case 43 - user has given correct answers in the correct boxes
def test43():
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

#test case 44 - user has given correct answers in the correct boxes
def test44():
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

#test case 45 - user has given correct answers in the correct boxes
def test45():
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

#test case 46 - user has given incorrect answers
def test46():
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

#test case 47 - user has put input in the wrong box with wrong answers
def test47():
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


#test case 48 - user has given an incorrect input/ incorrect answer
def test48():
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

#test case 49 - user has not completed the puzzle
def test49():
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

#test case 50 - user has not completed the puzzle
def test50():
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