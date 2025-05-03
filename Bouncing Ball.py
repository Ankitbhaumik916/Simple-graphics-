import pygame
import random

# Initialize
pygame.init()
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Ball settings
x, y = width // 2, height // 2
radius = 20
dx, dy = 5, 4
color = (255, 0, 0)

running = True
while running:
    screen.fill((30, 30, 30))

    # Ball movement
    x += dx
    y += dy

    # Bounce
    if x <= radius or x >= width - radius:
        dx = -dx
        color = [random.randint(50, 255) for _ in range(3)]
    if y <= radius or y >= height - radius:
        dy = -dy
        color = [random.randint(50, 255) for _ in range(3)]

    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
