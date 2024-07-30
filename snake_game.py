import pygame

# Game initialisation and settings
pygame.init()
WIDTH = 600
HEIGHT = 600
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
FPS = 20
BLOCK_SIZE = 30
SNAKE_SIZE = BLOCK_SIZE - 6

# Colours
BACKGROUND = (60, 60, 60)
GREY = (50, 50, 50)
GREEN = (100, 255, 10)

class Snake:
    def __init__(self, x, y):
        # Snake attributes
        self.x = x
        self.y = y
        self.colour = GREEN
        self.entity = pygame.Surface((SNAKE_SIZE, SNAKE_SIZE))
        self.rect = self.entity.get_rect(topleft=(self.x, self.y))

        # Movement attrivutes
        self.moving = False
        self.velocity = 1
        self.dx = self.velocity
        self.dy = 0
    
    def move(self):
        if self.moving == True:
            self.x += self.dx
            self.y += self.dy
    
    def update(self):
        # Fill in the snake 
        self.entity.fill(self.colour)

        # Ensure the snake is inside of the grid blocks
        self.rect.x = self.x * BLOCK_SIZE + 3
        self.rect.y = self.y * BLOCK_SIZE + 3

        # Draw the snake 
        DISPLAY.blit(self.entity, self.rect)

# Helper function to draw the background
def draw_background():
        # Fill the screen
        DISPLAY.fill(BACKGROUND)
        # Draw grid
        for x in range(BLOCK_SIZE, WIDTH, BLOCK_SIZE):
            pygame.draw.line(DISPLAY, GREY, (x, 0), (x, HEIGHT))
        for y in range(BLOCK_SIZE, HEIGHT, BLOCK_SIZE):
            pygame.draw.line(DISPLAY, GREY, (0, y), (WIDTH, y))

if __name__ == '__main__':
    snake = Snake(0, 0)

    # Game loop
    while True:
        clock.tick(FPS)
        draw_background()
        snake.update()
        snake.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                snake.moving = True
                if event.key == pygame.K_RIGHT:
                    snake.dx = snake.velocity
                    snake.dy = 0
                elif event.key == pygame.K_LEFT:
                    snake.dx = -snake.velocity
                    snake.dy = 0
                elif event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -snake.velocity
                elif event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = snake.velocity
                

            
        pygame.display.update()

    pygame.quit()
