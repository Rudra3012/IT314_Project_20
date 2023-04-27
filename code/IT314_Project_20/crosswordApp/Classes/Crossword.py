import datetime
import uuid


class gridCell:
    x: int
    y: int
    value: str

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value


class Crossword:

    creator: str
    title: str
    description: str
    width: int
    height: int
    AnswersHor = []
    AnswersVer = []
    cluesHor = []
    cluesVer = []
    AnswersHorStart = []
    AnswersVerStart = []
    timeOfCreation: str
    clueAnswers = {}
    grid = []
    timesRating: int
    rating: int
    timesSolved: int
    avgTime = 0
    message = ""
    def __init__(self, creator, title, description, width, height, cluesVer, cluesHor, AnswersHor, AnswersVer, gridList, AnswersHorStart, AnswersVerStart):

        self.creator = creator
        self.title = title
        self.description = description
        self.width = width
        self.height = height
        self.AnswersHor = AnswersHor
        self.AnswersVer = AnswersVer
        self.grid = gridList
        self.cluesHor = cluesHor
        self.cluesVer = cluesVer
        self.AnswersHorStart = AnswersHorStart
        self.AnswersVerStart = AnswersVerStart
        self.timeOfCreation = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.timesSolved = 0
        self.timesRating = 0
        self.rating = 0
        self.avgTime = 0

        
    def __str__(self):
        return f"Crossword: {self.title}"

    def check(self):
        
        print("Check function called")
        
        if self.creator == "":
            self.message = "Creator is empty"
            return False

        print("Creator is not empty")
        
        if self.title == "" or len(self.title) > 50:
            self.message = "Title is empty or too long"
            return False

        print("Title is not empty")
    
        if self.description == "" or len(self.description) > 300:
            self.message = "Description is empty or too long"
            return False

        print("Description is not empty")

        if self.AnswersHor == [] and self.AnswersVer == []:
            self.message = "Answers are empty"
            return False

        print("Answers are not empty")

        if self.width > 15 or type(self.width) != int:
            self.message = "Width is too long or not an integer"
            return False

        print("Width is not too long")

        if self.height > 15 or type(self.height) != int:
            self.message = "Height is too long or not an integer"
            return False

        print("Height is not too long")

        if self.cluesHor == {} and self.cluesVer == {}:
            self.message = "Clues are empty"
            return False

        print("Clues are not empty")

        if not self.grid:
            self.message = "Grid is empty"
            return False

        print("Grid is not empty")

        if len(self.grid) != self.height:
            print(len(self.grid))
            print(self.height)
            self.message = "Grid height is not equal to height"
            return False

        print("Grid height is equal to height")

        for i in range(len(self.grid)):
            if len(self.grid[i]) != self.width:
                self.message = "Grid width is not equal to width"
                return False

        print("Grid width is equal to width")

        if len(self.AnswersHor) != len(self.cluesHor):
            self.message = "Number of Horizontal answers is not equal to number of Horizontal clues"
            return False

        print("Number of Horizontal answers is equal to number of Horizontal clues")

        if len(self.AnswersVer) != len(self.cluesVer):
            self.message = "Number of Vertical answers is not equal to number of Vertical clues"
            return False

        print("Number of Vertical answers is equal to number of Vertical clues")

        for i in range(len(self.AnswersHor)):
            list1 = list(self.AnswersHorStart[i])
            x = list1[0]
            y = list1[1]
            for j in range(len(self.AnswersHor[i])):
                
                if self.grid[x][y+j] != self.AnswersHor[i][j]:
                    self.message = "Start of Horizontal word in grid is not correct"
                    return False

        print("Start of all Horizontal words in grid is correct")
        
        for i in range(len(self.AnswersVer)):
            list1 = list(self.AnswersVerStart[i])
            x = list1[0]
            y = list1[1]
            for j in range(len(self.AnswersVer[i])):
                print("x:", x)
                print("j:", j)
                print("y:", y)
                if self.grid[x+j][y] != self.AnswersVer[i][j]:
                    self.message = "Start of Vertical word in grid is not correct"
                    return False

        print("Start of all Vertical words in grid is correct")

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print(self.grid[i][j])
                if self.grid[i][j].isalpha() == False and self.grid[i][j] != "_":
                    print(self.grid[i][j])
                    self.message = "Grid contains non-characters"
                    return False

        print("Grid contains only characters or underscores")
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j].isalpha() and self.grid[i][j].isupper() == False:
                    self.message = "Grid contains non-uppercase characters"
                    return False
        
        print("Grid contains only uppercase characters")    
            
        return True