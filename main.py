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

    #model.add_animal(Animal( BodyPart("", "head_0"), BodyPart("", "legs_0"), BodyPart("", "body_0"), BodyPart("", "tail_4"), 0, 0, model ))


    FPS = 60
    LOOP_TIME = 1 / FPS

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
