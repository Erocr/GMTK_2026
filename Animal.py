import random
import time
from BodyPart import BodyPart
from Model import Model
from View import View

class Animal:
    
    def __init__(self, head : BodyPart,legs : BodyPart, torso : BodyPart, tail : BodyPart, x, y):
        self.list_body_parts = {"head" : head, "legs" : legs, "torso" : torso, "tail" : tail}
        self.pos_x = x
        self.pos_y = y
        self.dir = "left"
        self.start = time.time()
    
    def set_body_part(self, part : str, new_part : BodyPart):
        self.list_body_parts.get(part) = new_part

    def set_pos(self,x,y):
        """set body parts positions"""

        diff_x = self.pos_x - x
        diff_y = self.pos_y - y

        if(abs(diff_x) > abs(diff_y)):
            if(diff_x>0):
                self.dir = "left"
            else:
                self.dir = "right"
        else:
            if(diff_y>0):
                self.dir = "up"
            else:
                self.dir = "down"
        
        self.pos_x = x
        self.pos_y = y

        if(self.dir ==  "down"):
            # head (oups)
            self.list_body_parts.get("head").set_x(self.pos_x + 2)
            self.list_body_parts.get("head").set_y(self.pos_y - 2)

            # pattes
            self.list_body_parts.get("legs").set_x(self.pos_x)
            self.list_body_parts.get("legs").set_y(self.pos_y + 2)

            # queue
            self.list_body_parts.get("tail").set_x(self.pos_x +2)
            self.list_body_parts.get("tail").set_y(self.pos_y)

            # torso
            self.list_body_parts.get("torso").set_x(self.pos_x)
            self.list_body_parts.get("torso").set_y(self.pos_y)

        elif(self.dir == "right"):
            # head (oups)
            self.list_body_parts.get("head").set_x(self.pos_x - 2)
            self.list_body_parts.get("head").set_y(self.pos_y + 2)

            # pattes
            self.list_body_parts.get("pattes").set_x(self.pos_x)
            self.list_body_parts.get("pattes").set_y(self.pos_y + 2)

            # queue
            self.list_body_parts.get("queue").set_x(self.pos_x-2)
            self.list_body_parts.get("queue").set_y(self.pos_y)

            # torso
            self.list_body_parts.get("torso").set_x(self.pos_x)
            self.list_body_parts.get("torso").set_y(self.pos_y)

        elif(self.dir == "up"):
            # head (oups)
            self.list_body_parts.get("head").set_x(self.pos_x )
            self.list_body_parts.get("head").set_y(self.pos_y - 2)

            # pattes --> rotate ? en dessous ?
            self.list_body_parts.get("pattes").set_x(self.pos_x)
            self.list_body_parts.get("pattes").set_y(self.pos_y)

            # queue
            self.list_body_parts.get("queue").set_x(self.pos_x-2)
            self.list_body_parts.get("queue").set_y(self.pos_y)

            # torso
            self.list_body_parts.get("torso").set_x(self.pos_x)
            self.list_body_parts.get("torso").set_y(self.pos_y)

        elif(self.dir == "down"):
            # head (oups)
            self.list_body_parts.get("head").set_x(self.pos_x - 2)
            self.list_body_parts.get("head").set_y(self.pos_y + 2)

            # pattes
            self.list_body_parts.get("pattes").set_x(self.pos_x)
            self.list_body_parts.get("pattes").set_y(self.pos_y + 2)

            # queue
            self.list_body_parts.get("queue").set_x(self.pos_x-2)
            self.list_body_parts.get("queue").set_y(self.pos_y)

            # torso
            self.list_body_parts.get("torso").set_x(self.pos_x)
            self.list_body_parts.get("torso").set_y(self.pos_y)
    
    
    def move(self):
        now = time.time()
        if(now - self.start > 60):
            self.start = now
            x_goal = random.randint(0,Model.SCREEN_LENGTH)
            y_goal = random.randint(0,Model.SCREEN_WIDTH)
        
        self.go_to(x_goal,y_goal)
    
    def go_to(self,x,y):
        # ràv avec la fonction set_pos pas touche
        dist_x = self.pos_x - x
        dist_y = self.pos_y - y

        # x
        if(dist_x>=3):
            x_speed = 3
        elif(dist_x>-3):
            x_speed = dist_x
        elif(dist_x<-3):
            x_speed = -3
        # y
        if(dist_y>=3):
            y_speed = 3
        elif(dist_y>-3):
            y_speed = dist_y
        elif(dist_y<-3):
            y_speed = -3
        
        self.set_pos(self.pos_x+ x_speed, self.pos_y+ y_speed)
