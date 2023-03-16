import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Define the snake class
class Snake:
    def __init__(self):
        self.body = [(250, 250), (240, 250), (230, 250)]
        self.direction = 'RIGHT'
        self.color = white
    
    def move(self):
        x, y = self.body[0]
        if self.direction == 'RIGHT':
            x += 1
        elif self.direction == 'LEFT':
            x -= 1
        elif self.direction == 'UP':
            y -= 1
        elif self.direction == 'DOWN':
            y += 1
        self.body.pop()
        self.body.insert(0, (x, y))
    
    def change_direction(self, new_direction):
        if new_direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
        elif new_direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif new_direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        elif new_direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
    
    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(window, self.color, (x, y, 10, 10))

# Define the food class
class Food:
    def __init__(self):
        self.x = random.randint(0, window_width - 10)
        self.y = random.randint(0, window_height - 10)
        self.color = red
    
    def draw(self):
        pygame.draw.rect(window, self.color, (self.x, self.y, 10, 10))

# Set up the game loop
snake = Snake()
food = Food()
game_over = False
clock = pygame.time.Clock()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_direction('RIGHT')
            elif event.key == pygame.K_LEFT:
                snake.change_direction('LEFT')
            elif event.key == pygame.K_UP:
                snake.change_direction('UP')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('DOWN')
    
    # Move the snake
    snake.move()
    
    # Check if the snake has collided with a wall or itself
    if snake.body[0][0] < 0 or snake.body[0][0] >= window_width or snake.body[0][1] < 0 or snake.body[0][1] >= window_height:
        game_over = True
    for x, y in snake.body[1:]:
        if snake.body[0] == (x, y):
            game_over = True
    
    # Check if the snake has eaten the food
    if snake.body[0] == (food.x, food.y):
        snake.body.append((0, 0))
        food = Food()
    
    # Draw the game objects
    window.fill(black)
    snake.draw()
    food.draw()
    pygame.display.update()
