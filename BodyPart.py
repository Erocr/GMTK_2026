class BodyPart:

    def __init__(self, img:str):
        self.img = img 
        self.adn_sec = ""
        self.pos_x = 0
        self.pos_y = 0

    def set_x(self, x):
        self.pos_x = x

    def set_y(self, y):
        self.pos_y = y