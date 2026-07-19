import random, math
from circleshape import*
from constants import*
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

        
        self.offsets = [random.uniform(0.7, 1.3) for _ in ASTEROID_BASE_POINTS]
        self.angle = 0.0

    def draw(self, screen: pygame.Surface):
        points = []
        for i, (bx, by) in enumerate(ASTEROID_BASE_POINTS):
            r = self.radius * self.offsets[i]

            x = r * math.cos(self.angle + math.atan2(by, bx))
            y = r * math.sin(self.angle + math.atan2(by, bx))

            points.append((self.position.x + x, self.position.y + y))

        pygame.draw.polygon(screen, "WHITE", points,
                            LINE_WIDTH)

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






