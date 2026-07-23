from itertools import combinations
class Model:
    def __init__(self):
        self.SCREEN_LENGTH = 1280
        self.SCREEN_WIDTH = 1920
        self.animals = []

    def update(self):
        pass

    def add_animal(self, animal):
        self.animals.append(animal)

    def dna_edit():
        col = ['R', 'B', 'V']
        sequences = combinations(col, 8)
        dna_image = {}
        for elt in sequences:
            dna_image[elt] = None