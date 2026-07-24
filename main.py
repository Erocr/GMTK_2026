from Animal import Animal
from BodyPart import BodyPart
from Tree import Tree
from View import View
from Controller import Controller
from Model import Model
from Animal import Animal
from BodyPart import BodyPart

import time


def play():
    model = Model()
    view = View(model)
    controller = Controller(model, view)



    FPS = 60
    LOOP_TIME = 1 / FPS

    
    # create ancestor body parts
    head = BodyPart(controller.get_random_seq("head"))
    torso = BodyPart(controller.get_random_seq("torso"))
    legs = BodyPart(controller.get_random_seq("legs"))
    tail = BodyPart(controller.get_random_seq("tail"))

    # create animals
    ancestor = Animal(head,torso,legs,tail,0,0,model)
    tree = Tree(ancestor,model)
    controller.create_children(tree, ancestor, 20)

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
