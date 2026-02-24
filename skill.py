import pygame, time, math

class Skill:
    def __init__(self, name, damage, cooldown, radius):
        self.name = name
        self.damage = damage
        self.cooldown = cooldown
        self.radius = radius
        self.last_cast = 0

    def ready(self):
        return time.time() - self.last_cast >= self.cooldown

    def cast(self, caster_pos, enemies):
        if not self.ready(): return
        self.last_cast = time.time()

        for e in enemies:
            if caster_pos.distance_to(e.pos) <= self.radius:
                e.hp -= self.damage