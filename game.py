import pygame
import sys
from food import Food
from map import Textures
from packman import Packman
from ghost import Ghost

class Game:
    def __init__(self):
        pygame.init()
        self.packman = None
        self.screen = pygame.display.set_mode((720, 720))
        self.food = []
        self.textures = Textures()
        self.ghosts = []
    def parse_map(self):
        x = 0
        y = 0
        map = self.textures.wall
        for i in map:
            for g in i:
                if g == 'P':
                    self.packman = Packman(x, y)

                elif g == 'G':
                    self.ghosts.append(Ghost(x, y))


                elif g == '1':


                elif g == '0':

                x += 40
                y += 40


def fill_food(self):
    for i in range(0, 18):
        for m in range(0, 18):
            self.food.append(Food)


def draw(self):
    self.packman.draw()


def move(self):
    self.packman.move()


def launch(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.check_the_ghost_is_kill_packman():
                pygame.quit()
                sys.exit()

            if event.type == pygame.K_w:
                self.packman.move(0, 10)
            if event.type == pygame.K_s:
                self.packman.move(0, -10)
            if event.type == pygame.K_a:
                self.packman.move(-10, 0)
            if event.type == pygame.K_a:
                self.packman.move(10, 0)


def check_the_ghost_is_kill_packman(self):
    for ghost in ghosts:
        if packman.x == ghost.x and packman.y == ghost.y:
            return True


game = Game()
game.launch()
