import pygame

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first game")

x, y = WIDTH / 2, HEIGHT / 2
radius = 10
step = 10
fps = 120

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    
    if (pressed[pygame.K_w] or pressed[pygame.K_UP]) and y - radius > 0:
        y -= step
    if (pressed[pygame.K_s] or pressed[pygame.K_DOWN]) and y + radius < HEIGHT:
        y += step
    if (pressed[pygame.K_a] or pressed[pygame.K_LEFT]) and x - radius > 0:
        x -= step
    if (pressed[pygame.K_d] or pressed[pygame.K_RIGHT]) and x + radius < WIDTH:
        x += step
    if pressed[pygame.K_q]:
        running = False

    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.display.flip()

    clock.tick(fps)

pygame.quit()