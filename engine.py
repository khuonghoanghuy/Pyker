import pygame

def isMouseOverlaps(left, top, width, height, pos):
    rectthing = pygame.Rect(left, top, width, height)
    return rectthing.collidepoint(pos)