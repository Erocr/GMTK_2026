import time

import pygame as pg
from BodyPart import BodyPart
from Vec import *
import os
from Animal import Animal


class View:
    ANIMAL_SIZE_RATIO = 0.8

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
        self.animations_full = {}
        self.animations = {}

        self.body_parts_ordered = ["tail", "torso", "legs", "head"]

        self.load_images()
        self.resize_images()

        self.left_dna_editor = None
        self.right_dna_editor = None

    def resize(self, screen_size):
        self.screen_size = screen_size
        self.screen_ratio = self.screen_size / self.screen_size_full
        self.resize_images()

    def is_animal_image(self, image_name):
        for body_part in self.body_parts_ordered:
            if image_name[:len(body_part)] == body_part:
                return True
        return False

    def resize_images(self):
        for image_name in self.images_full:
            screen_ratio = self.screen_ratio
            if self.is_animal_image(image_name):
                screen_ratio *= self.ANIMAL_SIZE_RATIO
            self.images[image_name] = pg.transform.scale_by(self.images_full[image_name], screen_ratio.get()).convert_alpha()

        for body_part in self.body_parts_ordered:
            for i in range(5):
                image_name = body_part + f"_{i}"
                self.images[image_name+"_flipped"] = pg.transform.flip(self.images[image_name], True, False).convert_alpha()

        for animation in self.animations_full:
            self.animations[animation + "_flipped"] = [None] * 14
            for i in range(len(self.animations_full[animation])):
                self.animations[animation][i] = pg.transform.scale_by(self.animations_full[animation][i],
                                                                      (self.screen_ratio * self.ANIMAL_SIZE_RATIO).get()).convert_alpha()
                self.animations[animation+"_flipped"][i] = pg.transform.flip(self.animations[animation][i], True, False).convert_alpha()

    def load_images(self):
        for file_name in os.listdir("assets/images"):
            self.load_image(file_name)

        for animation in os.listdir("assets/animations"):
            to_add = []
            for animation_im in os.listdir("assets/animations/"+animation):
                to_add.append(pg.image.load("assets/animations/"+animation+"/"+animation_im).convert_alpha())
            self.animations_full[animation] = to_add
            self.animations[animation] = to_add.copy()  # To initialize with good size

    def load_image(self, file_name):
        """
        Load all the images from the directory assets/images/.
        Loads into self.images_full
        """
        image_name = file_name.split(".")[0]
        file_name = "assets/images/" + file_name
        image = pg.image.load(file_name).convert_alpha()
        self.images_full[image_name] = image

    def empty_surf(self, size: Vec) -> pg.Surface:
        res = pg.Surface(size.get())
        res.convert_alpha()
        res.fill((0, 0, 0, 0))
        return res

    def draw_image(self, image_name: str, pos):
        self.screen.blit(self.images[image_name], (pos*self.screen_ratio).get())

    def draw_anim(self, anim, index, pos):
        self.screen.blit(self.animations[anim][index], (pos*self.screen_ratio).get())

    def draw_image_flipped(self, image_name: str, pos):
        self.screen.blit(self.images[image_name+"_flipped"], (pos*self.screen_ratio).get())

    def draw_anim_flipped(self, anim, index, pos):
        self.screen.blit(self.animations[anim+"_flipped"][index], (pos*self.screen_ratio).get())
    
    def draw_animal(self, animal: Animal):
        """ Tourner les images selon la direction: de base, elle va vers la gauche"""
        if animal.dir == "left":
            for key in self.body_parts_ordered:
                if key == "legs":
                    anim_i = (time.time() - animal.startMovementTime) / animal.LEG_ANIM_FRAME_DURATION
                    anim_i = int(anim_i)
                    anim_i = anim_i % 13
                    anim = self.model.get_image(animal.list_body_parts[key].active_sec)
                    if anim[:4] != "legs":
                        print(f"anomaly: {anim}")
                        continue
                    print(f"normal: {anim_i}")
                    self.draw_anim(anim, anim_i, animal.pos)
                else:
                    self.draw_image(self.model.get_image(animal.list_body_parts[key].active_sec), animal.pos)
        elif animal.dir == "right":
            for key in self.body_parts_ordered:
                if key == "legs":
                    anim_i = (time.time() - animal.startMovementTime) / animal.LEG_ANIM_FRAME_DURATION
                    anim_i = int(anim_i)
                    anim_i = anim_i % 13
                    anim = self.model.get_image(animal.list_body_parts[key].active_sec)
                    if anim[:4] != "legs":
                        print(f"anomaly: {anim}")
                        continue
                    print(f"normal: {anim_i}")
                    self.draw_anim_flipped(anim, anim_i, animal.pos)
                else:
                    self.draw_image_flipped(self.model.get_image(animal.list_body_parts[key].active_sec), animal.pos)
        else:
            pass

    def draw_text(self, pos, text, color=(0, 0, 0)):
        pos *= self.screen_ratio
        text_im = self.font.render(text, True, color)
        self.screen.blit(text_im, pos.get())

    def rect(self, pos, size, color=(255, 255, 255)):
        pos *= self.screen_ratio
        size *= self.screen_ratio
        pg.draw.rect(self.screen, color, pg.Rect(*pos.get(), *size.get()))

    def draw(self):
        #self.draw_image("test", Vec(1900, 1260))


        for animal in self.model.animals:
            self.draw_animal(animal)

        if self.left_dna_editor is not None:
            self.left_dna_editor.draw()
        if self.right_dna_editor is not None:
            self.right_dna_editor.draw()

        self.flip()

    def flip(self):
        pg.display.flip()
        self.draw_image("background_terrarium_v1", Vec(0, 0))
