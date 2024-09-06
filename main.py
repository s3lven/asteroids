import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from scoreboard import *

def main ():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    AsteroidField()
    scoreboard = Scoreboard()

    while True:
        # Check if they want to quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        # Check for object updates
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
                    scoreboard.update_score(1)
                    asteroid.split()
                    bullet.kill()
            
        # Draw black screen
        screen.fill('black')
        # Render text AFTER rendering black screen
        scoreboard.render(screen)

        # Render all drawables
        for object in drawable:
            object.draw(screen)

        # Then render (THIS MUST BE LAST)
        pygame.display.flip()
        # Update the clock
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
