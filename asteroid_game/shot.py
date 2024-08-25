from constants import *
from circleshape import *



class Shot(CircleShape):
    def __init__(self, position, radius ,velocity):
        super().__init__(position,position, radius)
        self.radius = radius
        self.position = position
        self.velocity = velocity
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self, dt):
        self.position = self.position + self.velocity * dt