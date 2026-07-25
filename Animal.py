import random
import time
from Vec import Vec
from Specie import Specie



class Animal:
    def __init__(self, pos: Vec, specie: Specie):
        self.pos = pos
        self.goal_pos = self.pos
        self.specie = specie
        self.start = time.time() - 60  # Commence instant en bougeant
        self.dir = "right"

    def set_pos(self, new_pos):
        """set body parts positions"""

        diff = self.pos - new_pos

        if diff.x > 0:
            self.dir = "left"
        else:
            self.dir = "right"

        """
        décalage des membres inutile normalement
        On peut le retrouver dans les anciens commits sur git
        """
        self.pos = new_pos

    def update(self):
        self.change_direction()
        self.move()

    def change_direction(self):
        now = time.time()
        if now - self.start > 60:
            self.start = now + random.randint(0, 30)
            x_goal = random.randint(0, self.specie.model.SCREEN_SIZE.x - 743)  # 743 is the width of an animal
            y_goal = random.randint(0, self.specie.model.SCREEN_SIZE.y - 458)  # 458 is the height of an animal

            self.goal_pos = Vec(x_goal, y_goal)
    
    def move(self):
        dist = self.goal_pos - self.pos

        # x
        if dist.x >= 3:
            x_speed = 3
        elif dist.x > -3:
            x_speed = dist.x
        elif dist.x <= -3:
            x_speed = -3
        # y
        if dist.y >= 3:
            y_speed = 3
        elif dist.y > -3:
            y_speed = dist.y
        elif dist.y <= -3:
            y_speed = -3
        
        self.set_pos(self.pos + Vec(x_speed, y_speed))

    def get_dna(self):
        dna = ""
        for body_part in self.specie.list_body_parts:
            dna += self.specie.list_body_parts[body_part].get_dnasec
        return dna
