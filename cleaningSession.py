# version of game with no ui.
# runs quicker then the ui version

import numpy as np
import random

width = 500
height = 500

#cleaning session for robby
def cleaning(robby):
    x, y = 1, 1
    charwidth, charheight = (50, 50)
    vel = 50
    fitness = 0
    run = True
    move_count = 200
    grid = makeMap()
    prevmove = 7;

    while run and move_count > 0:
        move = robby.move(grid, x // 50, y // 50)
        # this block is to prevent robby from cycling back and forth
        if move == prevmove:
            fitness - 1
        if move_count % 2 == 0:
            prevmove = move

        if int(move) == 6:
            move = random.randint(0, 6)

        if int(move) == 3:
            if x - vel >= 0:
                x -= vel
            else:
                fitness -= 5
            move_count -= 1

        if int(move) == 2:
            if x + vel + charwidth <= width + 1:
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
            if y + vel + charheight <= height + 1:
                y += vel
            else:
                fitness -= 5
            move_count -= 1

        if int(move) == 5:
            if grid[x // 50][y // 50] == 1:
                grid[x // 50][y // 50] = 0
                fitness += 20
            else:
                fitness -= 1

            move_count -= 1

        if int(move) == 4:
            fitness -= 2
            move_count -= 1
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

