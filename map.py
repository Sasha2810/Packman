import pygame
import sys


class Textures:
    def __init__(self):
        self.pol = pygame.image.load("m_pol.jpg")
        self.stena = pygame.image.load("m_stena.png")
        self.pacman = pygame.image.load('m_pacman.png')
        self.eat = pygame.image.load('m_eat.png')
        self.boost = pygame.image.load('m_boost.png')
        self.wall = ["888888888888888888",
                            "880808888888808088",
                            "80000000P000000008",
                            "880888008800888088",
                            "88000001880G000088",
                            "888808888888808888",
                            "800000000000000008",
                            "888808888888808888",
                            "8800G8000000800088",
                            "880808888888808088",
                            "800800000000008008",
                            "888888008800888888",
                            "800000008800000008",
                            "808801888888008808",
                            "800000000000000008",
                            "888088808808880888",
                            "888080008800080888",
                            "888888888888888888"]

    def draw(self, screen):
        x = 0
        y = 0
        for i in self.wall:
            for g in i:
                if g == "8":
                    screen.blit(self.stena, (x, y))
                elif g == 'P':
                    screen.blit(self.pacman, (x, y))
                elif g == 'G':
                    screen.blit(self.eat, (x, y))
                elif g == '1':
                    screen.blit(self.boost, (x, y))
                elif g == '0':
                    screen.blit(self.pol, (x, y))
                x += 40
            y += 40


