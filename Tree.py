from random import randint
from Specie import Specie


class Tree:
    def __init__(self, common_ancestor: Specie):
        """
        The commun ancestor has a value of None in the dict of the direct ancestors
        """
        common_ancestor = common_ancestor
        self.direct_ancestors = {common_ancestor: None}

    def add_animal(self, animal: Specie, ancestor: Specie):
        self.direct_ancestors[animal] = ancestor

    """ def is_ancestor(self, animal1, animal2):
        \"""
        Test if animal2 is the ancestor of animal1
        \"""
        return self.direct_ancestors[animal1] == animal2 """

    def get_last_gen(self):
        gen = set(self.direct_ancestors.keys())
        ancestor = set(self.direct_ancestors.values())
        return gen - ancestor

    def get_direct_ancestor(self, spec1: Specie, spec2 : Specie):
        """
        Returns the direct ancestor of spec1 and spec2 if it's the same and if none of the ancestors are None and None otherwise
        """
        if self.direct_ancestors[spec1] and self.direct_ancestors[spec2] and self.direct_ancestors[spec1] == self.direct_ancestors[spec2]:
            return self.direct_ancestors[spec1]
        else : return None