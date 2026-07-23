from BodyPart import BodyPart

class Animal:
    
    def __init__(self,tete : BodyPart,pattes : BodyPart, torse : BodyPart, x, y):
        self.list_body_parts = {"tete" : tete, "pattes" : pattes, "torse" : torse}
        self.pos_x = x
        self.pos_y = y
    
    def set_body_part(self, part : str, new_part : BodyPart):
        self.list_body_parts.get(part) = new_part
    
    def set_x(self, x):
        self.pos_x = x
        self.set_pos()
    
    def set_y(self,y):
        self.pos_y = y
        self.set_pos()

    def set_pos(self):
        """set body parts positions"""

        # head (oups)
        self.list_body_parts.get("tete").set_x(self.pos_x + 2)
        self.list_body_parts.get("tete").set_y(self.pos_y - 2)

        # pattes
        self.list_body_parts.get("pattes").set_x(self.pos_x -1)
        self.list_body_parts.get("pattes").set_y(self.pos_y + 2)

        # torse
        self.list_body_parts.get("torse").set_x(self.pos_x)
        self.list_body_parts.get("torse").set_y(self.pos_y)