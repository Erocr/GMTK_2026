from random import randint
from Animal import Animal
from Model import Model

class Tree :

    def __init__(self, common_ancestor: Animal, model : Model):
        """
        The commun ancestor has a value of None in the dict of the direct ancestors
        """
        common_ancestor = common_ancestor
        self.direct_ancestors = {common_ancestor: None}
        self.model = model

    def add_animal(self, animal: Animal, ancestor: Animal):
        self.direct_ancestors[animal: ancestor]

    def is_ancestor(self, animal1, animal2):
        """
        Test if animal2 is the ancestor of animal1
        """
        return self.direct_ancestor[animal1] == animal2


    def create_kid(self, ancestor : Animal):
            p = randint(4)
            part = ["head", "body", "legs", "tail"][p]
            ind = randint(ancestor.list_body_parts[part]//8)
            kid1, kid2 = ancestor.copy(), ancestor.copy()
            dna1 = kid1.list_body_parts[part].getdna()
            dna2 = kid2.list_body_parts[part].getdna()
            # TODO : randomize seq1 & seq2
            seq1, seq2 = ""
            for i in range(0, ancestor.list_body_parts[part], 8):
                if i == ind:
                    for j in range(8):
                        dna1[i+j] = seq1[j]
                        dna2[i+j] = seq2[j]
                if i<ind:
                    for j in range(8):
                        dna1[i+j] = ancestor.list_body_parts[part][j]
                        dna2[i+j] = ancestor.list_body_parts[part][j]

            kid1.list_body_parts[part].setdna(dna1)
            kid2.list_body_parts[part].setdna(dna2)
            self.add_animal(kid1, ancestor)
            self.add_animal(kid2, ancestor)
            return kid1, kid2
