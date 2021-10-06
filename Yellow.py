import pygame
import os
import time
import random

pygame.font.init()
from Piece import Piece


class Yellow(Piece):

    def __init__(self, x, y, image):
        super().__init__(x, y, image, True)
        self.coloredYellow = True
    def isYellow(self):
        return True