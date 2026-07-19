import sys, pygame, os
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

os.environ["SDL_AUDIODRIVER"] = 'pulseaudio'

def main():
    pygame.init()
    pygame.mixer.init()
    
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (shots, updatable, drawable)

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

        # iterate over asteroids and checks if collision with player.
        for item in asteroids:
            if item.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        # iterates over asteroids and checks if collision with shots.
        for item in asteroids:
            for shot in shots:
                if item.collides_with(shot) == True:
                    log_event("asteroid_shot")
                    shot.kill()
                    item.split()

        
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
