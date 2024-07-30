import pygame

# Game initialisation and settings
pygame.init()
WIDTH = 600
HEIGHT = 600
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
FPS = 60
BLOCK_SIZE = 30
SNAKE_PIECE_SIZE = BLOCK_SIZE - 2

# Colours
BACKGROUND = (60, 60, 60)
GREY = (50, 50, 50)
GREEN = (100, 255, 10)

# Helper class to track the position of each piece of the snake
class SnakePiece:
    def __init__(self, x, y):
        # Snake attributes
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        # Snake attributes
        self.snake = [SnakePiece(2 * BLOCK_SIZE, 0), SnakePiece(1 * BLOCK_SIZE, 0), SnakePiece(0, 0)]
        self.head = self.snake[0]
        
        # Movement attributes
        self.moving = False
        self.velocity = 1
        self.dx = 0
        self.dy = 0
    
    def move(self):
        if self.moving:    
            if self.dx == 1:
                self.head = SnakePiece(self.head.x + BLOCK_SIZE, self.head.y)
                self.snake.insert(0, self.head)
            elif self.dx == -1:
                self.head = SnakePiece(self.head.x - BLOCK_SIZE, self.head.y)
                self.snake.insert(0, self.head)
            elif self.dy == 1:
                self.head = SnakePiece(self.head.x, self.head.y + BLOCK_SIZE)
                self.snake.insert(0, self. head)
            elif self.dy == -1:
                self.head = SnakePiece(self.head.x, self.head.y - BLOCK_SIZE)
                self.snake.insert(0, self.head)
            self.snake.pop()
    
    def update(self):
        # Draw on the background
        DISPLAY.fill(BACKGROUND)
        for x in range(BLOCK_SIZE, WIDTH, BLOCK_SIZE):
            pygame.draw.line(DISPLAY, GREY, (x, 0), (x, HEIGHT))
        for y in range(BLOCK_SIZE, HEIGHT, BLOCK_SIZE):
            pygame.draw.line(DISPLAY, GREY, (0, y), (WIDTH, y))

        # Draw on the snake 
        for snake_piece in self.snake:
            pygame.draw.rect(DISPLAY, GREEN, pygame.Rect(snake_piece.x + 1, snake_piece.y + 1, SNAKE_PIECE_SIZE, SNAKE_PIECE_SIZE))

if __name__ == '__main__':
    snake = Snake()

    # Game loop
    while True:
        clock.tick(FPS)
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
