import sys, pygame


def makeMap():
    grid = []
    for row in range(10):
        grid.append([])
        for column in range(10):
            grid[row].append(0)
    return grid

def drawGrid():
    win.fill(WHITE)
    for i in range(10):
        pygame.draw.line(win, BLACK, (i * 50, 0), (i * 50, height), 2)
    for i in range(10):
        pygame.draw.line(win, BLACK, (0, i * 50), (width, i * 50), 2)
    pygame.draw.rect(win, (255, 0, 0), (x, y, charwidth, charheight))


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

windowSize = width, height = 500, 500
margin = 5
win = pygame.display.set_mode(windowSize)

pygame.display.set_caption("Robby Robot")

win.fill(WHITE)
for i in range(10):
    pygame.draw.line(win, BLACK, (i*50, 0), (i*50, height), 2)
for i in range(10):
    pygame.draw.line(win, BLACK, (0, i*50), (width, i*50), 2)
x, y = 51, 51
charsize = charwidth, charheight = (50, 50)
vel = 50

run = True
count = 200
clock = pygame.time.Clock()
grid = makeMap()

while run and count > 0:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x - vel >= 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x + vel + charwidth <= width + 1:
        x += vel
    if keys[pygame.K_UP] and y - vel >= 0:
        y -= vel
    if keys[pygame.K_DOWN] and y + vel + charheight <= height + 1:
        y += vel



    drawGrid()
    pygame.display.update()

pygame.quit()



