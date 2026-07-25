from Animal import Animal
from BodyPart import BodyPart
from Tree import Tree
from Vec import Vec
from View import View
from Controller import Controller
from Model import Model
from Specie import Specie
from BodyPart import BodyPart

import time


def play():
    model = Model()
    view = View(model)
    controller = Controller(model, view)



    FPS = 60
    LOOP_TIME = 1 / FPS

    
    # create ancestor body parts
    head = BodyPart(model.get_random_seq("head"))
    torso = BodyPart(model.get_random_seq("torso"))
    legs = BodyPart(model.get_random_seq("legs"))
    tail = BodyPart(model.get_random_seq("tail"))

    # create animals
    specie = Specie(head, torso, legs, tail, model)
    # ancestor = Animal(Vec(0, 0), specie)
    tree = Tree(specie)
    model.set_tree(tree)
    controller.create_children(tree, specie, 20)
    model.fill_animals()
    print(model.animals)

    # Game loop
    while not controller.quit:
        start = time.time()

        controller.update()
        model.update()
        view.draw()

        # Freeze the FPS
        end = time.time()
        if end - start < LOOP_TIME:
            time.sleep(LOOP_TIME - (end - start))


if __name__ == "__main__":
    play()
