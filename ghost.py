class Ghost:
    def __init__(self, x, y, steni, ghost_picture):
        self.cell = [x / 40, y / 40]
        self.steni = steni
        self.ghost_picture = ghost_picture

    def move(self):
        if [self.cell[0] + 1, self.cell[1]] in self.steni:
            self.cell[0] += 1
        elif [self.cell[0], self.cell[1] + 1] in self.steni:
            self.cell[1] += 1
        elif [self.cell[0] - 1, self.cell[1]] in self.steni:
            self.cell[0] -= 1
        else:
            self.cell[1] -= 1

    def draw(self, screen):
        screen.blit(self.ghost_picture, (self.cell[0] * 40, self.cell[1] * 40))
