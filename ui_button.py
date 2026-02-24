import pygame

class UIButton:
    def __init__(self, rect, text, font, bg, fg):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.bg = bg
        self.fg = fg

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg, self.rect, border_radius=14)
        label = self.font.render(self.text, True, self.fg)
        screen.blit(
            label,
            label.get_rect(center=self.rect.center)
        )

    def clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and self.rect.collidepoint(event.pos)
        )