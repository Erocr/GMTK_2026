from InputHandler import InputHandler


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.inputHandler = InputHandler()

    @property
    def quit(self):
        return self.inputHandler.quit

    def update(self):
        self.inputHandler.update()
