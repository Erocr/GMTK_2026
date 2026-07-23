import random
from BodyPart import BodyPart
from Model import Model
from View import View

class Animal:
    
    def __init__(self,tete : BodyPart,pattes : BodyPart, torse : BodyPart, x, y):
        self.list_body_parts = {"tete" : tete, "pattes" : pattes, "torse" : torse}
        self.pos_x = x
        self.pos_y = y
    
    def set_body_part(self, part : str, new_part : BodyPart):
        self.list_body_parts.get(part) = new_part

    def set_pos(self,x,y):
        """set body parts positions"""

        self.pos_x = x
        self.pos_y = y

        # head (oups)
        self.list_body_parts.get("tete").set_x(self.pos_x + 2)
        self.list_body_parts.get("tete").set_y(self.pos_y - 2)

        # pattes
        self.list_body_parts.get("pattes").set_x(self.pos_x -1)
        self.list_body_parts.get("pattes").set_y(self.pos_y + 2)

        # torse
        self.list_body_parts.get("torse").set_x(self.pos_x)
        self.list_body_parts.get("torse").set_y(self.pos_y)
    
    def move(self):
        x = random.randint(0,Model.SCREEN_LENGTH)
        y = random.randint(0,Model.SCREEN_WIDTH)
        self.set_pos(x,y)
