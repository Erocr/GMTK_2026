
from InputHandler import InputHandler, Key
from Model import Model
from Vec import Vec
from random import randint, shuffle
from Tree import Tree
from DnaEditor import DnaEditor
from Dna import Dna
from Button import DnaEditorButton


class Controller:
    def __init__(self, model: Model, view):
        self.model = model
        self.view = view
        self.inputHandler = InputHandler(view)
        self.buttons_right = []
        self.buttons_left = []

    @property
    def quit(self):
        return self.inputHandler.quit

    def search_animal(self, mouse_pos: Vec):
        if 1226 <= mouse_pos.x and 56 <= mouse_pos.y and 1250 >= mouse_pos.y and self.view.right_dna_editor is not None: return
        if 694 >= mouse_pos.x and 56 <= mouse_pos.y and 1250 >= mouse_pos.y and self.view.left_dna_editor is not None: return

        shuffle(self.model.animals)
        for animal in self.model.animals:
            if(animal.pos.x <= mouse_pos.x and animal.pos.x + 743 >= mouse_pos.x and animal.pos.y <= mouse_pos.y and animal.pos.y + 458 >= mouse_pos.y):
                if self.view.last_edit == "left":
                    self.view.right_dna_editor = DnaEditor(animal, False, None, self.view)
                    self.model.dna_2 = Dna(Vec(1550, 600), 600, animal.get_dna())
                    self.view.last_edit = "right"

                    self.buttons_right.append(DnaEditorButton(Vec(148, 185) + Vec(1253, 50), Vec(204,170), self.view.right_dna_editor, animal.list_body_parts["torso"], self.model, 2))
                    self.buttons_right.append(DnaEditorButton(Vec(1338, 348), Vec(253, 118), self.view.right_dna_editor, animal.list_body_parts["legs"], self.model, 2))
                    self.buttons_right.append(DnaEditorButton(Vec(300, 160) + Vec(1253, 50), Vec(442,297), self.view.right_dna_editor, animal.list_body_parts["tail"], self.model, 2))
                    self.buttons_right.append(DnaEditorButton(Vec(1253, 50), Vec(245, 297), self.view.right_dna_editor, animal.list_body_parts["head"], self.model, 2))

                
                elif self.view.last_edit == "right":
                    self.view.left_dna_editor = DnaEditor(animal, True, None, self.view)
                    self.model.dna_1 = Dna(Vec(325, 600), 600, animal.get_dna())
                    self.view.last_edit = "left"

                    self.buttons_right.append(DnaEditorButton(Vec(148, 185) + Vec(27, 50), Vec(204,170), self.view.left_dna_editor, animal.list_body_parts["torso"], self.model, 1))
                    self.buttons_left.append(DnaEditorButton(Vec(112, 348), Vec(253, 118), self.view.left_dna_editor, animal.list_body_parts["legs"], self.model, 1))
                    self.buttons_right.append(DnaEditorButton(Vec(300, 160) + Vec(27, 50), Vec(442,297), self.view.left_dna_editor, animal.list_body_parts["tail"], self.model, 1))
                    self.buttons_right.append(DnaEditorButton(Vec(27, 50), Vec(245, 297), self.view.left_dna_editor, animal.list_body_parts["head"], self.model, 1))



                break #oui c'est pas bien, mais ça séléctionne un unique animal par clic

    
    def update(self):
        self.inputHandler.update()
        if self.inputHandler.resized is not None:
            self.view.resize(self.inputHandler.resized)
        
        if self.inputHandler.pressed("mouse_left"):
            self.search_animal(self.inputHandler.mouse_pos)

            for button in self.buttons_left:
                button.is_clicked(self.inputHandler.mouse_pos)
            for button in self.buttons_right:
                button.is_clicked(self.inputHandler.mouse_pos)

            if self.view.model.dna_1 is not None:
                index = self.view.model.dna_1.dna_clicked(self.inputHandler.mouse_pos)
                # print(index) ???

        for animal in self.model.animals:
            animal.move()

