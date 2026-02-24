import pygame, math

def draw_rank(surface, rank, t):
    color = (120,160,255) if rank < 4 else (180,120,255) if rank < 9 else (255,200,120)
    r = 60 + int(6 * math.sin(t))
    pygame.draw.circle(surface,color,(640,140),r,5)