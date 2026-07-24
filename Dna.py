from typing import Callable

from Animal import Animal
from Vec import Vec
from math import cos, pi
import pygame as pg


class Dna:
    WIDTH = 80

    def __init__(self, top_left_pos: Vec, length: int, dna: str):
        self.pos = top_left_pos
        self.length = length
        self.dna = dna

    def draw(self, view):
        branch1_col = (0, 255, 255)
        branch2_col = (0, 0, 255)

        nb_periods = len(self.dna) // 8
        period_size = self.length / nb_periods  # The horizontal size of a period

        def f1(t):
            # On veut que t * 2 * pi / period_size vaut 2 * pi lorsque t = period_size
            return self.WIDTH * 0.5 * cos(t * 2 * pi / period_size)

        def f2(t):
            # On veut que t * 2 * pi / period_size vaut 2 * pi lorsque t = period_size
            return - self.WIDTH * 0.5 * cos(t * 2 * pi / period_size)

        def draw_func(f: Callable, col, width: int):
            for i in range(self.length):
                pos = self.pos + Vec(-width/2 + f(i), i)
                size = Vec(width, 1/view.screen_ratio.y)
                view.rect(pos, size, col)

        # Draw the bars
        for i in range(len(self.dna)):
            bar = self.dna[i]
            col = {"R": (255, 0, 0),
                   "V": (255, 0, 255),
                   "B": (0, 0, 255)}[bar]
            bar_y = period_size * (i // 8)  # Start by putting the position of the position associated to the period
            j = i % 8  # The index relatively to the period
            bar_y += j / 12 * period_size
            if j >= 2: bar_y += period_size / 6
            if j >= 6: bar_y += period_size / 6

            offset_x = min(f1(bar_y), f2(bar_y))  # Is negative
            bar_x = self.pos.x + offset_x

            bar_size = Vec(-2 * offset_x, 6)

            view.rect(Vec(bar_x, bar_y), bar_size, col)

        # Draw the branches
        draw_func(f1, branch1_col, 6)
        draw_func(f2, branch2_col, 6)

    def dna_clicked(self, pos):
        """
        Returns None if pos is not on the DNA.
        Else, it sends the index of the DNA part touched by pos.
        """
        pos = pos - self.pos
        if -self.WIDTH*0.5 <= pos.x <= self.WIDTH*0.5 and 0 <= pos.y <= self.length:
            nb_periods = len(self.dna) // 8
            period_size = self.length / nb_periods  # The horizontal size of a period
            return int(pos.y / period_size)
        else:
            return None

    