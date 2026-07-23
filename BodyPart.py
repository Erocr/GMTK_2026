class BodyPart:

    def __init__(self):
        # self.img = img TODO
        self.dna_sec = ""
        self.pos_x = 0
        self.pos_y = 0

    def set_x(self, x):
        self.pos_x = x

    def set_y(self, y):
        self.pos_y = y

    def get_dnasec(self):
        return self.dna_sec