# version of game with no ui.
# runs quicker then the ui version

import numpy as np
import random


#cleaning session for robby
def cleaning(robby):
    x, y = 0, 0
    vel = 1
    fitness = 0
    run = True
    move_count = 200
    grid = makeMap()

    while run and move_count > 0:
        move = robby.move(grid, x, y)
        # move up

        # random move
        if int(move) == 6:
            move = random.randint(0, 5)
        # move up
        if int(move) == 0:
            if y - vel >= 0:
                y -= vel
            else:
                fitness -= 5
            move_count -= 1
        # move down
        if int(move) == 1:
            if y + vel < 9:
                y += vel
            else:
                fitness -= 5
            move_count -= 1
        # move right
        if int(move) == 2:
            if x + vel < 9:
                x += vel
            else:
                fitness -= 5
            move_count -= 1
        #  move left
        if int(move) == 3:
            if x - vel >= 0:
                x -= vel
            else:
                fitness -= 5
            move_count -= 1
        # pick up
        if int(move) == 4:
            if grid[x][y] == 1:
                grid[x][y] = 0
                fitness += 10
            else:
                fitness -= 1
            move_count -= 1
        # stay put
        if int(move) == 5:
            fitness -= 1
            move_count -= 1

    return fitness



# makes a random mount

def makeMap():
    g = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    g = g.ravel()
    np.random.shuffle(g)
    g = g.reshape(10, 10)
    return g

