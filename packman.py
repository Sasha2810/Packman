import pygame


class Packman:
    def _init_(self, x, y):
        self.x = x
        self.y = y
        self.is_open_mouth = False
        self.image1 = pygame.image.load('pacman1.png')
        self.image2 = pygame.image.load('pacman2.png')

    def draw(self, screen):
        if not self.is_open_mouth:
            screen.blit(self.image1, (self.x, self.y))
        elif self.is_open_mouth:
            screen.blit(self.image2, (self.x, self.y))

    def move(self, x_move, y_move):
        self.x += x_move
        self.y += y_move
        if not self.is_open_mouth:
            self.is_open_mouth = True
        elif self.is_open_mouth:
            self.is_open_mouth = False


packman = Packman()
