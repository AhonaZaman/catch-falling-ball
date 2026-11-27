
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Ball")

# Colors
WHITE = (255, 255, 255)
BLUE = (40, 100, 200)
DARK_BLUE = (20, 40, 90)
GREEN = (50, 180, 100)
YELLOW = (255, 220, 80)

# Fonts
title_font = pygame.font.Font(None, 65)
button_font = pygame.font.Font(None, 40)
text_font = pygame.font.Font(None, 45)

# Game state
game_state = "start"

# Start button
button = pygame.Rect(300, 300, 200, 65)

# Main game loop
running = True

while running:

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "start" and button.collidepoint(mouse_pos):
                game_state = "playing"

        # Enter key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and game_state == "start":
                game_state = "playing"

    # Start Screen
    if game_state == "start":

        screen.fill(DARK_BLUE)

        title = title_font.render(
            "Catch the Falling Ball", True, WHITE
        )

        screen.blit(title, (175, 180))

        # Button hover effect
        if button.collidepoint(mouse_pos):
            button_color = GREEN
        else:
            button_color = BLUE

        pygame.draw.rect(
            screen, button_color, button, border_radius=12
        )

        button_text = button_font.render(
            "START GAME", True, WHITE
        )

        screen.blit(button_text, (325, 317))

        instruction = button_font.render(
            "Click to Start", True, YELLOW
        )

        screen.blit(instruction, (315, 410))

    # Game Started Screen
    elif game_state == "playing":

        screen.fill(DARK_BLUE)

        message = text_font.render(
            "Game Started!", True, GREEN
        )

        screen.blit(message, (290, 260))

    # Update display
    pygame.display.update()

# Quit game
pygame.quit()
sys.exit()
