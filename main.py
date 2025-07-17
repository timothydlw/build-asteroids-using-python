import pygame

from constants import *

from player import Player

from asteroid import Asteroid

from asteroidfield import *

updatable = pygame.sprite.Group() #all the objects that can be updated

drawable = pygame.sprite.Group() #all the objects that can be drawn

Player.containers = (updatable, drawable)

def main():
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))

        updatable.update(dt)
        for player in drawable:
            player.draw(screen)
        
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
