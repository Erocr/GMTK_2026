from Animal import Animal

class Tree :

    def __init__(self, common_ancestor: Animal):
        """
        The commun ancestor has a value of None in the dict of the direct ancestors
        """
        common_ancestor = common_ancestor
        direct_ancestors = {common_ancestor: None}

    def add_animal(self, animal: Animal, ancestor: Animal):
        self.direct_ancestors[animal: ancestor]

    def is_ancestor(self, animal1, animal2):
        """
        Test if animal2 is the ancestor of animal1
        """
        return self.direct_ancestor[animal1] == animal2
