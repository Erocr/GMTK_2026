
from InputHandler import InputHandler, Key
from Model import Model
from TreeWindow import TreeWindow
from Vec import Vec
from random import randint, shuffle
from Tree import Tree
from DnaEditor import DnaEditor
from Dna import Dna
from Button import DnaEditorButton, GenericButton


class Controller:
    def __init__(self, model: Model, view):
        self.model = model
        self.view = view
        self.inputHandler = InputHandler(view)
        self.tree_window = TreeWindow(view, "icon_dossier", "arbre_genealogique_v3", "empty_window",Vec(0,0))
        self.opened_box = None
        view.set_tree_window(self.tree_window)
        self.buttons_right = []
        self.buttons_left = []

    @property
    def quit(self):
        return self.inputHandler.quit

    def search_animal(self, mouse_pos: Vec):
        if 1226 <= mouse_pos.x and 56 <= mouse_pos.y and 1250 >= mouse_pos.y and self.view.right_dna_editor is not None: return
        if 694 >= mouse_pos.x and 56 <= mouse_pos.y and 1250 >= mouse_pos.y and self.view.left_dna_editor is not None: return

        self.model.animals.sort(key=lambda animal: -animal.pos.y)
        for animal in self.model.animals:
            if (animal.pos.x <= mouse_pos.x and animal.pos.x + Model.ANIMAL_SIZE.x >= mouse_pos.x and animal.pos.y <= mouse_pos.y and animal.pos.y + Model.ANIMAL_SIZE.y >= mouse_pos.y):
                if self.view.last_edit == "left":
                    self.view.right_dna_editor = DnaEditor(animal, False, None, self.view)
                    self.model.dna_2 = Dna(Vec(1550, 600), 600, animal.get_dna())
                    self.view.last_edit = "right"

                    self.buttons_right.append(DnaEditorButton(Vec(1360, 280), Vec(100,90), self.view.right_dna_editor, animal.list_body_parts["torso"], self.model, 2))
                    self.buttons_right.append(DnaEditorButton(Vec(1330, 348), Vec(130, 118), self.view.right_dna_editor, animal.list_body_parts["legs"], self.model, 2))
                    self.buttons_right.append(DnaEditorButton(Vec(1465, 160), Vec(300,297), self.view.right_dna_editor, animal.list_body_parts["tail"], self.model, 2))
                    self.buttons_right.append(DnaEditorButton(Vec(1240, 50), Vec(145, 297), self.view.right_dna_editor, animal.list_body_parts["head"], self.model, 2))

                    self.view.add_button(GenericButton(Vec(1226, 56), Vec(81, 88), "close_window_icon", None, "close_right_window"))
                    button = self.view.buttons[-1]

                    def close_window():
                        self.view.right_dna_editor = None
                        self.view.buttons.remove(button)

                    button.action_when_clicked = close_window
                elif self.view.last_edit == "right":
                    self.view.left_dna_editor = DnaEditor(animal, True, None, self.view)
                    self.model.dna_1 = Dna(Vec(325, 600), 600, animal.get_dna())
                    self.view.last_edit = "left"

                    self.buttons_right.append(DnaEditorButton(Vec(150, 280), Vec(100,90), self.view.left_dna_editor, animal.list_body_parts["torso"], self.model, 1))
                    self.buttons_left.append(DnaEditorButton(Vec(120, 348), Vec(130, 118), self.view.left_dna_editor, animal.list_body_parts["legs"], self.model, 1))
                    self.buttons_right.append(DnaEditorButton(Vec(225, 160), Vec(300,297), self.view.left_dna_editor, animal.list_body_parts["tail"], self.model, 1))
                    self.buttons_right.append(DnaEditorButton(Vec(30, 50), Vec(145, 297), self.view.left_dna_editor, animal.list_body_parts["head"], self.model, 1))

                    self.view.add_button(
                        GenericButton(Vec(0, 56), Vec(81, 88), "close_window_icon", None, name="close_left_window"))
                    button = self.view.buttons[-1]

                    def close_window():
                        self.view.left_dna_editor = None
                        self.view.buttons.remove(button)

                    button.action_when_clicked = close_window
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
            if self.opened_box and spec.pos.x < mouse_pos.x and spec.pos.x + 157 > mouse_pos.x and spec.pos.y < mouse_pos.y and spec.pos.y + 296> mouse_pos.y:
                self.opened_box.update_spec = spec
                self.opened_box = None
                s2 = None
                for i in range(len(self.tree_window.boxes)):
                    if self.tree_window.boxes[i].spec is not None and self.tree_window.boxes[i].spec ==  spec:
                        if i%2==0:
                            s2 = self.tree_window.boxes[i-1]
                        else:
                            s2 = self.tree_window.boxes[i+1]

                if s2 and self.model.tree.get_direct_ancestor(spec, s2) is not None:
                    self.model.score += 2
                

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

            for button in self.buttons_left:
                button.is_clicked(self.inputHandler.mouse_pos)
            for button in self.buttons_right:
                button.is_clicked(self.inputHandler.mouse_pos)

            for button in self.view.buttons:
                if button.pos.x <= self.inputHandler.mouse_pos.x <= button.pos.x + button.size.x \
                        and button.pos.y <= self.inputHandler.mouse_pos.y <= button.pos.y + button.size.y:
                    button.action_when_clicked()

            if self.view.model.dna_1 is not None and self.view.left_dna_editor is not None:
                index = self.view.model.dna_1.dna_clicked(self.inputHandler.mouse_pos)

                # print(index) ???
            if self.model.score == 32:
                self.view.draw_image("win_pop_up")
                self.view.left_dna_editor.modify_dna(index)

            if self.view.model.dna_2 is not None and self.view.right_dna_editor is not None:
                index = self.view.model.dna_2.dna_clicked(self.inputHandler.mouse_pos)
                self.view.right_dna_editor.modify_dna(index)



