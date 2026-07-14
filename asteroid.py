import random
from circleshape import*
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "WHITE", self.position,
                           self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        
        asteroid_a = Asteroid(self.position.x, self.position.y, self.radius / 2)
        asteroid_b = Asteroid(self.position.x, self.position.y, self.radius / 2)

        asteroid_a.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.2
        asteroid_b.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle) * 1.2






