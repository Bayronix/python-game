import pygame
from settings import GREEN


class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect)


class Level:
    def __init__(self):
        self.platforms = [
            Platform(0, 650, 1280, 70),
        ]

    def draw(self, screen):
        for platform in self.platforms:
            platform.draw(screen)
