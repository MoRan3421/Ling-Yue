import pygame

class GameMap:
    def __init__(self):
        self.width = 1280
        self.height = 720
        # 防御塔、Buff、小水晶位置
        self.towers = [(300,200),(980,200),(300,520),(980,520)]
        self.crystals = [(640,50),(640,670)]
        self.buffs = [(400,360,"red"),(880,360,"blue"),
                      (400,120,"purple"),(880,120,"purple")]
        self.lanes = ["top","mid","bot"]

    def draw(self, screen):
        # 草地
        screen.fill((20,25,40))
        # 绘制红区 / 蓝区
        for bx,by,color in self.buffs:
            if color=="red": pygame.draw.circle(screen,(255,180,220),(bx,by),50)
            if color=="blue": pygame.draw.circle(screen,(160,120,255),(bx,by),50)
            if color=="purple": pygame.draw.circle(screen,(180,150,255),(bx,by),50)
        # 绘制防御塔
        for tx,ty in self.towers:
            pygame.draw.rect(screen,(255,200,100),(tx-15,ty-15,30,30))
        # 绘制小水晶
        for cx,cy in self.crystals:
            pygame.draw.rect(screen,(100,255,255),(cx-20,cy-20,40,40))
        # 绘制三路
        pygame.draw.line(screen,(180,180,180),(100,100),(1180,100),5)
        pygame.draw.line(screen,(180,180,180),(100,360),(1180,360),5)
        pygame.draw.line(screen,(180,180,180),(100,620),(1180,620),5)