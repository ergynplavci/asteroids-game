import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    field = AsteroidField()
    
    print("""Starting Asteroids!
            Screen width: 1280
            Screen height: 720""")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = (clock.tick(60) / 1000.0)
        updatable.update(dt)
        screen.fill((0, 0, 0))
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                sys.exit()
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()



if __name__ == "__main__":
    main()
