import pygame as pg
from Vec import *
import os


class View:
    def __init__(self, model):
        self.model = model

        self.screen_size_full = Vec(1920, 1280)
        self.screen_size = Vec(600, 600)
        self.screen_ratio = self.screen_size / self.screen_size_full
        self.screen = pg.display.set_mode(self.screen_size.get(), pg.RESIZABLE)

        pg.font.init()
        sys_font_path = pg.font.get_default_font()
        self.font = pg.font.Font(sys_font_path, 20)

        self.images_full = {}  # associates to the name of an image the corresponding image
        self.images = {}  # Same of images_full, but this time it has a size depending on the size of the screen
        self.load_images()
        self.resize_images()

    def resize(self, screen_size):
        self.screen_size = screen_size
        self.screen_ratio = self.screen_size / self.screen_size_full
        self.resize_images()

    def resize_images(self):
        for image_name in self.images_full:
            self.images[image_name] = pg.transform.scale_by(self.images_full[image_name], self.screen_ratio.get())

    def load_images(self):
        for file_name in os.listdir("assets/images"):
            self.load_image(file_name)

    def load_image(self, file_name):
        """
        Load all the images from the directory assets/images/.
        Loads into self.images_full
         """
        image_name = file_name.split(".")[0]
        file_name = "assets/images/" + file_name
        image = pg.image.load(file_name)
        self.images_full[image_name] = image

    def draw_image(self, image_name, pos):
        self.screen.blit(self.images_full[image_name], (pos*self.screen_ratio).get())

    def draw_text(self, pos, text, color=(0, 0, 0)):
        pos *= self.screen_ratio
        text_im = self.font.render(text, True, color)
        self.screen.blit(text_im, pos.get())

    def rect(self, pos, size, color=(255, 255, 255)):
        pos *= self.screen_ratio
        size *= self.screen_ratio
        pg.draw.rect(self.screen, color, pg.Rect(*pos.get(), *size.get()))

    def draw(self):
        self.draw_image("test", Vec(1900, 1260))

        self.flip()

    def flip(self):
        pg.display.flip()
        self.screen.fill((0, 0, 0))
