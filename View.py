import pygame as pg
from BodyPart import BodyPart
from Vec import *
import os
from Animal import Animal
from Dna import Dna


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

        # associates to the name of an image the corresponding image
        self.images_full: dict[str: pg.Surface] = {}
        # Same of images_full, but this time it has a size depending on the size of the screen
        self.images: dict[str: pg.Surface] = {}

        self.body_parts_ordered = ["tail", "torso", "legs", "head"]

        self.load_images()
        self.resize_images()

        self.dna_1 = Dna(Vec(40, 0), 500, "RRVVVBBBBRRRVBVRRVRBRRVB")
        self.dna_2 = None

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

    def empty_surf(self, size: Vec) -> pg.Surface:
        res = pg.Surface(size.get())
        res.convert_alpha()
        res.fill((0, 0, 0, 0))
        return res

    def draw_ADN(self, pos: Vec, length: float, adn):
        """ adn is a string : R for red, G for green, B for blue"""
        bar_positions_y = [10, 27, 85, 104, 123, 141, 201, 218]  # Relatively to the image
        bar_positions_x = [11, 14, 18, 11, 11, 17, 15, 11]  # Relatively to the image

        colors = {"R": (255, 0, 0),
                  "G": (0, 255, 0),
                  "B": (0, 0, 255)}

        index = 0
        y = 0
        while y < length:
            for i in range(8):
                if index + i >= len(adn):
                    return
                bar_y = bar_positions_y[i]
                bar_x = bar_positions_x[i]
                bar_size = Vec(80-bar_x*2, 5)
                self.rect(pos + Vec(bar_x, bar_y), bar_size, colors[adn[index+i]])
            self.draw_image("ADN_no_bars", pos)
            pos += Vec(0, self.images_full["ADN_no_bars"].get_height())
            y += self.images_full["ADN_no_bars"].get_height()
            index += 8

    def draw_image(self, image_name : str, pos):
        self.screen.blit(self.images[image_name], (pos*self.screen_ratio).get())

    def draw_image_flipped(self, image_name : str, pos):
        self.screen.blit( pg.transform.flip( self.images[image_name] , False, True) , (pos*self.screen_ratio).get())

    def draw_image_rotated(self, image_name : str, pos, angle):
        self.screen.blit( pg.transform.rotate( self.images[image_name] , angle) , (pos*self.screen_ratio).get())
    
    def draw_animal(self, animal:Animal):
        
        """ tourner les images selon la direction: de base elle va vers la gauche"""
        if(animal.dir == "left"):
            for key in self.body_parts_ordered:
                self.draw_image(animal.list_body_parts[key].image_name, Vec(animal.pos_x,animal.pos_y))
        elif(animal.dir == "right"):
            for key in self.body_parts_ordered:
                self.draw_image_flipped(animal.list_body_parts[key].image_name, Vec(animal.pos_x,animal.pos_y))
        else:
            if(animal.dir == "up"):
                angle = -90
            elif(animal.dir == "down"):
                angle = 90

            for key in self.body_parts_ordered:
                self.draw_image_rotated(animal.list_body_parts[key].image_name, Vec(animal.pos_x,animal.pos_y), angle)


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

        if self.dna_1 is not None:
            self.dna_1.draw(self)
        if self.dna_2 is not None:
            self.dna_2.draw(self)
        
        for animal in self.model.animals:
            self.draw_animal(animal)

        self.flip()

    def flip(self):
        pg.display.flip()
        self.screen.fill((0, 0, 0))
