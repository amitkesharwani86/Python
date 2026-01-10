import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Circle Movement")
clock = pygame.time.Clock()

# Game variables
running = True
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_speed = 300  # pixels per second

# Game loop
while running:
    dt = clock.tick(60) / 1000  # Delta time in seconds

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= player_speed * dt
    if keys[pygame.K_s]:
        player_pos.y += player_speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= player_speed * dt
    if keys[pygame.K_d]:
        player_pos.x += player_speed * dt

    # Drawing
    screen.fill("purple")
    pygame.draw.circle(screen, "red", (int(player_pos.x), int(player_pos.y)), 40)
    pygame.display.flip()

# Clean up
pygame.quit()
