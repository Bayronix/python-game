import pygame

from settings import WIDTH, HEIGHT, FPS, BLACK
from entities.player import Player
from world.level import Level

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

level = Level()
player = Player(100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(level.platforms)

    screen.fill(BLACK)
    level.draw(screen)
    player.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
