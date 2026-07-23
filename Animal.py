from BodyPart import BodyPart

class Animal:
    
    def __init__(self,tete : BodyPart,pattes : BodyPart, torse : BodyPart):
        self.list_body_parts = {"tete" : tete, "pattes" : pattes, "torse" : torse}
    
    def set_body_part(self, part : str, new_part : BodyPart):
        self.list_body_parts.get(part) = new_part