from itertools import combinations
from random import randint, shuffle
class Model:
    def __init__(self):
        self.SCREEN_LENGTH = 1280
        self.SCREEN_WIDTH = 1920
        self.animals = []
        self.dna_image = {}
        self.images = []
        self.dna_set_up()

    def update(self):
        pass

    def add_animal(self, animal):
        self.animals.append(animal)

    def dna_set_up(self):
        
        nbimg = 5 #A UPDATE
        for i in range(nbimg):
            self.images.append("tail_"+ str(i)+".png")
            self.images.append("body_"+ str(i)+".png")
            self.images.append("head_"+ str(i)+".png")
            self.images.append("legs_"+ str(i)+".png")

        col = ['R','V','B']*8
        for i in range(200):
            shuffle(col)
            seq = ""
            for elt in col:
                seq += elt
            if seq not in self.dna_image:
                self.dna_image[seq] = None
            else:
                while seq in self.dna_image:
                    seq = shuffle(col)
                self.dna_image[seq] = None

        nb_dna = [0]*20
        for elt in self.dna_image:
            ind = randint(0, len(self.images)-1)
            while nb_dna[ind] >= 10:
                ind = randint(0, len(self.images)-1)
            self.dna_image[elt] = self.images[ind]
            nb_dna[ind] += 1
        print(nb_dna)
