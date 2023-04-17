import enum
import itertools
import math
import numpy as np
import random
from datetime import datetime


@enum.unique
class Direction(enum.Enum):
    ACROSS = enum.auto()
    DOWN = enum.auto()

    def __str__(self):
        return ("ACROSS" if self is Direction.ACROSS else "DOWN")

    def get_deltas(self):
        delta_r = int(self == Direction.DOWN)
        delta_c = int(self == Direction.ACROSS)
        return (delta_r, delta_c)

    @staticmethod
    def random():
        return random.choice(list(Direction))


class GridWord:
    def __init__(self, word: str, r: int, c: int, direction: Direction):
        if not isinstance(word, str):
            raise TypeError("word must be a string")
        if not (isinstance(r, int) and isinstance(c, int) and r >= 0 and c >= 0):
            raise ValueError("Row and column positions must be positive integers")
        if not isinstance(direction, Direction):
            raise TypeError("Direction must be an enum of type Direction")

        self.word = word.upper()
        self.r1 = r
        self.c1 = c
        self.direction = direction
        self.delta_r, self.delta_c = self.direction.get_deltas()

        self.__len = len(self.word)
        self.r2 = self.r1 + (self.__len - 1) * self.delta_r
        self.c2 = self.c1 + (self.__len - 1) * self.delta_c

    def __str__(self):
        return (f"{self.word}, ({self.r1}, {self.c1}) -- ({self.r2}, {self.c2}), {self.direction}")

    def __len__(self):
        return (self.__len)

    def __contains__(self, item):
        if isinstance(item, str):
            # The left operand is a string
            return (item in self.word)
        elif isinstance(item, tuple) and len(item) == 2 and isinstance(item[0], int) and isinstance(item[1], int):
            # The left operand is a tuple that contains two integers, i.e. a
            # coordinate pair
            return (self.r1 <= item[0] and item[0] <= self.r2 and
                    self.c1 <= item[1] and item[1] <= self.c2)
        else:
            raise TypeError("'in <GridWord>' requires string or coordinate pair as left operand")

    def __getitem__(self, item):
        try:
            return (self.word[item])
        except:
            raise

    def intersects(self, other):
        if not isinstance(other, GridWord):
            raise TypeError("Intersection is only defined for two GridWords")
        if self.direction == other.direction:
            raise ValueError("Intersection is only defined for GridWords placed in different directions")

        for idx1, letter1 in enumerate(self.word):
            for idx2, letter2 in enumerate(other.word):
                rr1 = self.r1 + idx1 * self.delta_r
                cc1 = self.c1 + idx1 * self.delta_c
                rr2 = other.r1 + idx2 * self.delta_c  # because the direction is reversed
                cc2 = other.c1 + idx2 * self.delta_r
                if letter1 == letter2 and rr1 == rr2 and cc1 == cc2:
                    return (True)
        return (False)

    def overlaps(self, other):
        if not isinstance(other, GridWord):
            raise TypeError("Overlap check is only defined for two GridWords")
        if self.direction == other.direction:
            return ((self.r1, self.c1) in other or (other.r1, other.c1) in self)

        for idx, letter in enumerate(self.word):
            rr = self.r1 + idx * self.delta_r
            cc = self.c1 + idx * self.delta_c
            if (rr, cc) in other:
                return (True)
        return (False)

    def adjacent_to(self, other):
        if not isinstance(other, GridWord):
            raise TypeError("Adjacency is only defined for two GridWords")
        if self.direction != other.direction:
            return (False)
        for delta in [-1, 1]:
            for idx in range(self.__len):
                r = self.r1 + idx * self.delta_r + delta * self.delta_c
                c = self.c1 + idx * self.delta_c + delta * self.delta_r
                if (r, c) in other:
                    return (True)

            # (-1) point directly to the left of (or above) a word placed across
            # (or down)
            #
            # (1) point directly to the right of (or below) a word placed across
            # (or down)
            if delta == -1:
                r = self.r1 + delta * self.delta_r
                c = self.c1 + delta * self.delta_c
            elif delta == 1:
                r = self.r2 + delta * self.delta_r
                c = self.c2 + delta * self.delta_c
            if (r, c) in other:
                return (True)
        return (False)


