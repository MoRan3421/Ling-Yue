# minion.py
import pygame

class Minion:
    def __init__(self, pos, direction):
        self.pos = pygame.Vector2(pos)
        self.dir = direction
        self.speed = 1.4
        self.hp = 100

    def update(self):
        self.pos.x += self.dir * self.speed

    def draw(self, s):
        pygame.draw.circle(s, (180,180,180), self.pos, 10)
        # 血条
        pygame.draw.rect(s,(60,60,60),(self.pos.x-12,self.pos.y-18,24,4))
        pygame.draw.rect(
            s,(120,220,120),
            (self.pos.x-12,self.pos.y-18,24*self.hp/100,4)
        )

def spawn_wave(y, dir):
    return [Minion((50 if dir>0 else 1230, y+i*22), dir) for i in range(3)]