import pygame
import math

class SkillButton:
    def __init__(self, pos, key, cd=5):
        self.pos = pos
        self.radius = 32
        self.key = key
        self.cd = cd
        self.timer = 0

    def trigger(self):
        if self.timer <= 0:
            self.timer = self.cd * 60
            return True
        return False

    def update(self):
        if self.timer > 0:
            self.timer -= 1

    def draw(self, screen, font):
        pygame.draw.circle(screen, (90,90,120), self.pos, self.radius)
        label = font.render(self.key, True, (255,255,255))
        screen.blit(label, label.get_rect(center=self.pos))

        if self.timer > 0:
            angle = 360 * (self.timer / (self.cd * 60))
            overlay = pygame.Surface((80,80), pygame.SRCALPHA)
            pygame.draw.arc(
                overlay,
                (0,0,0,180),
                (8,8,64,64),
                math.radians(-90),
                math.radians(angle-90),
                8
            )
            screen.blit(overlay, (self.pos[0]-40, self.pos[1]-40))