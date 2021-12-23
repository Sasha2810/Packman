import random
class Food:

    def _init_(self, x, y):
        self.x = x
        self.y = y
    def create_the_food(self):
        self.points = random.randint(5,10)
        self.food_ability = random.choice(['get_points', 'get_speed', 'get_strong', 'get_invisible'])
        self.was_eaten = False



