import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid = AsteroidField() 

    while True:
        log_state()   # log events. 

        # quits the game when the x is pressed.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fills the background color    
        screen.fill("BLACK")

        # updates all items in updatable group
        updatable.update(dt)
        
        # used to draw each item in the drawable group
        for item in drawable:
            item.draw(screen)

        # updates the screen
        pygame.display.flip()

        # sets delta time.
        dt = clock.tick(60) / 1000
        
    pygame.QUIT

if __name__ == "__main__":
    main()
