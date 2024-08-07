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
FONT = pygame.font.SysFont('arial', 25)

# Colours
BACKGROUND = (60, 60, 60)
GREY = (50, 50, 50)
GREEN = (100, 255, 10)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

class Food():
    def __init__(self, snake):
        self.x = place_food(snake)[0]
        self.y = place_food(snake)[1]
        self.is_eaten = False

    def draw(self):
        pygame.draw.rect(DISPLAY, RED, pygame.Rect(self.x + 1, self.y + 1, ELEMENT_SIZE, ELEMENT_SIZE))

class Snake:
    def __init__(self):
        # Start the snake in the middle of the grid
        self.body = [(WIDTH / 2, HEIGHT / 2), 
                     ((WIDTH / 2) - TILE_SIZE, HEIGHT / 2), 
                     ((WIDTH / 2) - (2 * TILE_SIZE), HEIGHT / 2)]
        self.head = self.body[0]
        self.score = 0
        self.food_consumed = False
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
            x = snake_piece[0]
            y = snake_piece[1]
            pygame.draw.rect(DISPLAY, GREEN, pygame.Rect(x + 1, y + 1, ELEMENT_SIZE, ELEMENT_SIZE))
        
        # Draw on the current score
        text = FONT.render("Score: " + str(self.score), True, WHITE)
        DISPLAY.blit(text, [0, 0])
    
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
        x = self.head[0]
        y = self.head[1]
        if self.moving:    
            if self.dx == 1:
                self.head = (x + TILE_SIZE, y)
                self.body.insert(0, self.head)
            elif self.dx == -1:
                self.head = (x - TILE_SIZE, y)
                self.body.insert(0, self.head)
            elif self.dy == 1:
                self.head = (x, y + TILE_SIZE)
                self.body.insert(0, self.head)
            elif self.dy == -1:
                self.head = (x, y - TILE_SIZE)
                self.body.insert(0, self.head)
            if not self.food_consumed:
                self.body.pop()
            else:
                self.food_consumed = False

def place_food(snake):
    # Create food
    x = random.randint(0, (WIDTH - TILE_SIZE) // TILE_SIZE ) * TILE_SIZE 
    y = random.randint(0, (HEIGHT - TILE_SIZE) // TILE_SIZE ) * TILE_SIZE

    # Ensure the food does not spawn inside the snake
    while (x, y) in snake.body:
        x = random.randint(0, (WIDTH - TILE_SIZE) // TILE_SIZE ) * TILE_SIZE 
        y = random.randint(0, (HEIGHT - TILE_SIZE) // TILE_SIZE ) * TILE_SIZE
    
    return [x, y]

def is_collision(snake):
    # Check if the snake hits the edge
    if snake.head[0] > WIDTH - TILE_SIZE or snake.head[0] < 0 or snake.head[1] > HEIGHT - TILE_SIZE or snake.head[1] < 0:
        return True
    # Check if the snake hits itself
    if snake.head in snake.body[1:]:
        return True
    # If no collisions return false
    return False

def check_food(snake, food):
    # Check if the snake has eaten the food
    if snake.head[0] == food.x and snake.head[1] == food.y:
        snake.food_consumed = True
        food.is_eaten = True
        snake.score += 1

def end_game_screen(score):
    # Draw on end text after losing
    DISPLAY.fill(GREY)
    end_text = FONT.render(f'Game over! Score: {snake.score}', True, WHITE)
    DISPLAY.blit(end_text, [195, 295])

if __name__ == '__main__':
    snake = Snake()
    food = Food(snake)

    # Game loop
    while True:
        clock.tick(FPS)
        snake.update_ui()
        if food.is_eaten:
            food = Food(snake)
        food.draw()
        snake.move()
        pygame.display.update()
        check_food(snake, food)
        if is_collision(snake):
            break
    
    # Display end screen after game is finished
    while True:
        end_game_screen(snake.score)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
    