import pygame
import random
import numpy as np

import robby

pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

robbyIMG = pygame.image.load('images/Idle.png')
trashIMG = pygame.image.load('images/trash.png')

width = 500
height = 500
menuheight = 100
windowSize = width, height + menuheight
win = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Robby Robot")


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


def drawGrid(g,x,y):
    win.fill(WHITE)
    # Vertical Lines
    for i in range(10):
        pygame.draw.line(win, BLACK, (i * 50, 0), (i * 50, height), 2)
    # Horizontal Lines
    for i in range(11):
        pygame.draw.line(win, BLACK, (0, i * 50), (width, i * 50), 2)
    # draw Robby
    win.blit(robbyIMG, (x, y))
    # draw soda cans
    for i in range(10):
        for j in range(10):
            if g[i][j] == 1:
               win.blit(trashIMG, (i*50 + 12.5, j * 50 + 12.5))


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


# draw fitness score and move count
def drawtext(score, count):
    scoreText = pygame.font.Font('freesansbold.ttf', 22)
    textSurf, textRect = text_objects('Fitness: ', scoreText)
    textRect.center = (50, 525)
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects(str(score), scoreText)
    textRect.center = (150, 525)
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects('Moves: ', scoreText)
    textRect.center = (50, 575)
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects(str(count), scoreText)
    textRect.center = (150, 575)
    win.blit(textSurf, textRect)





def gameloop():
    x, y = 1, 1
    charsize = charwidth, charheight = (50, 50)
    vel = 50
    score = 0

    run = True
    movecount = 200
    clock = pygame.time.Clock()
    grid = makeMap()
    robot = robby.Robby()


    while run and movecount > 0:
        pygame.time.delay(500)
        move = robot.move(grid, x // 50, y // 50)
        print(move)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if int(move) == 6:
            move = random.randint(0, 6)

        if keys[pygame.K_LEFT] or int(move) == 3:
            if x - vel >= 0:
                x -= vel
            else:
                score -= 5
            movecount -= 1

        if keys[pygame.K_RIGHT] or int(move) == 2:
            if x + vel + charwidth <= width + 1:
                x += vel
            else:
                score -= 5
            movecount -= 1

        if keys[pygame.K_UP] or int(move) == 0:
            if y - vel >= 0:
                y -= vel
            else:
                score -= 5
            movecount -= 1

        if keys[pygame.K_DOWN] or int(move) == 1:
            if y + vel + charheight <= height + 1:
                y += vel
            else:
                score -= 5
            movecount -= 1

        if keys[pygame.K_SPACE] or int(move) == 5:
            if grid[x // 50][y // 50] == 1:
                grid[x // 50][y // 50] = 0
                score += 10
            else:
                score -= 1

            movecount -= 1

        if int(move) == 4:
            movecount -= 1

        drawGrid(grid, x, y)
        drawtext(score, movecount)
        pygame.display.update()
    return  score


gameloop()
pygame.quit()
quit()



