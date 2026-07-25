from Controller import Controller


class TreeWindow:

    def __init__(self, controller:Controller, img:str):
        self.controller = controller
        self.img = img
        self.opened = False

    def draw(self):
        if self.opened:
            self.controller.view.draw_image(self.img, )
        else:
            pass