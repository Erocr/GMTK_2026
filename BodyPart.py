class BodyPart:

    def __init__(self, dna_sec : str, image_name : str):
        self.dna_sec = ""
        self.active_sec = "" # 8 caractère
        self.pos_x = 0
        self.pos_y = 0
        self.image_name = image_name

    def set_x(self, x):
        self.pos_x = x

    def set_y(self, y):
        self.pos_y = y

    def getdna(self):
        return self.dna_sec

    def adddna(self, newdna):
        self.active_sec = newdna
        self.dna_sec += newdna

    def setdna(self, dna, activedna):
        self.active_sec = activedna
        self.dna_sec = dna