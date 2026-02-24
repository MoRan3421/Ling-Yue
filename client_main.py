import pygame, sys, random, math
from pygame.math import Vector2

# ------------------------------
# 基础类
# ------------------------------
class Particle:
    def __init__(self, x, y, dx, dy, color, lifetime):
        self.pos = Vector2(x, y)
        self.vel = Vector2(dx, dy)
        self.color = color
        self.life = lifetime
        self.radius = random.randint(2,5)
    def update(self):
        self.pos += self.vel
        self.life -= 1
        self.vel *= 0.95
        self.radius *= 0.98
    def draw(self, screen):
        if self.life>0:
            fade = max(0,min(255,int(255*self.life/60)))
            c = (self.color[0], self.color[1], fade)
            pygame.draw.circle(screen, c, (int(self.pos.x), int(self.pos.y)), int(self.radius))

class Skill:
    def __init__(self, caster, radius=50, dmg=50, color=(255,200,50)):
        self.caster = caster
        self.radius = radius
        self.dmg = dmg
        self.color = color
        self.cd = 120
        self.cooldown = 0
    def update(self):
        if self.cooldown>0:
            self.cooldown -= 1
    def can_cast(self):
        return self.cooldown <= 0
    def cast(self, targets, particle_list):
        self.cooldown = self.cd
        for t in targets:
            if t.pos.distance_to(self.caster.pos) < self.radius:
                t.hp -= self.dmg
        # 粒子效果
        for _ in range(20):
            dx, dy = random.uniform(-3,3), random.uniform(-3,3)
            particle_list.append(Particle(self.caster.pos.x, self.caster.pos.y, dx, dy, self.color, 60))

class Hero:
    def __init__(self, color=(255,255,0)):
        self.pos = Vector2(200, 320)
        self.radius = 20
        self.color = color
        self.hp = 1000
        self.buffs = []
        self.skill_particles = []
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,180), (int(self.pos.x), int(self.pos.y)), self.radius+5, 3)
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)
        pygame.draw.rect(screen, (255,0,0), (self.pos.x-25, self.pos.y-35, 50, 5))
        pygame.draw.rect(screen, (0,255,0), (self.pos.x-25, self.pos.y-35, 50*self.hp/1000, 5))
        for i, b in enumerate(self.buffs):
            pygame.draw.circle(screen, (255,255,0), (int(self.pos.x-20+i*12), int(self.pos.y-45)), 5)
        for p in self.skill_particles:
            p.draw(screen)

class Minion:
    def __init__(self, x, y, color):
        self.pos = Vector2(x, y)
        self.radius = 12
        self.color = (0,0,255) if color=="blue" else (255,0,0)
        self.hp = 200
        self.speed = 2
        self.target = Vector2(950 if color=="blue" else 50, y)
    def update(self, heroes, others):
        dir = (self.target - self.pos).normalize() if self.target != self.pos else Vector2(0,0)
        self.pos += dir*self.speed
        # 攻击英雄
        for h in heroes:
            if self.pos.distance_to(h.pos) < self.radius + h.radius:
                h.hp -= 0.5
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)
        pygame.draw.rect(screen, (255,0,0), (self.pos.x-15, self.pos.y-20, 30, 3))
        pygame.draw.rect(screen, (0,255,0), (self.pos.x-15, self.pos.y-20, 30*self.hp/200, 3))

class GameMap:
    def __init__(self, width=1000, height=700):
        self.width = width
        self.height = height
        self.lanes = [140,320,500]
        self.river_rect = pygame.Rect(0,280,width,140)
    def draw(self, screen):
        # 草地
        screen.fill((80,180,80))
        pygame.draw.rect(screen, (50,150,200), self.river_rect)
        for i in range(0,self.width,20):
            offset = int(5*math.sin(pygame.time.get_ticks()/500 + i/50))
            pygame.draw.circle(screen,(180,220,255),(i,350+offset),3)
        for y in self.lanes:
            pygame.draw.line(screen,(150,150,150),(0,y),(self.width,y),5)
            pygame.draw.circle(screen,(0,200,255),(100,y),30,5)
            pygame.draw.circle(screen,(255,50,50),(900,y),30,5)
        pygame.draw.circle(screen,(0,255,255),(50,320),60,5)
        pygame.draw.circle(screen,(255,100,100),(950,320),60,5)

class SkillButton:
    def __init__(self,x,y,skill):
        self.pos = Vector2(x,y)
        self.skill = skill
        self.radius = 35
    def draw(self,screen):
        pygame.draw.circle(screen,(30,30,30),(self.pos.x+3,self.pos.y+3),self.radius)
        pygame.draw.circle(screen,(50,50,50),self.pos,self.radius)
        if self.skill.cooldown>0:
            angle = int(360*self.skill.cooldown/self.skill.cd)
            pygame.draw.arc(screen,(100,150,255),(self.pos.x-self.radius,self.pos.y-self.radius,self.radius*2,self.radius*2),0,math.radians(angle),5)
    def check_click(self,pos):
        if Vector2(pos).distance_to(self.pos)<=self.radius:
            if self.skill.can_cast():
                self.skill.cast([hero], particles)

# ------------------------------
# 初始化 Pygame
# ------------------------------
WIDTH, HEIGHT = 1000, 700
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60

# ------------------------------
# 游戏对象
# ------------------------------
game_map = GameMap()
hero = Hero()
minions=[]
for lane in game_map.lanes:
    for i in range(3):
        minions.append(Minion(50+i*60,lane,"blue"))
        minions.append(Minion(950-i*60,lane,"red"))

skills = [Skill(hero), Skill(hero, radius=100, dmg=80, color=(100,255,100))]
particles = []
skill_buttons = [SkillButton(WIDTH-100, HEIGHT-100, s) for s in skills]

# ------------------------------
# 主循环
# ------------------------------
running = True
while running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            for btn in skill_buttons:
                btn.check_click(event.pos)

    # 英雄移动
    keys = pygame.key.get_pressed()
    move = Vector2(0,0)
    if keys[pygame.K_w]: move.y-=4
    if keys[pygame.K_s]: move.y+=4
    if keys[pygame.K_a]: move.x-=4
    if keys[pygame.K_d]: move.x+=4
    hero.pos += move

    # 更新技能
    for s in skills: s.update()
    for p in particles: p.update()
    particles = [p for p in particles if p.life>0]

    # 更新小兵
    for m in minions: m.update([hero], minions)

    # 绘制
    game_map.draw(screen)
    for m in minions: m.draw(screen)
    hero.draw(screen)
    for btn in skill_buttons: btn.draw(screen)
    for p in particles: p.draw(screen)
    pygame.display.flip()