import random
import time
from BodyPart import BodyPart
from Model import Model

class Animal:
    last_id = 0

    def __init__(self, head : BodyPart, legs : BodyPart, torso : BodyPart, tail : BodyPart, x, y, model : Model):
        self.id = self.last_id + 1
        Animal.last_id += 1
        self.list_body_parts = {"head" : head, "legs" : legs, "torso" : torso, "tail" : tail}
        self.model = model
        self.pos_x = x
        self.pos_y = y
        self.dir = "left"
        self.start = time.time()
        model.add_animal(self)

    def __hash__(self):
        return  hash(self.id)

    def __eq__(self, animal2):
        for bodypart in self.list_body_parts:
            if self.list_body_parts[bodypart] != animal2.list_body_parts[bodypart]: return False
        return True

    def copy(self):
        copy = Animal(self.list_body_parts["head"], self.list_body_parts["legs"], self.list_body_parts["torso"], self.list_body_parts["tail"], self.pos_x, self.pos_y, self.model)
        return copy
        
    
    def set_body_part(self, part : str, new_part : BodyPart):
        self.list_body_parts[part] = new_part

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



        """décalage des membres inutile normalement"""
        self.pos_x = x
        self.pos_y = y

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
        if(now - self.start > 60):
            self.start = now
            x_goal = random.randint(0,self.model.SCREEN_LENGTH)
            y_goal = random.randint(0,self.model.SCREEN_WIDTH)
        
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

    def get_dna(self):
        dna = ""
        for body_part in self.list_body_parts:
            dna += self.list_body_parts[body_part].get_dnasec
        return dna
