# version of game with no ui.
# runs quicker then the ui version

import numpy as np
import random


#cleaning session for robby
def cleaning(robby):
    x, y = 1, 1
    vel = 1
    fitness = 0
    run = True
    prevmove = 9
    move_count = 200
    grid = makeMap()

    while run and move_count > 0:
        move = robby.move(grid, x, y)

        if int(move) == 6:
            move = random.randint(0, 5)
        # if prev move was stay put makes the move random
        if int(move) == 5:
            if prevmove == move:
                move = random.randint(0, 5)
            else:
                move_count -= 1

        if int(move) == 3:
            if x - vel >= 0:
                x -= vel
            else:
                fitness -= 5
            move_count -= 1

        if int(move) == 2:
            if x + vel + 1 <= 10:
                x += vel
            else:
                fitness -= 5
            move_count -= 1

        if int(move) == 0:
            if y - vel >= 0:
                y -= vel
            else:
                fitness -= 5
            move_count -= 1

        if int(move) == 1:
            if y + vel + 1 <= 10:
                y += vel
            else:
                fitness -= 5
            move_count -= 1

        if int(move) == 4:
            if grid[x][y] == 1:
                grid[x][y] = 0
                fitness += 10
            else:
                fitness -= 1

            move_count -= 1
        prevmove = move
    return fitness




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

