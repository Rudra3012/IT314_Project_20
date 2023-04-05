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
    id: int
    title: str
    description: str
    width: int
    height: int
    cluesUp = []
    AnswersUp = []
    AnswersDown = []
    cluesDown = []
    timeOfCreation: str
    clueAnswers={}
    grid=[]
    rating: int
    def __init__(self, title, description, width, height, cluesUp, cluesDown, WordsUp,WordsDown, gridList):
        unique_id = uuid.uuid4()
        self.id = unique_id
        self.title = title
        self.description = description
        self.width = width
        self.height = height
        self.AnswersUp = WordsUp
        self.AnswersDown = WordsDown
        self.grid = gridList
        self.cluesUp = cluesUp
        self.cluesDown = cluesDown

        self.timeOfCreation = datetime.datetime.now()
        self.rating = 0
    def __str__(self):
        return f"Crossword: {self.title}"


