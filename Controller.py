from InputHandler import InputHandler, Key
from Model import Model
from Vec import Vec


class Controller:
    def __init__(self, model:Model, view):
        self.model = model
        self.view = view
        self.inputHandler = InputHandler()

    @property
    def quit(self):
        return self.inputHandler.quit

    def search_animal(self,pos:Vec):
        for animal in self.model.animals:
            if(animal.pos_x == pos.x and animal.pos_y == pos.y):
                #TODO prévenir l'animal qu'il est cliqué ? ouvrir la fenêtre de découpage d'adn
                pass

    def update(self):
        self.inputHandler.update()
        if self.inputHandler.resized is not None:
            self.view.resize(self.inputHandler.resized)
        
        for event in InputHandler.events.keys():
            if InputHandler.events[event] == InputHandler.keys["mouse_left"]: # si on a cliqué gauche
                if InputHandler.events[event].released: # si on a *cliqué* gauche
                    self.search_animal(InputHandler.mouse_pos)


        for animal in self.model.animals:
            animal.move()