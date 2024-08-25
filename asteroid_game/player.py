import pygame
from circleshape import *
from constants import *
from shot import *
class Player (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.position = pygame.Vector2(x,y)
        self.rotation = 0
        self.cooldown = 0
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]  
    def shoot(self):
        if self.cooldown > 0:
            return None
        velocity = pygame.Vector2(0,1)
        velocity = velocity.rotate(self.rotation)
        velocity = velocity * PLAYER_SHOT_SPEED
        shot = Shot(self.position,SHOT_RADIUS,velocity)
        self.cooldown = PLAYER_SHOOT_COOLDOWN
        # print("shooting")
    def draw (self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
    def rotate(self,dt):
        self.rotation = self.rotation + PLAYER_TURN_SPEED * dt
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown = self.cooldown - dt
        if keys[pygame.K_a]:
            self.rotate(dt)    
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)    
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            # print("shoot")
            self.shoot()