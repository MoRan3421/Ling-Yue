import pygame
import math
import random

class RankUpgradeAnimation:
    def __init__(self, title, color):
        self.title = title
        self.color = color
        self.timer = 0
        self.duration = 90  # 1.5 秒（60fps）
        self.particles = []

        for _ in range(120):
            a = random.uniform(0, math.pi * 2)
            s = random.uniform(1.5, 4.5)
            self.particles.append((a, s))

    def update(self):
        self.timer += 1

    def done(self):
        return self.timer >= self.duration

    def draw(self, screen, font):
        w, h = screen.get_size()
        cx, cy = w // 2, h // 2
        p = self.timer / self.duration

        # 暗场
        overlay = pygame.Surface((w, h), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, int(180 * p)))
        screen.blit(overlay, (0, 0))

        # 能量环
        for i in range(4):
            r = 90 + i * 14 + math.sin(self.timer * 0.15 + i) * 6
            pygame.draw.circle(screen, self.color, (cx, cy), int(r), 2)

        # 粒子爆发
        for a, s in self.particles:
            d = p * 200 * s
            x = cx + math.cos(a) * d
            y = cy + math.sin(a) * d
            pygame.draw.circle(screen, self.color, (int(x), int(y)), 3)

        # 段位文字
        scale = 1.0 + math.sin(p * math.pi) * 0.25
        txt = font.render(self.title, True, self.color)
        txt = pygame.transform.rotozoom(txt, 0, scale)
        rect = txt.get_rect(center=(cx, cy))
        screen.blit(txt, rect)