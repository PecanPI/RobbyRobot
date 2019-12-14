import random

def make_gene(self):
    gene = ""
    gene_length = 243
    for i in range(gene_length):
        gene = gene + str(random.randint(0, 6))
    return gene


class Robby:
    gene = ""
    x_pos = 0
    y_pos = 0
    fitness = 0

    def __init__(self):
        self.gene = make_gene(self)

    def __str__(self):
        return self.gene

    def __repr__(self):
        return self.gene

    def set_fitness(self, fit):
        self.fitness = fit

    def set_gene(self, gene):
        self.gene = gene

    def move(self, grid, x, y):
        move = 0

        # for top 3**0
        # if space above is a wall base 3 is 2
        # if space above is a can 1, and empty is 0
        if y - 1 < 0:
            move = move + 2
        elif grid[x][y-1] == 1:
            move = move + 1
        else:
            move = move + 0

        # for left 3**1
        if x - 1 < 0:  # left is a wall
            move = move + 20
        elif grid[x - 1][y] == 1:  # left has a can
            move = move + 10
        else:  # left is empty
            move = move + 0

        # down 3**2
        if y + 1 > 9:  # below is a wall
            move = move + 200
        elif grid[x][y+1] == 1:  # below has a can
            move = move + 100
        else:  # below is empty
            move = move + 0

        # right 3**3
        if x + 1 > 9:  # right is a wall
            move = move + 2000
        elif grid[x+1][y] == 1:  # right has a can
            move = move + 1000
        else:  # right is empty
            move = move + 0

        # current spot 3**4
        if x > 20:  # current is a wall, not possible, could optimize and shorten the gene a bit
            move = move + 20000
        elif grid[x][y] == 1:  # current has a can
            move = move + 10000
        else:  # current is empty
            move = move + 0

        # move needs to be converted from ternary to decmial
        move = to_decimal(str(move), 3)
        return self.gene[move]


# https://www.reddit.com/r/learnpython/comments/1rvl8s/how_to_convert_a_number_from_any_base_to_base_10/
def to_decimal(number, base):
    result = 0
    for index, character in enumerate(number):
        result += int(character) * base ** index
    return result