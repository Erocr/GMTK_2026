import pygame as pg
import os


class View:
    def __init__(self, model):
        self.model = model

        self.screen = pg.display.set_mode((600, 600))

        pg.font.init()
        sys_font_path = pg.font.get_default_font()
        self.font = pg.font.Font(sys_font_path, 20)

        self.images = {}  # associates to the name of an image the corresponding image
        self.load_images()

    def load_images(self):
        for file_name in os.listdir("assets/images"):
            self.load_image(file_name)

    def load_image(self, file_name):
        image_name = file_name.split(".")[0]
        file_name = "assets/images/" + file_name
        image = pg.image.load(file_name)
        self.images[image_name] = image

    def draw_image(self, image_name, pos):
        self.screen.blit(self.images[image_name], pos.get())

    def draw_text(self, pos, text, color=(0, 0, 0)):
        text_im = self.font.render(text, True, color)
        self.screen.blit(text_im, pos.get())

    def rect(self, pos, size, color=(255, 255, 255)):
        pg.draw.rect(self.screen, color, pg.Rect(*pos.get(), *size.get()))

    def draw(self):
        self.flip()

    def flip(self):
        pg.display.flip()
        self.screen.fill((0, 0, 0))
