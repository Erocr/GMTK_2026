
from InputHandler import InputHandler, Key
from Model import Model
from Vec import Vec
from random import randint
from Tree import Tree


class Controller:
    def __init__(self, model: Model, view):
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
            return children
        else:
            waiting_children = []
            kid1, kid2 = tree.create_kid(ancestor)
            children.append(kid1)
            children.append(kid2)
            waiting_children.append(kid1)
            children.append(kid2)
            for kid in waiting_children:
                self.create_children(tree, kid, etage-1, children)
            


    def search_animal(self,mouse_pos:Vec):
        for animal in self.model.animals:
            if(animal.pos.x <= mouse_pos.x and animal.pos.x + 743 >= mouse_pos.x and animal.pos.y <= mouse_pos.y and animal.pos.y + 458 >= mouse_pos.y):
                if self.view.left_dna_editor is not None:
                    pass
                else:
                    pass

    def update(self):
        self.inputHandler.update()
        if self.inputHandler.resized is not None:
            self.view.resize(self.inputHandler.resized)
        
        if self.inputHandler.pressed("mouse_left"):
            self.search_animal(self.inputHandler.mouse_pos)
            if self.view.dna_1 is not None:
                index = self.view.dna_1.dna_clicked(self.inputHandler.mouse_pos)
                # print(index) ???

        for animal in self.model.animals:
            animal.move()

        
    def add_animal(self, animal):
        self.model.add_animal(animal)
