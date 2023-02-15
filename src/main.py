import pygame
from UI import UI

pygame.init()

# Set up screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

# Create UI
ui = UI(screen)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state

    # Draw UI
    ui.draw()

    # Update screen
    pygame.display.flip()

pygame.quit()