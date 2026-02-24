# joystick.py
import pygame

class Joystick:
    def __init__(self, center):
        self.center = pygame.Vector2(center)
        self.knob = self.center
        self.radius = 60
        self.active = False
        self.out = pygame.Vector2()

    def handle(self, e):
        if e.type == pygame.MOUSEBUTTONDOWN:
            if self.center.distance_to(e.pos) <= self.radius:
                self.active = True

        if e.type == pygame.MOUSEBUTTONUP:
            self.active = False
            self.knob = self.center
            self.out = pygame.Vector2()

        if e.type == pygame.MOUSEMOTION and self.active:
            d = pygame.Vector2(e.pos) - self.center
            if d.length() > self.radius:
                d.scale_to_length(self.radius)
            self.knob = self.center + d
            self.out = d / self.radius

    def draw(self, s):
        pygame.draw.circle(s,(40,60,120),self.center,self.radius,3)
        pygame.draw.circle(s,(160,200,255),self.knob,22)