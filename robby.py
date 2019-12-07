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
            move = move + 3**1 + 2
        elif grid[x - 1][y] == 1:  # left has a can
            move = move + 3**1 + 1
        else:  # left is empty
            move = move + 3**1 + 0

        # down 3**2
        if y + 1 > 9:  # below is a wall
            move = move + 3**3 + 2
        elif grid[x][y+1] == 1:  # below has a can
            move = move + 3**3 + 1
        else:  # below is empty
            move = move + 3**2 + 0

        # right 3**3
        if x + 1 > 9:  # right is a wall
            move = move + 3**3 + 2
        elif grid[x+1][y] == 1:  # right has a can
            move = move + 3**3 + 1
        else:  # right is empty
            move = move + 3**3 + 0

        # current spot 3**4
        if x > 20:  # current is a wall, not possible, could optimize and shorten the gene a bit
            move = move + 3 ** 4 + 2
        elif grid[x][y] == 1:  # current has a can
            move = move + 3 ** 4 + 1
        else:  # current is empty
            move = move + 3 ** 4 + 0
        return self.gene[move]


