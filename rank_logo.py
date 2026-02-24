# rank_logo.py
import pygame, math

class RankLogo:
    def __init__(self):
        self.anim = 0
        self.upgrade_fx = 0

    def trigger_upgrade(self):
        self.upgrade_fx = 60

    def draw(self, screen, rank):
        self.anim += 0.05
        cx, cy = 640, 260

        # 根据段位决定颜色
        if rank < 4:
            core = (160, 200, 255)
        elif rank < 9:
            core = (200, 160, 255)
        else:
            core = (255, 200, 120)

        pulse = int(8 * math.sin(self.anim))
        pygame.draw.circle(screen, core, (cx, cy), 70 + pulse)

        pygame.draw.circle(screen, (30, 30, 50), (cx, cy), 55)
        pygame.draw.circle(screen, core, (cx, cy), 55, 4)

        # 升段特效
        if self.upgrade_fx > 0:
            r = 90 + (60 - self.upgrade_fx) * 2
            pygame.draw.circle(screen, (255,255,255), (cx,cy), r, 3)
            self.upgrade_fx -= 1

import pygame, math

def draw_rank(surface, rank, t):
    color = (120,160,255) if rank < 4 else (180,120,255) if rank < 9 else (255,200,120)
    r = 60 + int(6 * math.sin(t))
    pygame.draw.circle(surface,color,(640,140),r,5)