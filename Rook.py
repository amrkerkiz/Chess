import pygame
import os
import time
import random

pygame.font.init()
from Piece import Piece


class Rook(Piece):

    def __init__(self, x, y, image, notBlack):
        super().__init__(x, y, image, notBlack)

    def toString(self):
        return "rook"

    def changeImageWhiteYellow(self):
        WHITE_ROOK_YELLOW = pygame.image.load(os.path.join("pic", "wRy.png"))
        self.image = WHITE_ROOK_YELLOW
        self.changedToYellow()

    def changeImageWhiteRed(self):
        WHITE_ROOK_RED = pygame.image.load(os.path.join("pic", "wRr.png"))
        self.image = WHITE_ROOK_RED
        self.changedToRed()

    def changeImageWhite(self):
        WHITE_ROOK = pygame.image.load(os.path.join("pic", "wR.png"))
        self.image = WHITE_ROOK
        self.cleared()

    def changeImageBlackRed(self):
        BLACK_ROOK_RED = pygame.image.load(os.path.join("pic", "bRr.png"))
        self.image = BLACK_ROOK_RED
        self.changedToRed()

    def changeImageBlack(self):
        BLACK_ROOK_YELLOW = pygame.image.load(os.path.join("pic", "bR.png"))
        self.image = BLACK_ROOK_YELLOW
        self.cleared()

    def changeImageBlackYellow(self):
        BLACK_ROOK = pygame.image.load(os.path.join("pic", "bRy.png"))
        self.image = BLACK_ROOK
        self.changedToYellow()


    def getMoves(self, pieces):
        thisX = int(self.x / 64)
        thisY = int(self.y / 64)
        list = []
        #Down
        x = thisX
        y = thisY + 1
        while y < 8:
            if pieces[y][x] == None:
                list.append([x, y])
                y = y + 1
            else:
                list.append([x, y])
                break
        # Up
        x = thisX
        y = thisY - 1
        while y >= 0:
            if pieces[y][x] == None:
                list.append([x, y])
                y = y - 1
            else:
                list.append([x, y])
                break
        # Right
        x = thisX + 1
        y = thisY
        while x < 8:
            if pieces[y][x] == None:
                list.append([x, y])
                x = x + 1
            else:
                list.append([x, y])
                break
        # Left
        x = thisX - 1
        y = thisY
        while x >= 0:
            if pieces[y][x] == None:
                list.append([x, y])
                x = x - 1
            else:
                list.append([x, y])
                break
        return list
