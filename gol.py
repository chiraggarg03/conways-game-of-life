import pygame
from random import randint
from copy import deepcopy

Size = 100
Scale = 10
done = False
black = (0,0,0)
white = (255,255,255)
Grid_Current = [[bool(randint(0, 1)) for _ in range(Size)] for _ in range(Size)]


def count_neighbours(x, y, grid):
    global Size
    neighbours = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            neighbours += int(grid[(i + Size) % Size][(j + Size) % Size])
    if not grid[x][y]:
    	return neighbours
    else:
    	return neighbours - 1


def next_state(grid):
    global Size
    grid_next = deepcopy(grid)

    for i in range(Size):
        for j in range(Size):
            neighbours = count_neighbours(i, j, grid)

            if grid[i][j]:
                if (neighbours < 2) or (neighbours > 3):
                    grid_next[i][j] = False
            else:
                if neighbours == 3:
                    grid_next[i][j] = True

    return grid_next


def display_grid(grid):
	global Size
	global Scale

	for i in range(Size):
		for j in range(Size):
			if grid[i][j]:
				pygame.draw.rect(screen, white, pygame.Rect(i * Scale, j * Scale, Scale, Scale))


pygame.init()
screen = pygame.display.set_mode((Size * Scale, Size * Scale))
pygame.display.set_caption('Conway\'s Game of Life')
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(black)
    display_grid(Grid_Current)
    Grid_Current = next_state(Grid_Current)
    pygame.display.update()

    clock.tick(60)