# app_ui.py
import pygame, math

class AppUI:
    def __init__(self):
        self.time = 0
        self.tabs = ["首页", "英雄", "装备", "排位", "活动"]
        self.active_tab = 0

    def draw_bg(self, s):
        s.fill((12, 16, 36))
        for i in range(40):
            x = (i * 97) % 1280
            y = (i * 53) % 720
            pygame.draw.circle(s, (25, 40, 90), (x, y), 2)

    def draw_top_bar(self, s, font, rank_name):
        pygame.draw.rect(s, (20,25,60), (0,0,1280,80))
        pygame.draw.circle(s, (120,180,255), (60,40), 22)  # 头像位
        s.blit(font.render("LingYue玩家",1,(255,255,255)),(100,22))
        s.blit(font.render(rank_name,1,(180,200,255)),(260,22))
        s.blit(font.render("💎 8888",1,(255,220,120)),(1100,22))

    def draw_match_button(self, s, font):
        self.time += 0.05
        pulse = int(6 * math.sin(self.time))
        rect = pygame.Rect(440-pulse, 360-pulse, 400+2*pulse, 90+2*pulse)

        pygame.draw.rect(s, (80,100,255), rect, border_radius=26)
        pygame.draw.rect(s, (200,220,255), rect, 3, border_radius=26)

        txt = font.render("开始匹配",1,(255,255,255))
        s.blit(txt, txt.get_rect(center=rect.center))

        return rect

    def draw_tabs(self, s, font):
        pygame.draw.rect(s, (20,25,60), (0,650,1280,70))
        for i,name in enumerate(self.tabs):
            x = 1280//5*i + 128
            color = (200,220,255) if i==self.active_tab else (140,160,200)
            s.blit(font.render(name,1,color),(x-20,670))

    def handle_tab_click(self, e):
        if e.type == pygame.MOUSEBUTTONDOWN and e.pos[1] > 650:
            self.active_tab = e.pos[0] // (1280//5)