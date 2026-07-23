from Animal import Animal

class Tree :

    def __init__(self, commun_ancestor: Animal):
        """
        The commun ancestor has a value of None in the dict of the direct ancestors
        """
        commun_ancestor = commun_ancestor
        direct_ancestors = {commun_ancestor: None}

    def add_animal(self, animal: Animal, ancestor: Animal):
        self.direct_ancestors[animal: ancestor]

    def is_ancestor(self, animal1, animal2):
        """
        Test if animal2 is the ancestor of animal1
        """
        return self.direct_ancestor[animal1] == animal2