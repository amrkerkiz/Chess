import pygame
import os
import time
import random

pygame.font.init()
from Piece import Piece


class Knight(Piece):

    def __init__(self, x, y, image, notBlack):
        super().__init__(x, y, image, notBlack)

    def toString(self):
        return "knight"

    def changeImageWhiteYellow(self):
        WHITE_KNIGHT_YELLOW = pygame.image.load(os.path.join("pic", "wNy.png"))
        self.image = WHITE_KNIGHT_YELLOW
        self.changedToYellow()

    def changeImageWhiteRed(self):
        WHITE_KNIGHT_RED = pygame.image.load(os.path.join("pic", "wNr.png"))
        self.image = WHITE_KNIGHT_RED
        self.changedToRed()

    def changeImageWhite(self):
        WHITE_KNIGHT = pygame.image.load(os.path.join("pic", "wN.png"))
        self.image = WHITE_KNIGHT
        self.cleared()
    def changeImageBlackRed(self):
        BLACK_KNIGHT_RED = pygame.image.load(os.path.join("pic", "bNr.png"))
        self.image = BLACK_KNIGHT_RED
        self.changedToRed()
    def changeImageBlack(self):
        BLACK_KNIGHT = pygame.image.load(os.path.join("pic", "bN.png"))
        self.image = BLACK_KNIGHT
        self.cleared()
    def changeImageBlackYellow(self):
        BLACK_KNIGHT_YELLOW = pygame.image.load(os.path.join("pic", "bNy.png"))
        self.image = BLACK_KNIGHT_YELLOW
        self.changedToYellow()

    def getMoves(self, pieces):
        thisX = int(self.x / 64)
        thisY = int(self.y / 64)
        list = []
        # TopRight
        x = thisX + 1
        y = thisY - 2
        if x < 8 and y >= 0:
            list.append([x, y])

        # UpRight
        x = thisX + 2
        y = thisY - 1
        if x < 8 and y >= 0:
            list.append([x, y])

        # DownRight
        x = thisX + 2
        y = thisY + 1
        if x < 8 and y < 8:
            list.append([x, y])

        # BottomRight
        x = thisX + 1
        y = thisY + 2
        if x < 8 and y < 8:
            list.append([x, y])

        # TopLeft
        x = thisX - 1
        y = thisY - 2
        if x >= 0 and y >= 0:
            list.append([x, y])

        # UpLeft
        x = thisX - 2
        y = thisY - 1
        if x >= 0 and y >= 0:
            list.append([x, y])

        # DownLeft
        x = thisX - 2
        y = thisY + 1
        if x >= 0 and y < 8:
            list.append([x, y])

        # BottomRight
        x = thisX - 1
        y = thisY + 2
        if x >= 0 and y < 8:
            list.append([x, y])
        return list
