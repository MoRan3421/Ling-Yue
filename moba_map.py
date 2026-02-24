# map_moba.py
import pygame

LANE_COLOR = (60, 80, 120)
GRASS_COLOR = (30, 90, 60)
RED_BUFF = (200, 80, 120)     # 粉红偏紫
BLUE_BUFF = (80, 120, 200)    # 蓝紫

class MobaMap:
    def __init__(self):
        self.top_lane = pygame.Rect(0, 120, 1280, 80)
        self.mid_lane = pygame.Rect(0, 320, 1280, 80)
        self.bot_lane = pygame.Rect(0, 520, 1280, 80)

        self.grasses = [
            pygame.Rect(200, 200, 120, 80),
            pygame.Rect(900, 400, 120, 80),
        ]

        self.red_buff = pygame.Rect(300, 360, 80, 80)
        self.blue_buff = pygame.Rect(900, 160, 80, 80)

    def draw(self, s):
        # 地面
        s.fill((20, 26, 50))

        # 三路
        pygame.draw.rect(s, LANE_COLOR, self.top_lane)
        pygame.draw.rect(s, LANE_COLOR, self.mid_lane)
        pygame.draw.rect(s, LANE_COLOR, self.bot_lane)

        # 草丛
        for g in self.grasses:
            pygame.draw.rect(s, GRASS_COLOR, g)

        # Buff 区
        pygame.draw.ellipse(s, RED_BUFF, self.red_buff)
        pygame.draw.ellipse(s, BLUE_BUFF, self.blue_buff)

    def in_grass(self, pos):
        return any(g.collidepoint(pos) for g in self.grasses)