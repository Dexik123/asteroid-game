from circleshape import *
from constants import *
import random
class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.position = pygame.Vector2(x,y)
        self.velocity = 0
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self, dt):
        self.position = self.position + self.velocity * dt
    def split (self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None
        angle = int(random.uniform(20,50))
        asteroid_1_trajectory = self.velocity.rotate(angle)
        asteroid_2_trajectory = self.velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position,self.position,radius)
        asteroid_1.velocity = asteroid_1_trajectory * 1.2
        asteroid_2 = Asteroid(self.position,self.position,radius)
        asteroid_2.velocity = asteroid_2_trajectory * 1.2