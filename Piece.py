import pygame
import os
import time
import random
pygame.font.init()

class Piece:

    def __init__(self, x, y, image, white):
        self.x = x
        self.y = y
        self.image = image
        self.white = white
        self.coloredRed = False
        self.coloredYellow = False

    def drawImage(self, window):
        xMid = self.x + 32 - (self.image.get_width() / 2)
        yMid = self.y + 32 - (self.image.get_height() / 2)
        window.blit(self.image, (xMid, yMid))


    def toString(self):
        return None
    def isWhite(self):
        return self.white
    def isYellow(self):
        return False
    def isColoredYellow(self):
        return self.coloredYellow
    def isColoredRed(self):
        return self.coloredRed
    def changedToRed(self):
        self.coloredRed = True
    def changedToYellow(self):
        self.coloredYellow = True

    def cleared(self):
        self.coloredRed = False
        self.coloredYellow = False

    def changeImageRed(self):
        self.changedToRed()
    def isAPawn(self):
        return False
    def isKing(self):
        return False
    def changeCord(self, x, y):
        self.x = x * 64
        self.y = y * 64


