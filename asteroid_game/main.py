import pygame
from constants import *
from player import *
pygame.init()
pygclock = pygame.time.Clock()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable,drawable)
player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)


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
            print(f"update {update}")
        screen.fill((0,0,0))
        for draw in drawable:
            draw.draw(screen)
            print(f"draw {draw}")
        print("=================================")
        pygame.display.flip()
       
        
if __name__ == "__main__":
    main()