import pygame
from constants import *

def main ():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # Check if they want to quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Otherwise, render black screen
        screen.fill('black')
        pygame.display.flip()

if __name__ == "__main__":
    main()
