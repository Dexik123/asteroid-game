#!/bin/python3

import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
pygame.init()
pygclock = pygame.time.Clock()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updatable,drawable)
Asteroid.containers = (updatable,drawable,asteroids)
AsteroidField.containers = (updatable)
Shot.containers = (updatable,drawable,shots)
player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
asteroidfield = AsteroidField()

def main():

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = pygclock.tick(60) / 1000
        for update in updatable:
            update.update(dt)
            # print(f"update {update}")
        screen.fill((0,0,0))
        for draw in drawable:
            draw.draw(screen)
            # print(f"draw {draw}")
        # print("=================================")
        for aster in asteroids:
            if aster.collision(player):
                print("Game over!")
                return
        for shot in shots:
            for aster in asteroids:
                if shot.collision(aster):
                    shot.kill()
                    aster.split()
        pygame.display.flip()
       
        
if __name__ == "__main__":
    main()
