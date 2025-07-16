import pygame

from constants import *

from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))

        
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
