import pygame
from pygame.math import Vector2

class Tower:
    def __init__(self, x, y, team):
        self.pos = Vector2(x, y)
        self.team = team
        self.hp = 1500
        self.range = 180
        self.damage = 30

    def draw(self, screen):
        color = (255, 120, 180) if self.team == "red" else (120, 180, 255)
        pygame.draw.rect(screen, color, (*self.pos, 30, 30))
        # 血条
        pygame.draw.rect(screen, (0,0,0), (self.pos.x, self.pos.y-8, 30, 5))
        pygame.draw.rect(
            screen,
            (0,255,0),
            (self.pos.x, self.pos.y-8, 30 * (self.hp/1500), 5)
        )