from InputHandler import InputHandler
from Model import Model


class Controller:
    def __init__(self, model:Model, view):
        self.model = model
        self.view = view
        self.inputHandler = InputHandler()

    @property
    def quit(self):
        return self.inputHandler.quit

    def update(self):
        self.inputHandler.update()
        if self.inputHandler.resized is not None:
            self.view.resize(self.inputHandler.resized)
        for animal in self.model.animals:
            animal.move()