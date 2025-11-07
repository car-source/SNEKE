import pygame, random

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(size)
pygame.display.set_caption("~~SNEKE~~")

# Set FSP and clock
# TODO: make a variable (constant) called FPS and initialize to 20
clock = pygame.time.Clock()

# Set game values
# TODO: make a variable (constant) named SNAKE_SIZE and initialize to 20

# TODO: make a variable named head_x and assign half of the window_width to it. use integer divison // (i.e. 11 / 2 is 5.5, 11//2 is 5)
# TODO: make a variable named head_y and assign half of the window_height + 100 to it. use integer divison //

# TODO: make a variable named snake_dx and assign 0 to it
# TODO: repeat for a variable named snake_dy

# TODO: repeat for a variable named score and assign 0 to it.

# Set colors
GREEN = (0, 255, 0) # (r, g, b)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
DARKRED = (150, 0, 0)
WHITE = (255, 255, 255)


# Set fonts

# Set text

# Set sounds and music

# Set images (in this case, use simple rects...so just create their coordinates)
# For a rectangle you need (top-left x, top-left y, width, height)

# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the snake

    # Add the head coordinate to the first index of the body coordinate list
    # This will essentially move all the snakes body by one position in the list

    # Update the x,y position of the snakes head and make a new coordinate

    # Check for game over

    # Check for collisions

    # Update HUD

    # Fill the surface

    # Blit HUD

    # Blit assets

    # Update display and tick clock

# End the game
pygame.quit()
