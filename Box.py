

from Vec import Vec
from Specie import Specie
from View import View


class Box:

    def __init__(self, pos:Vec, rad: float, view : View, parent):
        self.pos = pos
        self.rad = rad
        self.view = view
        self.spec : Specie  = None
        self.parent = parent

    def update_spec(self, new_spec : Specie):
        self.spec = new_spec

    def draw(self):
        if self.spec:
            for body_part in self.spec:
                dna_to_draw = self.spec.list_body_parts[body_part].active_sec
                image = self.view.draw_image[dna_to_draw] + "_mini"
                self.view.draw_image(image, self.pos)

    def fill(self,specie):
        pass