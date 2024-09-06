import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main ():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Instantiate a player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    player = Player(x, y)
    AsteroidField()

    while True:
        # Check if they want to quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Check for player rotations
        for object in updatable:
            object.update(dt)

        # Check for game over state
        for object in asteroids:
            if object.isCollision(player):
                print("Game over!")
                exit()

        # Check if an bullet hit an asteroid
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.isCollision(bullet):
                    asteroid.split()
                    bullet.kill()
            
        # Draw black screen and player
        screen.fill('black')
        for object in drawable:
            object.draw(screen)

        # Then render (THIS MUST BE LAST)
        pygame.display.flip()
        # Update the clock
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
