import pygame
from settings import GRAVITY, PLAYER_SPEED, JUMP_STRENGTH, WHITE


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 60)
        self.velocity_y = 0
        self.on_ground = False

    def update(self, platforms):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += PLAYER_SPEED
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.velocity_y = JUMP_STRENGTH

        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y
        self.on_ground = False

        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.velocity_y >= 0:
                self.rect.bottom = platform.rect.top
                self.velocity_y = 0
                self.on_ground = True

    def draw(self, screen):
        x, y, w, h = self.rect

        head_radius = w // 2
        head_center = (x + w // 2, y + head_radius)
        pygame.draw.circle(screen, WHITE, head_center, head_radius)

        torso_rect = pygame.Rect(x + w // 4, y + head_radius * 2, w // 2, h // 2)
        pygame.draw.rect(screen, WHITE, torso_rect)

        leg_width = w // 5
        leg_height = h - torso_rect.height - head_radius * 2
        leg_y = torso_rect.bottom
        pygame.draw.rect(screen, WHITE, (x + w // 4, leg_y, leg_width, leg_height))
        pygame.draw.rect(screen, WHITE, (x + w - w // 4 - leg_width, leg_y, leg_width, leg_height))
