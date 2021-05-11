import pygame
from random import randint
from copy import deepcopy

# Global Variables
Size = 100    # Controls size of display
Scale = 10    # Controls size of box
done = False    # Controls loop
black = (0,0,0)    # PyGame Colour Tuples
white = (255,255,255)
Grid_Current = [[bool(randint(0, 1)) for _ in range(Size)] for _ in range(Size)]    # Grid with random sections


# Counts neighbours to a cell. Uses wrap around for cells at the edges
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


# Returns the next state of the grid according the rules of the game
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


# Displays the grid given to it as a parameter
def display_grid(grid):
	global Size
	global Scale

	for i in range(Size):
		for j in range(Size):
			if grid[i][j]:
				pygame.draw.rect(screen, white, pygame.Rect(i * Scale, j * Scale, Scale, Scale))


# PyGame initialisation
pygame.init()
screen = pygame.display.set_mode((Size * Scale, Size * Scale))
pygame.display.set_caption('Conway\'s Game of Life')
clock = pygame.time.Clock()

# Execution Loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(black)
    display_grid(Grid_Current)
    Grid_Current = next_state(Grid_Current)
    pygame.display.update()

    clock.tick(60)
