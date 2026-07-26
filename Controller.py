
from InputHandler import InputHandler, Key
from Model import Model
from TreeWindow import TreeWindow
from Vec import Vec
from random import randint
from Tree import Tree
from DnaEditor import DnaEditor
from Dna import Dna


class Controller:
    def __init__(self, model: Model, view):
        self.model = model
        self.view = view
        self.inputHandler = InputHandler(view)
        self.tree_window = TreeWindow(view, "icon_dossier", "arbre_genealogique_v3", "empty_window",Vec(0,0))
        self.opened_box = None
        view.set_tree_window(self.tree_window)


    @property
    def quit(self):
        return self.inputHandler.quit

    def search_animal(self, mouse_pos: Vec):
        for animal in self.model.animals:
            if (animal.pos.x <= mouse_pos.x and animal.pos.x + Model.ANIMAL_SIZE.x >= mouse_pos.x and animal.pos.y <= mouse_pos.y and animal.pos.y + Model.ANIMAL_SIZE.y >= mouse_pos.y):
                if self.view.left_dna_editor is not None:
                    self.view.right_dna_editor = DnaEditor(animal, False, None, self.view)
                    self.model.dna_2 = Dna(Vec(1550, 600), 600, animal.get_dna())
                else:
                    self.view.left_dna_editor = DnaEditor(animal, True, None, self.view)
                    self.model.dna_1 = Dna(Vec(325, 600), 600, animal.get_dna())

                break #oui c'est pas bien, mais ça séléctionne un unique animal par clic

    def tree_window_clicked(self, mouse_pos : Vec):
        if self.tree_window.pos.x<mouse_pos.x and self.tree_window.pos.x + self.tree_window.width > mouse_pos.x and self.tree_window.pos.y<mouse_pos.y and self.tree_window.pos.y + self.tree_window.height > mouse_pos.y:
            self.tree_window.opened = not self.tree_window.opened
            return True
        return False

    def box_clicked(self, mouse_pos:Vec):
        for box in self.tree_window.boxes:
            if box.pos.x - box.rad < mouse_pos.x and box.pos.x + box.rad > mouse_pos.x and box.pos.y - box.rad < mouse_pos.y and box.pos.y + box.rad > mouse_pos.y:
                self.view.open_list_species()
                self.opened_box = box

    def specie_chosen(self, mouse_pos:Vec):
        for spec in self.model.unlocked_species:
            if spec.pos.x < mouse_pos.x and spec.pos.x + 157 > mouse_pos.x and spec.pos.y < mouse_pos.y and spec.pos.y + 296> mouse_pos.y:
                self.opened_box.fill(spec)
                self.opened_box = None
                self.model.score += 1
                

    def update(self):
        self.inputHandler.update()
        if self.inputHandler.resized is not None:
            self.view.resize(self.inputHandler.resized)
        
        if self.inputHandler.pressed("mouse_left"):
            if not self.tree_window_clicked(self.inputHandler.mouse_pos):
                self.search_animal(self.inputHandler.mouse_pos)
            if self.tree_window.opened:
                self.box_clicked(self.inputHandler.mouse_pos)
            if self.view.list_species_opened:
                self.specie_chosen(self.inputHandler.mouse_pos)
            if self.view.model.dna_1 is not None:
                index = self.view.model.dna_1.dna_clicked(self.inputHandler.mouse_pos)
                # print(index) ???
            if self.model.score == 32:
                self.view.draw_image("win_pop_up")