class Grid:
    def __init__(self, num_rows=50, num_cols=50):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid = np.full([self.num_rows, self.num_cols], "")
        self.grid_words = []

    def __str__(self):
        s = ""

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                s += self.grid[i][j] if self.grid[i][j] != "" else "-"
            s += "\n"
        return (s)

    def __approximate_center(self):
        center = (math.floor(self.num_rows / 2), math.floor(self.num_cols / 2))
        return (center)

    def __insert_word(self, grid_word):
        if not isinstance(grid_word, GridWord):
            raise TypeError("Only GridWords can be inserted into the Grid")
        delta_r, delta_c = grid_word.direction.get_deltas()
        for idx, letter in enumerate(grid_word.word):
            self.grid[grid_word.r1 + idx * delta_r, grid_word.c1 + idx * delta_c] = letter
        self.grid_words.append(grid_word)

    def __word_fits(self, word: str, r: int, c: int, d: Direction):
        # Make sure we aren't inserting the word outside the grid
        if ((d == Direction.DOWN and r + len(word) >= self.num_rows) or
                (d == Direction.ACROSS and c + len(word) >= self.num_cols)):
            return (False)
        grid_word = GridWord(word, r, c, d)

        check = False
        for gw in self.grid_words:
            if grid_word.adjacent_to(gw):
                # If the word is adjacent to any other words in the grid, we can
                # exit right away because it doesn't fit
                return (False)
            if grid_word.overlaps(gw):
                if d == gw.direction:
                    # If the word overlaps another word that is placed in the
                    # same direction, we can exit right away
                    return (False)
                elif not grid_word.intersects(gw):
                    # If the word overlaps another word that is placed in the
                    # other direction but DOESN'T intersect it (i.e. the overlap
                    # doesn't happen on the same letter in each word), we can
                    # exit right away
                    return (False)
                else:
                    check = True
            else:
                # If the word doesn't overlap the current word (already in the
                # grid) that's being checked, we don't know yet whether or not
                # we CAN or CANNOT place it on the grid
                pass
        return (check)

    def __scan_and_insert_word(self, word):
        if not isinstance(word, str):
            raise TypeError("Only strings can be inserted into the puzzle by scanning")
        if len(self.grid_words) == 0:
            self.__insert_word(GridWord(word, *self.__approximate_center(), Direction.random()))
            return (None)
        for d, r, c in itertools.product(list(Direction), range(self.num_rows), range(self.num_cols)):
            if self.__word_fits(word, r, c, d):
                grid_word = GridWord(word, r, c, d)
                self.__insert_word(grid_word)
                break

    def scan_and_insert_all_words(self, words):
        for word in words:
            self.__scan_and_insert_word(word)

    def __randomly_insert_word(self, word):
        if not isinstance(word, str):
            raise TypeError("Only strings can be randomly inserted into the puzzle")
        if len(self.grid_words) == 0:
            self.__insert_word(GridWord(word, *self.__approximate_center(), Direction.random()))
            return (None)
        num_iterations = 0
        while num_iterations <= 10000:
            rand_r = random.randint(0, self.num_rows - 1)
            rand_c = random.randint(0, self.num_cols - 1)
            d = Direction.random()
            if self.__word_fits(word, rand_r, rand_c, d):
                grid_word = GridWord(word, rand_r, rand_c, d)
                self.__insert_word(grid_word)
                break
            num_iterations += 1

    def crop(self):
        min_c = min([word.c1 for word in self.grid_words])
        min_r = min([word.r1 for word in self.grid_words])
        max_c = max([word.c2 for word in self.grid_words])
        max_r = max([word.r2 for word in self.grid_words])

        cropped_grid = Grid(max_r - min_r + 1, max_c - min_c + 1)
        for grid_word in self.grid_words:
            cropped_word = GridWord(grid_word.word, grid_word.r1 - min_r,
                                    grid_word.c1 - min_c, grid_word.direction)
            cropped_grid.__insert_word(cropped_word)
        return (cropped_grid)


def generate_crossword(words):
    random.seed(datetime.now().timestamp())
    g = Grid()
    g.scan_and_insert_all_words(words)
    g = g.crop()

    grid_string = str(g)
    return grid_string


def getWordOrient(gridStr, words):
    print(("Received gridStr:", gridStr))
    print(("Received words:", words))
    # print(type(gridStr))
    h = 0
    w = -1
    l = -1
    grid = []
    row = []
    for i in range(len(gridStr)):
        # print(f'gridStr[{i}] = {gridStr[i]}')
        if gridStr[i] == '\n':
            # print('New line')
            grid.append(row)
            row = []
        else:
            # print('Appending')
            row.append(gridStr[i])
    # print(grid)
    w = len(grid[0])
    h = len(grid)
    dict = {}
    wordsHor = []
    wordsVer = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != '-':
                if (i - 1, j, 1) not in dict:
                    dict[(i, j, 1)] = grid[i][j]
                if (i, j - 1, 0) not in dict:
                    dict[(i, j, 0)] = grid[i][j]

                if (i - 1, j, 1) in dict:
                    dict[(i, j, 1)] = dict[(i - 1, j, 1)] + grid[i][j]
                    if dict[(i, j, 1)] in words:
                        wordsHor.append({dict[(i, j, 1)]: (i - len(dict[(i, j, 1)]) + 1, j)})
                if (i, j - 1, 0) in dict:
                    dict[(i, j, 0)] = dict[(i, j - 1, 0)] + grid[i][j]
                    if dict[(i, j, 0)] in words:
                        wordsVer.append({dict[(i, j, 0)]: (i, j - len(dict[(i, j, 0)]) + 1)})
    print(dict)
    print(wordsHor)
    print(wordsVer)
    return wordsHor, wordsVer
