from InputHandler import InputHandler, Key
from Model import Model
from Vec import Vec
from random import randint
from Tree import Tree


class Controller:
    def __init__(self, model:Model, view):
        self.model = model
        self.view = view
        self.inputHandler = InputHandler(view)

    @property
    def quit(self):
        return self.inputHandler.quit
    
    def create_children(self, tree:Tree, ancestor, etage, children = None):
        if children is None:
            children = [ancestor]
        if etage == 0:
            print(children)
            return children
        else:
            waiting_children = []
            kid1, kid2 = tree.create_kid(ancestor)
            children.append(kid1)
            children.append(kid2)
            waiting_children.append(kid1)
            children.append(kid2)
            for kid in waiting_children : 
                self.create_children(tree, kid,etage-1, children)
            


    def search_animal(self,pos:Vec):
        for animal in self.model.animals:
            if(animal.pos_x == pos.x and animal.pos_y == pos.y):
                #TODO prévenir l'animal qu'il est cliqué ? ouvrir la fenêtre de découpage d'adn
                pass

    def update(self):
        self.inputHandler.update()
        if self.inputHandler.resized is not None:
            self.view.resize(self.inputHandler.resized)
        
        if self.inputHandler.pressed("mouse_left"):
            self.search_animal(self.inputHandler.mouse_pos)
            if self.view.dna_1 is not None:
                index = self.view.dna_1.dna_clicked(self.inputHandler.mouse_pos)
                print(index)

        for animal in self.model.animals:
            animal.move()

    def get_random_seq(self, part : str, avoid: list[str]=None):
            """
            Return None if their is no body part left without choosing one that must be avoid \n
            """
            if not avoid : avoid = []
            if len(avoid) > 5: return None

            #Take all the dna sequences linked to the body part
            dna = []
            dict = self.model.get_dna_image()
            for elt in dict:
                #Récupération de la string
                p = ""
                for char in dict[elt]:
                    if char == '_': break
                    else: p += char
                #add if it's the good part
                if p == part : dna.append(elt)

            return dna[randint(0, len(dna)-1)]


model = Model()
test = Controller(model, None)
print(model.dna_image[test.get_random_seq("torso")])