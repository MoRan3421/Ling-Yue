import pygame
import math

class MatchResult:
    def __init__(self, win=True, mvp=True):
        self.win = win
        self.mvp = mvp
        self.timer = 0
        self.duration = 120  # 2 秒
        self.done = False

    def update(self):
        self.timer += 1
        if self.timer >= self.duration:
            self.done = True

    def draw(self, screen, font):
        w, h = screen.get_size()
        cx, cy = w // 2, h // 2
        p = min(1.0, self.timer / 30)

        # 半透明背景
        overlay = pygame.Surface((w, h), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        screen.blit(overlay, (0, 0))

        # 胜负标题
        title_text = "胜 利" if self.win else "失 败"
        title_color = (120, 220, 120) if self.win else (220, 100, 100)
        title = font.render(title_text, True, title_color)
        title = pygame.transform.rotozoom(title, 0, 1 + math.sin(self.timer*0.1)*0.05)
        screen.blit(title, title.get_rect(center=(cx, cy - 80)))

        # MVP 光环
        if self.mvp:
            glow = 50 + math.sin(self.timer * 0.15) * 6
            pygame.draw.circle(screen, (255, 220, 120), (cx, cy), int(glow), 3)
            mvp = font.render("MVP", True, (255, 220, 120))
            screen.blit(mvp, mvp.get_rect(center=(cx, cy)))

        # 提示
        tip = font.render("正在结算段位...", True, (200,200,200))
        screen.blit(tip, tip.get_rect(center=(cx, cy + 80)))