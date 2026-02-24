# skill_ui.py
import pygame

class SkillButton:
    def __init__(self, pos, radius, name, cooldown):
        self.pos = pygame.Vector2(pos)
        self.radius = radius
        self.name = name
        self.cooldown = cooldown
        self.last = -999

    def try_use(self, now):
        if now - self.last >= self.cooldown:
            self.last = now
            return True
        return False

    def clicked(self, e, now):
        if e.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Vector2(e.pos).distance_to(self.pos) <= self.radius:
                return self.try_use(now)
        return False

    def draw(self, s, now, font):
        left = max(0, int(self.cooldown - (now - self.last)))

        pygame.draw.circle(s,(50,60,100),self.pos,self.radius)
        pygame.draw.circle(s,(160,200,255),self.pos,self.radius,3)

        if left > 0:
            cover = pygame.Surface((self.radius*2,self.radius*2), pygame.SRCALPHA)
            pygame.draw.circle(cover,(40,40,80,180),(self.radius,self.radius),self.radius)
            s.blit(cover,(self.pos.x-self.radius,self.pos.y-self.radius))
            txt = font.render(str(left),1,(255,255,255))
            s.blit(txt, txt.get_rect(center=self.pos))

        key = font.render(self.name,1,(200,220,255))
        s.blit(key, key.get_rect(center=(self.pos.x,self.pos.y+self.radius+14)))