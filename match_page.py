import pygame
from ui_button import UIButton

class MatchPage:
    def __init__(self):
        self.matching = False
        self.btn = UIButton((360,260,240,60), "开始匹配")

    def draw(self, screen, font):
        screen.fill((22,25,40))
        if not self.matching:
            self.btn.draw(screen, font)
        else:
            txt = font.render("匹配中...", True, (180,220,255))
            screen.blit(txt, txt.get_rect(center=(480,270)))

    def handle(self, e):
        if self.btn.clicked(e):
            self.matching = True