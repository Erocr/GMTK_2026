from itertools import combinations
from random import randint
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
        nbimg = 2 #A UPADATE
        images = []
        for i in range(nbimg):
            images.append("tail"+ str(i)+".png")
            images.append("torso"+ str(i)+".png")
        for elt in sequences:
            dna_image[elt] = images[randint(len(images))]