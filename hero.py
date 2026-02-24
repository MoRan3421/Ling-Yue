# hero.py
import pygame

class Hero:
    def __init__(self, pos):
        self.pos = pygame.Vector2(pos)
        self.speed = 4
        self.radius = 22

    def update(self, move):
        self.pos += move * self.speed
        self.pos.x = max(0, min(1280, self.pos.x))
        self.pos.y = max(0, min(720, self.pos.y))

    def draw(self, s):
        pygame.draw.circle(s, (120,180,255), self.pos, self.radius+6)
        pygame.draw.circle(s, (30,30,60), self.pos, self.radius)
        pygame.draw.circle(s, (200,220,255), self.pos, self.radius, 2)