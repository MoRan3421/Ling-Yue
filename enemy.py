import pygame

class Minion:
    def __init__(self,x,y,team):
        self.pos=pygame.Vector2(x,y)
        self.radius=10
        self.hp=200
        self.team=team
        self.speed=2
        self.target=None
    def update(self, heroes, minions):
        if self.team=="blue": self.pos.x+=self.speed
        else: self.pos.x-=self.speed
        enemies=[h for h in heroes if h.color!=self.team]+[m for m in minions if m.team!=self.team]
        if enemies:
            self.target=min(enemies,key=lambda e:self.pos.distance_to(e.pos))
            if self.pos.distance_to(self.target.pos)<=25: self.target.hp-=1
    def draw(self,screen):
        color=(100,200,255) if self.team=="blue" else (255,100,100)
        pygame.draw.circle(screen,color,(int(self.pos.x),int(self.pos.y)),self.radius)
        pygame.draw.rect(screen,(255,0,0),(self.pos.x-10,self.pos.y-20,20,3))
        pygame.draw.rect(screen,(0,255,0),(self.pos.x-10,self.pos.y-20,20*self.hp/200,3))