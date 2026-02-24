import pygame

def bg(s):
    s.fill((15,18,40))
    for i in range(40):
        pygame.draw.circle(s,(30,50,90),(i*32%1280,i*71%720),2)

class Button:
    def __init__(self, r, t):
        self.r = pygame.Rect(r)
        self.t = t

    def draw(self,s,f):
        pygame.draw.rect(s,(40,40,80),self.r,0,12)
        txt=f.render(self.t,1,(255,255,255))
        s.blit(txt,txt.get_rect(center=self.r.center))

    def click(self,e):
        return e.type==pygame.MOUSEBUTTONDOWN and self.r.collidepoint(e.pos)