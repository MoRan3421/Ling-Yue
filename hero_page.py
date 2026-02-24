# hero_page.py
import pygame

class HeroPage:
    def __init__(self, heroes):
        self.heroes = heroes
        self.selected = 0
        self.scroll = 0

    def handle(self, e):
        if e.type == pygame.MOUSEBUTTONDOWN:
            x, y = e.pos
            if x < 380:
                idx = (y - 100 + self.scroll) // 90
                if 0 <= idx < len(self.heroes):
                    self.selected = idx

        if e.type == pygame.MOUSEWHEEL:
            self.scroll += e.y * 30
            self.scroll = max(0, self.scroll)

    def draw(self, s, font, big_font):
        # 左侧栏
        pygame.draw.rect(s, (20, 30, 70), (0, 80, 380, 570))

        # 英雄卡片
        y = 100 - self.scroll
        for i, h in enumerate(self.heroes):
            rect = pygame.Rect(20, y, 340, 70)
            if i == self.selected:
                pygame.draw.rect(s, (90, 120, 255), rect, border_radius=14)
            else:
                pygame.draw.rect(s, (40, 60, 120), rect, border_radius=14)

            s.blit(font.render(h["name"], 1, (255,255,255)), (40, y+10))
            s.blit(font.render(h["role"], 1, (200,200,255)), (40, y+38))
            y += 90

        # 右侧详情
        hero = self.heroes[self.selected]
        pygame.draw.rect(s, (15,20,45), (400, 100, 840, 500), border_radius=22)

        s.blit(big_font.render(hero["name"],1,(255,255,255)), (440,130))
        s.blit(font.render(f"定位：{hero['role']}",1,(180,200,255)), (440,180))

        # 属性条
        self.draw_bar(s, 440, 240, "生命", hero["hp"], 4000, (120,200,255))
        self.draw_bar(s, 440, 290, "攻击", hero["atk"], 300, (255,180,120))

        # 描述
        desc = "灵约世界的修行英雄，擅长战斗与策略配合。"
        s.blit(font.render(desc,1,(200,200,200)), (440, 360))

    def draw_bar(self, s, x, y, name, val, maxv, color):
        pygame.draw.rect(s, (40,40,60), (x, y, 260, 18), border_radius=9)
        w = int(260 * val / maxv)
        pygame.draw.rect(s, color, (x, y, w, 18), border_radius=9)
        s.blit(
            pygame.font.SysFont("simhei",18).render(f"{name} {val}",1,(255,255,255)),
            (x+270, y-2)
        )