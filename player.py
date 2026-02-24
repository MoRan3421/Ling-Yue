import pygame

class Player:
    def __init__(self, pos=(480,270)):
        self.pos = pygame.Vector2(pos)
        self.speed = 4

    def update(self, direction):
        self.pos += direction * self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, (120,200,255), self.pos, 18)