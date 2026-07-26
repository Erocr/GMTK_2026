from View import View
from Vec import Vec


class TreeWindow:

    def __init__(self, view: View, img_closed:str, img_opened:str, pos:Vec):
        self.view = view
        self.img_closed = img_closed
        self.img_opened = img_opened
        self.opened = False
        self.pos = pos
        self.width = 50 #width of the folder icon
        self.height = 50 #height of the folder icon

    def draw(self):
        if self.opened:
            self.view.draw_image(self.img_opened, self.pos)
        self.view.draw_image(self.img_closed, self.pos) # the folder is always showed