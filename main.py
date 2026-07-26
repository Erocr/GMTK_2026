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

    # titlescreen
    while not controller.quit:
        start = time.time()

        controller.update()
        if controller.inputHandler.pressed("mouse_left") and \
            165 <= controller.inputHandler.mouse_pos.x <= 695 and \
            530 <= controller.inputHandler.mouse_pos.y <= 700:
            break
        view.draw_titlescreen()

        # Freeze the FPS
        end = time.time()
        if end - start < LOOP_TIME:
            time.sleep(LOOP_TIME - (end - start))

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
        #print(1/(end - start))


if __name__ == "__main__":
    play()
