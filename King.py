import pygame
import os
import time
import random

pygame.font.init()
from Piece import Piece


class King(Piece):

    def __init__(self, x, y, image, notBlack):
        super().__init__(x, y, image, notBlack)

    def toString(self):
        return "king"

    def changeImageWhiteYellow(self):
        WHITE_KING_YELLOW = pygame.image.load(os.path.join("pic", "wKy.png"))
        self.image = WHITE_KING_YELLOW
        self.changedToYellow()

    def changeImageWhiteRed(self):
        WHITE_KING_YELLOW = pygame.image.load(os.path.join("pic", "wKr.png"))
        self.image = WHITE_KING_YELLOW
        self.changedToRed()

    def changeImageWhite(self):
        WHITE_KING = pygame.image.load(os.path.join("pic", "wK.png"))
        self.image = WHITE_KING
        self.cleared()

    def changeImageBlackRed(self):
        BLACK_KING_RED = pygame.image.load(os.path.join("pic", "bKr.png"))
        self.image = BLACK_KING_RED
        self.changedToRed()

    def changeImageBlack(self):
        BLACK_KING = pygame.image.load(os.path.join("pic", "bK.png"))
        self.image = BLACK_KING
        self.cleared()

    def changeImageBlackYellow(self):
        BLACK_KING_YELLOW = pygame.image.load(os.path.join("pic", "bKy.png"))
        self.image = BLACK_KING_YELLOW
        self.changedToYellow()

    def isKing(self):
        return True

    def getMoves(self, pieces):
        thisX = self.x / 64
        thisY = self.y / 64
        list = []
        for i in range(-1, 2):
            for z in range(-1, 2):
                thisX2 = int(thisX) + i
                thisY2 = int(thisY) + z
                if (thisX2 >= 0 and thisX2 < 8) and (thisY2 >= 0 and thisY2 < 8):
                    if not(i == 0 and z == 0):
                        list.append([thisX2, thisY2])
        return list