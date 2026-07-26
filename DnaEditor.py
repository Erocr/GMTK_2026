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
                if self.selected_body_part is not None and self.animal.specie.list_body_parts[key] != self.selected_body_part:
                    self.view.draw_image_with_effect(self.view.model.get_image( self.animal.specie.list_body_parts[key].active_sec) , Vec(1276, 150))
                else:
                    self.view.draw_image(self.view.model.get_image(self.animal.specie.list_body_parts[key].active_sec), Vec(1276, 150))

            self.view.model.dna_2.draw(self.view)
        else:
            self.view.draw_image("dna_window_alone", Vec(0,56))
            for key in self.view.body_parts_ordered:
                if self.selected_body_part is not None and self.animal.specie.list_body_parts[key] != self.selected_body_part:
                    self.view.draw_image_with_effect(self.view.model.get_image( self.animal.specie.list_body_parts[key].active_sec) , Vec(50, 150))
                else:
                    self.view.draw_image(self.view.model.get_image(self.animal.specie.list_body_parts[key].active_sec), Vec(50, 150))

            self.view.model.dna_1.draw(self.view)

    def get_animal_ancestor(self):
        return self.view.model.tree.direct_ancestors[self.animal.specie]

    def is_good_selected_part(self):
        if self.selected_body_part is None:
            return False
        selected_body_part = self.view.model.get_image(self.selected_body_part.active_sec)[:-2]
        ancestor_body_part = self.get_animal_ancestor().list_body_parts[selected_body_part]
        return ancestor_body_part.dna_sec != self.selected_body_part.dna_sec

    def modify_dna(self, index_dna_cutted):
        if index_dna_cutted is None or not self.is_good_selected_part():
            return

        dna_cutted = self.selected_body_part.dna_sec[index_dna_cutted * 8: index_dna_cutted * 8 + 8]
        if self.selected_body_part.active_sec == dna_cutted:
            self.animal.specie = self.get_animal_ancestor()
            self.view.get_button(f"close_{("right", "left")[self.is_left_col]}_window").action_when_clicked()

