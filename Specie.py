import random
import time
from BodyPart import BodyPart



class Specie:
    last_id = 0

    def __init__(self, head: BodyPart, legs: BodyPart, torso: BodyPart, tail: BodyPart, model):
        self.id = self.last_id + 1
        Specie.last_id += 1
        self.list_body_parts = {"head": head, "legs": legs, "torso": torso, "tail": tail}
        self.model = model

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, animal2):
        for bodypart in self.list_body_parts:
            if self.list_body_parts[bodypart] != animal2.list_body_parts[bodypart]: return False
        return True

    def copy(self):
        copy = Specie(self.list_body_parts["head"], self.list_body_parts["legs"], self.list_body_parts["torso"],
                      self.list_body_parts["tail"], self.model)
        return copy

    def set_body_part(self, part: str, new_part: BodyPart):
        self.list_body_parts[part] = new_part

    def get_dna(self):
        dna = ""
        for body_part in self.list_body_parts:
            dna += self.list_body_parts[body_part].dna_sec
        return dna
