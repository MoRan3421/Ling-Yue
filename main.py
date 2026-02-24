# main.py
import pygame, time
from hero import Hero
from joystick import Joystick
from skill_ui import SkillButton
from moba_map import MobaMap
from minion import spawn_wave

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("灵约 MOBA · 对局")
clock = pygame.time.Clock()
font = pygame.font.SysFont("simhei",20)

hero = Hero((640,360))
joystick = Joystick((140,580))
moba_map = MobaMap()

t0 = time.time()
last_spawn = 0

skills = [
    SkillButton((1080,500),42,"Q",5),
    SkillButton((1160,580),42,"W",8),
    SkillButton((1000,580),42,"E",12),
    SkillButton((1080,650),56,"R",30),
]

minions = []

show_range = 0

def draw_skill_range(s, pos, r):
    surf = pygame.Surface((1280,720), pygame.SRCALPHA)
    pygame.draw.circle(surf,(120,180,255,70),pos,r)
    s.blit(surf,(0,0))

running = True
while running:
    now = time.time() - t0

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running=False

        joystick.handle(e)

        for sk in skills:
            if sk.clicked(e, now):
                show_range = now + 0.5

    # 小兵生成（每 6 秒）
    if now - last_spawn > 6:
        minions += spawn_wave(160, 1)
        minions += spawn_wave(360, 1)
        minions += spawn_wave(560, 1)
        minions += spawn_wave(160, -1)
        minions += spawn_wave(360, -1)
        minions += spawn_wave(560, -1)
        last_spawn = now

    hero.update(joystick.out)

    # 绘制地图
    moba_map.draw(screen)

    # 草丛隐身效果
    if moba_map.in_grass(hero.pos):
        pygame.draw.circle(screen,(100,160,120,120),hero.pos,30)

    # 技能范围
    if now < show_range:
        draw_skill_range(screen, hero.pos, 160)

    # 小兵更新
    for m in minions:
        m.update()
        m.draw(screen)

    hero.draw(screen)
    joystick.draw(screen)

    for sk in skills:
        sk.draw(screen, now, font)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()