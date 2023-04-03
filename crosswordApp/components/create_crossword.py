from django_unicorn.components import UnicornView
import CrosswordGenerator as cg
from crosswordApp.models import crossword


class CreateCrosswordView(UnicornView):
    title: str=""
    description: str=""
    word: str=""
    clue: str=""
    clues_and_words = []
    crossword_grid=[]

    def add_clue_and_word(self):
        print(f'add clue and word: {self.clue} {self.word}')
        self.clues_and_words.append((self.clue, self.word))
        self.word = ""
        self.clue = ""

    def reset_page(self):
        self.title=""
        self.description=""
        self.word=""
        self.clue=""
        self.clues_and_words = []
        self.crossword_grid=[]

    def generate(self):
        print("Generate crossword")
        print("Title: " + self.title)
        print("Description: " + self.description)
        print("Words and clues: " + str(self.clues_and_words))

        words = [word for clue, word in self.clues_and_words]

        grid=cg.generate_crossword(words)
        print(grid)
        row=[]

        for i in range(len(grid)):
            if grid[i]!='\n':
                row.append(grid[i])
            else:
                self.crossword_grid.append(row)
                row=[]

        print(self.crossword_grid)

    def save_crossword(self):
            # print("Save crossword")
            # print("Title: " + self.title)
            # print("Description: " + self.description)
            # print("Words and clues: " + str(self.clues_and_words))
            # print("Crossword grid: " + str(self.crossword_grid))
            grid_dict = {}
            for i in range(len(self.crossword_grid)):
                for j in range(len(self.crossword_grid[i])):
                    grid_dict[(i,j)] = self.crossword_grid[i][j]
            print(grid_dict)
            crossword.objects.create(title=self.title, description=self.description, width=len(self.crossword_grid), height=len(self.crossword_grid[0]) , grid=grid_dict)
