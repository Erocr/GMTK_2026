from InputHandler import InputHandler, Key
from Model import Model
from Vec import Vec
from Tree import Tree


class Controller:
    def __init__(self, model:Model, view):
        self.model = model
        self.view = view
        self.inputHandler = InputHandler()

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
            children.append(kid1,kid2)
            waiting_children.append(kid1,kid2)
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
        
        for event in self.inputHandler.events.keys():
            if self.inputHandler.events[event] == self.inputHandler.keys["mouse_left"]: # si on a cliqué gauche
                if self.inputHandler.events[event].released: # si on a *cliqué* gauche
                    self.search_animal(self.inputHandler.mouse_pos)


        for animal in self.model.animals:
            animal.move()