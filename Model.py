from random import randint
from Animal import Animal
from BodyPart import BodyPart
from Vec import Vec
from Specie import Specie
from Tree import Tree
from itertools import combinations


class Model:
    SCREEN_SIZE = Vec(1920, 1280)

    def __init__(self):
        self.SCREEN_LENGTH = 1280
        self.SCREEN_WIDTH = 1920
        self.tree = None
        self.animals = []
        self.dna_image = {}
        self.images = []
        self.dna_set_up()
        self._init()

    def _init(self):
        # create ancestor body parts
        head = BodyPart(self.get_random_seq("head"))
        torso = BodyPart(self.get_random_seq("torso"))
        legs = BodyPart(self.get_random_seq("legs"))
        tail = BodyPart(self.get_random_seq("tail"))

        # create animals
        specie = Specie(head, torso, legs, tail, self)
        # ancestor = Animal(Vec(0, 0), specie)
        tree = Tree(specie)
        self.set_tree(tree)
        self.create_children(tree, specie, 20)
        self.fill_animals()

    def update(self):
        for animal in self.animals:
            animal.update()

    def set_tree(self, tree: Tree):
        self.tree = tree

    def get_image(self, sequence: str):
        return self.dna_image[sequence]

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_dna_image(self):
        return self.dna_image

    def dna_set_up(self):
        nbimg = 5  # A UPDATE
        for i in range(nbimg):
            self.images.append("tail_" + str(i))
            self.images.append("torso_" + str(i))
            self.images.append("head_" + str(i))
            self.images.append("legs_" + str(i))

        col = ['R','V','B']*8
        com = list(combinations(col, 8))
        for i in range(200):
            seq = ""
            seq = com[randint(0, len(com))]
            if seq not in self.dna_image:
                self.dna_image[seq] = None
            else:
                while seq in self.dna_image:
                    seq = com[randint(0, len(com))]
                self.dna_image[seq] = None

        nb_dna = [0]*20
        for elt in self.dna_image:
            ind = randint(0, len(self.images)-1)
            while nb_dna[ind] >= 10:
                ind = randint(0, len(self.images)-1)
            self.dna_image[elt] = self.images[ind]
            nb_dna[ind] += 1


    def get_random_seq(self, part : str, avoid: list[str]=None):
        """
        Return None if their is no body part left without choosing one that must be avoid \n
        """
        if not avoid : avoid = []
        if len(avoid) > 5: return None

        #Take all the dna sequences linked to the body part
        dna = []
        dict = self.get_dna_image()
        for elt in dict:
            #Récupération de la string
            p = ""
            for char in dict[elt]:
                if char == '_': break
                else: p += char
            #add if it's the good part
            if p == part : dna.append(elt)
        a = dna[randint(0, len(dna)-1)]
        return dna[randint(0, len(dna)-1)]

    def create_children(self, tree:Tree, ancestor, etage, children = None):
        if children is None:
            children = [ancestor]
        if etage == 0:
            return children
        else:
            waiting_children = []
            kid1, kid2 = self.create_kid(ancestor)
            """ for elt in kid1.list_body_parts:
                print(kid1.list_body_parts[elt].active_sec, kid2.list_body_parts[elt].active_sec)
            print('\n') """
            tree.add_animal(kid1, ancestor)
            tree.add_animal(kid2, ancestor)
            children.append(kid1)
            children.append(kid2)
            waiting_children.append(kid1)
            children.append(kid2)
            for kid in waiting_children:
                self.create_children(tree, kid, etage-1, children)

    def create_kid(self, ancestor: Specie):
            p = randint(0, 3)
            part = ["head", "torso", "legs", "tail"][p]
            ind = randint(0, (len(ancestor.list_body_parts[part].dna_sec))//8)
            kid1, kid2 = ancestor.copy(), ancestor.copy()
            dna1 = kid1.list_body_parts[part].getdna()
            dna2 = kid2.list_body_parts[part].getdna()

            seq1 = self.get_random_seq(part, [ancestor.list_body_parts[part].active_sec])
            seq2 = self.get_random_seq(part, [ancestor.list_body_parts[part].active_sec, seq1])

            #si la nouvel séquence d'adn est rajouté à la fin : 
            if ind == len(ancestor.list_body_parts[part].dna_sec)//8 :
                dna1 = kid1.list_body_parts[part].getdna()+ seq1
                dna2 = kid2.list_body_parts[part].getdna()+ seq2
            else:
                #sinon: prend l'adn de l'ancetre jusquà l'indice de la séquence voulu, ajoute la nouvelle séquence puis termin eavec la fin de la séquence de l'ancetre
                dna1 = ancestor.list_body_parts[part].getdna()[0:ind*8] + seq1 + ancestor.list_body_parts[part].getdna()[ind*8:len(ancestor.list_body_parts[part].getdna())]
                dna2 = ancestor.list_body_parts[part].getdna()[0:ind*8] + seq2 + ancestor.list_body_parts[part].getdna()[ind*8:len(ancestor.list_body_parts[part].getdna())]
            kid1.list_body_parts[part].setdna(dna1, seq1)
            kid2.list_body_parts[part].setdna(dna2, seq2)
            return kid1, kid2

    def fill_animals(self):
        last_gen = self.tree.get_last_gen()
        for spec in last_gen:
            x = randint(0, self.SCREEN_SIZE.x - 743)  # 743 is the width of an animal
            y = randint(0, self.SCREEN_SIZE.y - 458)  # 458 is the height of an animal
            self.animals.append(Animal(Vec(x, y), spec))
