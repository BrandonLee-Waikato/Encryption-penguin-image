import pygame
import random

# Initialize pygame
pygame.init()

# Game constants
WIDTH = 480
HEIGHT = 320
BIRD_Y_CHANGE = 5
PIPE_GAP = 75
PIPE_FREQUENCY = 150
PIPE_SPEED = 2
SCORE_FONT_SIZE = 32

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()


def draw_bird(bird_y):
    pygame.draw.circle(screen, RED, (50, bird_y), 10)


def draw_pipe(pipe_x, gap_start):
    pygame.draw.rect(screen, GREEN, (pipe_x, 0, 50, gap_start))
    pygame.draw.rect(screen, GREEN, (pipe_x, gap_start + PIPE_GAP, 50, HEIGHT))


def game():
    bird_y = HEIGHT // 2
    bird_y_change = 0
    pipes = []
    score = 0
    game_over = False

    while not game_over:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bird_y_change = -BIRD_Y_CHANGE
                elif event.key == pygame.K_DOWN:
                    bird_y_change = BIRD_Y_CHANGE

        bird_y += bird_y_change

        # Draw the bird
        draw_bird(bird_y)

        # Generate pipes
        if len(pipes) == 0 or pipes[-1]['x'] <= WIDTH - PIPE_FREQUENCY:
            gap_start = random.randint(20, HEIGHT - PIPE_GAP - 20)
            pipes.append({'x': WIDTH, 'gap_start': gap_start})

        # Move and draw pipes
        for pipe in pipes:
            pipe['x'] -= PIPE_SPEED
            draw_pipe(pipe['x'], pipe['gap_start'])

        # Check for collisions
        for pipe in pipes:
            if 40 > pipe['x'] > 0:
                if bird_y < pipe['gap_start'] or bird_y > pipe['gap_start'] + PIPE_GAP:
                    game_over = True
                else:
                    score += 1

        # Display the score
        font = pygame.font.SysFont(None, SCORE_FONT_SIZE)
        score_display = font.render(str(score), True, (0, 0, 0))
        screen.blit(score_display, (WIDTH // 2, 10))

        pygame.display.update()
        clock.tick(30)


game()
pygame.quit()
