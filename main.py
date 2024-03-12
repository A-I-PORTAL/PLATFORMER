import pygame
import player
import level

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set game title
pygame.display.set_caption("My Platformer Game")

# Load background image (replace with your image filename)
background_image = pygame.image.load("background.png")

# Create player object
player_object = player.Player(screen_width, screen_height)

# Create level object
current_level = level.Level(screen_width, screen_height)

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game objects
    player_object.update()
    current_level.update(player_object)

    # Draw game elements
    screen.blit(background_image, (0, 0))
    current_level.draw(screen)
    player_object.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
