from itertools import combinations
from random import randint
class Model:
    def __init__(self):
        self.SCREEN_LENGTH = 1280
        self.SCREEN_WIDTH = 1920
        self.animals = []
        self.dna_image = {}
        self.images = []

    def update(self):
        pass

    def add_animal(self, animal):
        self.animals.append(animal)

    def dna_edit(self):
        col = ['R', 'B', 'V']
        sequences = combinations(col, 8)
        nbimg = 2 #A UPDATE
        for i in range(nbimg):
            self.images.append("tail"+ str(i)+".png")
            self.images.append("torso"+ str(i)+".png")
        for elt in sequences:
            self.dna_image[elt] = self.images[randint(len(self.images))]