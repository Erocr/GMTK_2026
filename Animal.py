import random
import time
from Vec import Vec
from Specie import Specie


class Animal:
    def __init__(self, pos: Vec, specie: Specie):
        self.pos = pos
        self.specie = specie
        self.start = time.time()
        specie.controller.add_animal(self)
        self.dir = "right"

    def set_pos(self, new_pos):
        """set body parts positions"""

        diff = self.pos - new_pos

        if abs(diff.x) > abs(diff.y):
            if diff.x > 0:
                self.dir = "left"
            else:
                self.dir = "right"
        else:
            if diff.y > 0:
                self.dir = "up"
            else:
                self.dir = "down"

        """décalage des membres inutile normalement"""
        self.pos = new_pos

        # if(self.dir ==  "left"):
        #     # head (oups)
        #     self.list_body_parts["head"].set_x(self.pos_x + 2)
        #     self.list_body_parts["head"].set_y(self.pos_y - 2)

        #     # legs
        #     self.list_body_parts["legs"].set_x(self.pos_x)
        #     self.list_body_parts["legs"].set_y(self.pos_y + 2)

        #     # tail
        #     self.list_body_parts["tail"].set_x(self.pos_x +2)
        #     self.list_body_parts["tail"].set_y(self.pos_y)

        #     # torso
        #     self.list_body_parts["torso"].set_x(self.pos_x)
        #     self.list_body_parts["torso"].set_y(self.pos_y)

        # elif(self.dir == "right"):
        #     # head (oups)
        #     self.list_body_parts["head"].set_x(self.pos_x - 2)
        #     self.list_body_parts["head"].set_y(self.pos_y + 2)

        #     # legs
        #     self.list_body_parts["legs"].set_x(self.pos_x)
        #     self.list_body_parts["legs"].set_y(self.pos_y + 2)

        #     # tail
        #     self.list_body_parts["tail"].set_x(self.pos_x-2)
        #     self.list_body_parts["tail"].set_y(self.pos_y)

        #     # torso
        #     self.list_body_parts["torso"].set_x(self.pos_x)
        #     self.list_body_parts["torso"].set_y(self.pos_y)

        # elif(self.dir == "up"):
        #     # head (oups)
        #     self.list_body_parts["head"].set_x(self.pos_x )
        #     self.list_body_parts["head"].set_y(self.pos_y - 2)

        #     # legs --> rotate ? en dessous ?
        #     self.list_body_parts["legs"].set_x(self.pos_x)
        #     self.list_body_parts["legs"].set_y(self.pos_y)

        #     # tail
        #     self.list_body_parts["tail"].set_x(self.pos_x-2)
        #     self.list_body_parts["tail"].set_y(self.pos_y)

        #     # torso
        #     self.list_body_parts["torso"].set_x(self.pos_x)
        #     self.list_body_parts["torso"].set_y(self.pos_y)

        # elif(self.dir == "down"):
        #     # head (oups)
        #     self.list_body_parts["head"].set_x(self.pos_x - 2)
        #     self.list_body_parts["head"].set_y(self.pos_y + 2)

        #     # legs
        #     self.list_body_parts["legs"].set_x(self.pos_x)
        #     self.list_body_parts["legs"].set_y(self.pos_y + 2)

        #     # tail
        #     self.list_body_parts["tail"].set_x(self.pos_x-2)
        #     self.list_body_parts["tail"].set_y(self.pos_y)

        #     # torso
        #     self.list_body_parts["torso"].set_x(self.pos_x)
        #     self.list_body_parts["torso"].set_y(self.pos_y)
    
    def move(self):
        now = time.time()
        if now - self.start > 60:
            self.start = now
            x_goal = random.randint(0, self.model.SCREEN_LENGTH)
            y_goal = random.randint(0, self.model.SCREEN_WIDTH)
        
            self.go_to(Vec(x_goal, y_goal))
    
    def go_to(self, pos):
        # ràv avec la fonction set_pos pas touche
        dist = self.pos - pos

        # x
        if (dist.x >= 3):
            x_speed = 3
        elif (dist.x > -3):
            x_speed = dist.x
        elif (dist.x < -3):
            x_speed = -3
        # y
        if (dist.y >= 3):
            y_speed = 3
        elif (dist.y > -3):
            y_speed = dist.y
        elif (dist.y < -3):
            y_speed = -3
        
        self.set_pos(self.pos + Vec(x_speed, y_speed))

    def get_dna(self):
        dna = ""
        for body_part in self.specie.list_body_parts:
            dna += self.specie.list_body_parts[body_part].get_dnasec
        return dna
