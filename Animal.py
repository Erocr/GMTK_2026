import random
import time
from Vec import Vec, dist
from Specie import Specie


class Animal:
    LEG_ANIM_FRAME_DURATION = 0.1

    def __init__(self, pos: Vec, specie: Specie):
        self.pos = pos
        self.goal_pos = self.pos
        self.specie = specie
        self.list_body_parts = {"head": specie.list_body_parts["head"], "legs": specie.list_body_parts["legs"], "torso": specie.list_body_parts["torso"], "tail": specie.list_body_parts["tail"]}
        self.startMovementTime = time.time()  # Commence en bougeant
        self.nextDirectionChoseTime = time.time()
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

    def is_moving(self):
        return dist(self.pos, self.goal_pos) > 1

    def change_direction(self):
        now = time.time()
        if now > self.nextDirectionChoseTime:
            self.startMovementTime = now
            self.nextDirectionChoseTime = now + random.randint(3, 8)
            x_goal = random.randint(0, self.specie.model.SCREEN_SIZE.x - 743)  # 743 is the width of an animal
            y_goal = random.randint(0, self.specie.model.SCREEN_SIZE.y - 458)  # 458 is the height of an animal

            self.goal_pos = Vec(x_goal, y_goal)
    
    def move(self):
        dist = self.goal_pos - self.pos
        max_speed = Vec(self.specie.model.SCREEN_SIZE.x*0.002,self.specie.model.SCREEN_SIZE.y*0.002)

        # x
        if dist.x >= max_speed.x:
            x_speed = max_speed.x
        elif dist.x > -max_speed.x:
            x_speed = dist.x
        elif dist.x <= -max_speed.x:
            x_speed = -max_speed.x
        # y
        if dist.y >= max_speed.y:
            y_speed = max_speed.y
        elif dist.y > -max_speed.y:
            y_speed = dist.y
        elif dist.y <= -max_speed.y:
            y_speed = -max_speed.y
        
        self.set_pos(self.pos + Vec(x_speed, y_speed)) 

    def get_dna(self):
        dna = ""
        for body_part in self.specie.list_body_parts:
            dna += self.specie.list_body_parts[body_part].getdna()
        return dna
