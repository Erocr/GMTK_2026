#743 par 458
from Animal import Animal
from BodyPart import BodyPart
from Vec import *


class DnaEditor:
    def __init__(self, animal : Animal, is_left_col : bool, selected_body_part : BodyPart, view):
        self.animal = animal
        self.is_left_col = is_left_col
        self.selected_body_part = selected_body_part
        self.view = view

    def draw(self):
        if not self.is_left_col:
            self.view.draw_image("dna_window", Vec(0,0))
            for key in self.view.body_parts_ordered:
                self.view.draw_image( self.view.model.get_image( self.animal.specie.list_body_parts[key].active_sec) , Vec(1276, 150))

            self.view.model.dna_2.draw(self.view)
        else:
            self.view.draw_image("dna_window_alone", Vec(0,56))
            for key in self.view.body_parts_ordered:
                self.view.draw_image( self.view.model.get_image( self.animal.specie.list_body_parts[key].active_sec) , Vec(50, 150))

            self.view.model.dna_1.draw(self.view)
