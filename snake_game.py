import pygame

# Game initialisation and settings
pygame.init()
WIDTH = 600
HEIGHT = 600
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
FPS = 30
BLOCK_SIZE = 20

# Colours
BACKGROUND = (60, 60, 60)
GREY = (50, 50, 50)

# Helper function to draw the background
def draw_background():
        # Fill the screen
        DISPLAY.fill(BACKGROUND)
        # Draw grid
        for x in range(BLOCK_SIZE, WIDTH, BLOCK_SIZE):
            pygame.draw.line(DISPLAY, GREY, (x, 0), (x, HEIGHT))
        for y in range(BLOCK_SIZE, HEIGHT, BLOCK_SIZE):
            pygame.draw.line(DISPLAY, GREY, (0, y), (WIDTH, y))


# Game loop
while True:
    clock.tick(FPS)
    draw_background()

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
         
    pygame.display.update()

pygame.quit()
