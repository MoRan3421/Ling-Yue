import pygame

class Base:
    def __init__(self, x, y, team):
        self.pos = pygame.Vector2(x, y)
        self.hp = 3000
        self.team = team

    def draw(self, screen):
        color = (90,180,255) if self.team == "blue" else (255,80,80)
        pygame.draw.circle(screen, color, self.pos, 40)
        pygame.draw.circle(screen, (255,255,255), self.pos, 40, 3)