from Controller import Controller
from Vec import Vec


class TreeWindow:

    def __init__(self, controller:Controller, img_closed:str, img_opened:str):
        self.controller = controller
        self.img_closed = img_closed
        self.img_opened = img_opened
        self.opened = False

    def draw(self):
        if self.opened:
            self.controller.view.draw_image(self.img_opened, Vec(0,0))
        else:
            self.controller.view.draw_image(self.img_closed, Vec(0,0))