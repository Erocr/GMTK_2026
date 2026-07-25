class BodyPart:
    def __init__(self, dna_or_bodyPart):
        """
        You can create a new BodyPart in two ways:
        - If dna_or_bodyPart is a string, dna_or_body_part is considered as a dna sequence
        - If dna_or_bodyPart is a BodyPart, it will create a copy of the bodyPart
        """
        if isinstance(dna_or_bodyPart, str):
            self.dna_sec = ""
            self.active_sec = ""  # 8 caractère
            self.pos_x = 0
            self.pos_y = 0
            self.adddna(dna_or_bodyPart)
        else:
            self.dna_sec = dna_or_bodyPart.dna_sec
            self.active_sec = dna_or_bodyPart.active_sec
            self.pos_x = dna_or_bodyPart.pos_x
            self.pos_y = dna_or_bodyPart.pos_y

    def set_x(self, x):
        self.pos_x = x

    def set_y(self, y):
        self.pos_y = y

    def getdna(self):
        return self.dna_sec

    def adddna(self, newdna):
        assert len(newdna) == 8
        self.active_sec = newdna
        self.dna_sec += newdna

    def setdna(self, dna, activedna):
        assert len(activedna) == 8
        self.active_sec = activedna
        self.dna_sec = dna

    def copy(self):
        return BodyPart(self)
