import sys, pygame
import numpy as np
from PIL import Image

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


def drawGrid(g):
    win.fill(WHITE)
    # Vertical Lines
    for i in range(10):
        pygame.draw.line(win, BLACK, (i * 50, 0), (i * 50, height), 2)
    # Horizontal Lines
    for i in range(11):
        pygame.draw.line(win, BLACK, (0, i * 50), (width, i * 50), 2)

    #draw Robby
    win.blit(robbyIMG, (x, y))
    #pygame.draw.rect(win, (255, 0, 0), (x, y, charwidth, charheight))
    # draw soda cans
    for i in range(10):
        for j in range(10):
            if g[i][j] == 1:
               win.blit(trashIMG, (i*50 + 12.5, j * 50 + 12.5))


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


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

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Fitness: ', False, BLACK)

robbyIMG = pygame.image.load('images/Idle.png')
trashIMG = pygame.image.load('images/trash.png')

pygame.init()

width = 500
height = 500
menuheight = 100
windowSize = width, height + menuheight
margin = 5
win = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Robby Robot")

x, y = 51, 51
charsize = charwidth, charheight = (50, 50)
vel = 50

run = True
movecount = 200
clock = pygame.time.Clock()
grid = makeMap()

while run and movecount > 0:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    text = font.render('Fitness: ', False, BLACK)
    win.blit(text, (550, 25))
    if keys[pygame.K_LEFT]:
        if x - vel >= 0:
            x -= vel
        movecount -= 1
        pygame.time.delay(100)
    if keys[pygame.K_RIGHT]:
        if x + vel + charwidth <= width + 1:
            x += vel
        movecount -= 1
        pygame.time.delay(100)
    if keys[pygame.K_UP]:
        if y - vel >= 0:
            y -= vel
        movecount -= 1
        pygame.time.delay(100)
    if keys[pygame.K_DOWN]:
        if y + vel + charheight <= height + 1:
            y += vel
        movecount -= 1
        pygame.time.delay(100)
    if keys[pygame.K_SPACE]:
        if grid[x // 50][y // 50] == 1:
            grid[x // 50][y // 50] = 0
        pygame.time.delay(100)
        movecount -= 1

    drawGrid(grid)
    drawtext(0, movecount)
    pygame.display.update()

pygame.quit()



