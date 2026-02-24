import pygame, math, random
from rank_system import RANKS

class RankPage:
    def __init__(self, rank_system):
        self.rs = rank_system
        self.t = 0
        self.particles = []

    def update(self):
        self.t += 0.05
        if random.random() < 0.2:
            self.particles.append([
                640, 360,
                random.uniform(-1,1),
                random.uniform(-1,1),
                random.randint(2,4)
            ])

        for p in self.particles:
            p[0] += p[2]
            p[1] += p[3]
            p[4] -= 0.1
        self.particles = [p for p in self.particles if p[4] > 0]

    def draw(self, screen, font):
        screen.fill((18,22,35))

        # 发光段位圆
        glow = 90 + math.sin(self.t) * 10
        pygame.draw.circle(
            screen,
            (120,180,255),
            (640,360),
            int(glow),
            4
        )

        # 段位文字
        text = font.render(
            self.rs.rank_text(),
            True,
            (240,240,255)
        )
        screen.blit(text, text.get_rect(center=(640,220)))

        # 粒子
        for p in self.particles:
            pygame.draw.circle(
                screen,
                (200,220,255),
                (int(p[0]), int(p[1])),
                int(p[4])
            )