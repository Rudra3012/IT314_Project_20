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
    id: uuid
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
    rating: int

    def __init__(self, creator, title, description, width, height, cluesVer, cluesHor, WordsUp, WordsDown, gridList, AnswersHorStart, AnswersVerStart):
        unique_id = uuid.uuid4()
        self.id = unique_id
        self.creator = creator
        self.title = title
        self.description = description
        self.width = width
        self.height = height
        self.AnswersHor = WordsUp
        self.AnswersVer = WordsDown
        self.grid = gridList
        self.cluesHor = cluesHor
        self.cluesVer = cluesVer
        self.AnswersHorStart = AnswersHorStart
        self.AnswersVerStart = AnswersVerStart
        self.timeOfCreation = datetime.datetime.now()
        self.rating = 0

    def __str__(self):
        return f"Crossword: {self.title}"
