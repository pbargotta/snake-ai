import pygame
import random

# Game initialisation and settings
pygame.init()
WIDTH = 600
HEIGHT = 600
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
FPS = 10
TILE_SIZE = 30
ELEMENT_SIZE = TILE_SIZE - 2

# Colours
BACKGROUND = (60, 60, 60)
GREY = (50, 50, 50)
GREEN = (100, 255, 10)
RED = (255, 0, 0)

# Helper class to track the position of each piece of the snake
class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Food(Block):
    def __init__(self, snake):
        self.pos = place_food(snake)
        self.is_eaten = False
        Block.__init__(self, self.pos[0], self.pos[1])

    def draw(self):
        pygame.draw.rect(DISPLAY, RED, pygame.Rect(self.x + 1, self.y + 1, ELEMENT_SIZE, ELEMENT_SIZE))

class Snake:
    def __init__(self):
        # Snake attributes
        self.body = [Block(2 * TILE_SIZE, 0), Block(1 * TILE_SIZE, 0), Block(0, 0)]
        self.head = self.body[0]
        
        # Movement attributes
        self.moving = False
        self.dx = 0
        self.dy = 0
    
    def update_ui(self):
        # Draw on the background
        DISPLAY.fill(BACKGROUND)
        for x in range(TILE_SIZE, WIDTH, TILE_SIZE):
            pygame.draw.line(DISPLAY, GREY, (x, 0), (x, HEIGHT))
        for y in range(TILE_SIZE, HEIGHT, TILE_SIZE):
            pygame.draw.line(DISPLAY, GREY, (0, y), (WIDTH, y))

        # Draw on the snake 
        for snake_piece in self.body:
            pygame.draw.rect(DISPLAY, GREEN, pygame.Rect(snake_piece.x + 1, snake_piece.y + 1, ELEMENT_SIZE, ELEMENT_SIZE))
            
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            # Control the direction of the snake - ensures snake can not backtrack on itself
            if event.type == pygame.KEYDOWN:
                self.moving = True
                if event.key == pygame.K_RIGHT and self.dx != -1:
                    self.dx = 1
                    self.dy = 0
                elif event.key == pygame.K_LEFT and self.dx != 1:
                    self.dx = -1
                    self.dy = 0
                elif event.key == pygame.K_UP and self.dy != 1:
                    self.dx = 0
                    self.dy = -1
                elif event.key == pygame.K_DOWN and self.dy != -1:
                    self.dx = 0
                    self.dy = 1

        # Move the snake
        if self.moving:    
            if self.dx == 1:
                self.head = Block(self.head.x + TILE_SIZE, self.head.y)
                self.body.insert(0, self.head)
            elif self.dx == -1:
                self.head = Block(self.head.x - TILE_SIZE, self.head.y)
                self.body.insert(0, self.head)
            elif self.dy == 1:
                self.head = Block(self.head.x, self.head.y + TILE_SIZE)
                self.body.insert(0, self. head)
            elif self.dy == -1:
                self.head = Block(self.head.x, self.head.y - TILE_SIZE)
                self.body.insert(0, self.head)
            self.body.pop()

def place_food(snake):
    # Create food
    x = random.randint(0, (WIDTH - TILE_SIZE) // TILE_SIZE ) * TILE_SIZE 
    y = random.randint(0, (HEIGHT - TILE_SIZE) // TILE_SIZE ) * TILE_SIZE

    print(snake.body)
    # Ensure the food does not spawn inside the snake
    while Block(x, y) in snake.body:
        x = random.randint(0, (WIDTH - TILE_SIZE) // TILE_SIZE ) * TILE_SIZE 
        y = random.randint(0, (HEIGHT - TILE_SIZE) // TILE_SIZE ) * TILE_SIZE
    
    return [x, y]

def handle_collisions(score, snake, food):
    def is_collision():
        # Check if the snake hits the edge
        if snake.head.x > WIDTH - TILE_SIZE or snake.head.x < 0 or snake.head.y > HEIGHT - TILE_SIZE or snake.head.y < 0:
            return True
        # Check if the snake hits itself
        if snake.head in snake.body[1:]:
            return True
        return False
    
    # Check if the snake has eaten the food
    if snake.head.x == food.x and snake.head.y == food.y:
        food.is_eaten = True
        score += 1

    if is_collision():
        print("SCORE: " + str(score))
    
    return score
    

if __name__ == '__main__':
    score = 0
    snake = Snake()
    food = Food(snake)

    # Game loop
    while True:
        clock.tick(FPS)
        snake.update_ui()
        score = handle_collisions(score, snake, food)
        if food.is_eaten:
            food = Food(snake)
        food.draw()
        snake.move()
        pygame.display.update()

    pygame.quit()
