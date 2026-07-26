from typing import Callable

from Vec import *
from Dna import Dna

class DnaEditorButton:

    def __init__(self, pos : Vec, size : Vec, editor, bodypart, model, dna_nb):
        self.pos = pos
        self.size = size
        self.editor = editor
        self.bodypart = bodypart
        self.model = model
        self.dna_nb = dna_nb

    def is_clicked(self, mouse_pos : Vec):
        if self.pos.x <= mouse_pos.x and self.pos.x + self.size.x >= mouse_pos.x and self.pos.y <= mouse_pos.y and self.pos.y + self.size.y >= mouse_pos.y:
            self.editor.selected_body_part = self.bodypart
            if self.dna_nb == 1:
                self.model.dna_1 = Dna(Vec(325, 600), 600, self.bodypart.getdna())
            elif self.dna_nb == 2:
                self.model.dna_2 = Dna(Vec(1550, 600), 600, self.bodypart.getdna())

 
class GenericButton:
    def __init__(self, pos: Vec, size: Vec, image: str, action_when_clicked: Callable, name=""):
        self.pos = pos
        self.size = size
        self.image = image
        self.action_when_clicked = action_when_clicked
        self.name = name
