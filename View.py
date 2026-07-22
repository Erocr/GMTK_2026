import pygame as pg


class View:
    def __init__(self, model):
        self.model = model

        self.images = {}  # associates to the name of an image the corresponding image

        self.screen = pg.display.set_mode((600, 600))

    def rect(self, pos, size, color=(255, 255, 255)):
        pg.draw.rect(self.screen, color, pg.Rect(*pos.get(), *size.get()))

    def draw(self):
        self.flip()

    def flip(self):
        pg.display.flip()
        self.screen.fill((0, 0, 0))
