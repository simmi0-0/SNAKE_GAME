import pygame
import random

GAME_WIDTH = 600
GAME_HEIGHT = 400
SPEED = 3
SPACE_SIZE = 20
BODY_PARTS = 2
SNAKE_COLOR = "BLACK"
FOOD_COLOR = "RED"
BACKGROUND_COLOR = "WHITE"

direction = "right"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(BODY_PARTS):
            self.coordinates.append([100 - i * SPACE_SIZE, 100])

    def move(self):
        x, y = self.coordinates[0]

        if direction == "up":
            y -= SPACE_SIZE
        elif direction == "down":
            y += SPACE_SIZE
        elif direction == "left":
            x -= SPACE_SIZE
        elif direction == "right":
            x += SPACE_SIZE

        self.coordinates.insert(0, [x, y])  
        self.coordinates.pop()              

    def grow(self):
        self.coordinates.append(self.coordinates[-1])


class Food:
    def __init__(self):
        self.x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        self.y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE


def next_turn():
    snake.move()

    check_collision()

    head_x, head_y = snake.coordinates[0]
    if head_x == food.x and head_y == food.y:
        snake.grow()
        spawn_food()


def change_direction(new_direction):
    global direction

    opposite = {
        "up": "down",
        "down": "up",
        "left": "right",
        "right": "left"
    }

    if new_direction != opposite[direction]:
        direction = new_direction  


def check_collision():
    head_x, head_y = snake.coordinates[0]

    # Wall collision
    if head_x < 0 or head_x >= GAME_WIDTH or head_y < 0 or head_y >= GAME_HEIGHT:
        game_over()

    # Self collision
    for part in snake.coordinates[1:]:
        if head_x == part[0] and head_y == part[1]:
            game_over()


def spawn_food():
    global food
    food = Food()


def game_over():
    pygame.quit()
    exit()


pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Snake Game")

snake = Snake()
spawn_food()

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_direction("up")
            elif event.key == pygame.K_DOWN:
                change_direction("down")
            elif event.key == pygame.K_LEFT:
                change_direction("left")
            elif event.key == pygame.K_RIGHT:
                change_direction("right")

    next_turn()

    screen.fill(BACKGROUND_COLOR)

    # Draw snake
    for x, y in snake.coordinates:
        pygame.draw.rect(screen, SNAKE_COLOR, (x, y, SPACE_SIZE, SPACE_SIZE))

    # Draw food
    pygame.draw.rect(screen, FOOD_COLOR, (food.x, food.y, SPACE_SIZE, SPACE_SIZE))

    pygame.display.flip()
    clock.tick(SPEED)

pygame.quit()