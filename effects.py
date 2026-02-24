from random import random

import pygame

class FireEffect:
    def __init__(self, pos):
        self.pos = pos
        self.life = 30
        self.img = pygame.image.load("assets/effects/fire.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, (32, 32))

    def update(self):
        self.life -= 1

    def draw(self, screen):
        screen.blit(self.img, self.pos)

class Particle:
    def __init__(self, x, y, dx, dy, color, lifetime):
        self.pos = pygame.Vector2(x,y)
        self.vel = pygame.Vector2(dx,dy)
        self.color = color
        self.life = lifetime
        self.radius = random.randint(2,5)

    def update(self):
        self.pos += self.vel
        self.life -= 1
        self.vel *= 0.95  # 阻力减速
        self.radius *= 0.98

    def draw(self, screen):
        if self.life>0:
            # 渐变色效果
            fade = max(0,min(255,int(255*self.life/60)))
            c = (self.color[0], self.color[1], fade)
            pygame.draw.circle(screen, c, (int(self.pos.x), int(self.pos.y)), int(self.radius))