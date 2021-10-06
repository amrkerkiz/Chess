import pygame
import os
import time
import random
pygame.font.init()
from Piece import Piece

class Bishop(Piece):

    def __init__(self, x, y, image, notBlack):
        super().__init__(x, y, image, notBlack)

    def toString(self):
        return "bishop"

    def changeImageWhiteYellow(self):
        WHITE_BISHOP_YELLOW = pygame.image.load(os.path.join("pic", "wBy.png"))
        self.image = WHITE_BISHOP_YELLOW
        self.changedToYellow()

    def changeImageWhiteRed(self):
        WHITE_BISHOP_RED = pygame.image.load(os.path.join("pic", "wBr.png"))
        self.image = WHITE_BISHOP_RED
        self.changedToRed()

    def changeImageWhite(self):
        WHITE_BISHOP = pygame.image.load(os.path.join("pic", "wB.png"))
        self.image = WHITE_BISHOP
        self.cleared()

    def changeImageBlackRed(self):
        BLACK_BISHOP_RED = pygame.image.load(os.path.join("pic", "bBr.png"))
        self.image = BLACK_BISHOP_RED
        self.changedToRed()

    def changeImageBlack(self):
        BLACK_BISHOP = pygame.image.load(os.path.join("pic", "bB.png"))
        self.image = BLACK_BISHOP
        self.cleared()

    def changeImageBlackYellow(self):
        BLACK_BISHOP_YELLOW = pygame.image.load(os.path.join("pic", "bBy.png"))
        self.image = BLACK_BISHOP_YELLOW
        self.changedToYellow()

    def getMoves(self, pieces):
        thisX = int(self.x / 64)
        thisY = int(self.y / 64)
        list = []
        #UpRight
        x = thisX + 1
        y = thisY - 1
        while x < 8 and y >= 0:
            if pieces[y][x] == None:
                list.append([x, y])
                y = y - 1
                x = x + 1
            else:
                list.append([x, y])
                break

        # DownRight
        x = thisX + 1
        y = thisY + 1
        while x < 8 and y < 8:
            if pieces[y][x] == None:
                list.append([x, y])
                y = y + 1
                x = x + 1
            else:
                list.append([x, y])
                break
        # DownLeft
        x = thisX - 1
        y = thisY + 1
        while x >= 0 and y < 8:
            if pieces[y][x] == None:
                list.append([x, y])
                y = y + 1
                x = x - 1
            else:
                list.append([x, y])
                break
        #UpLeft
        x = thisX - 1
        y = thisY - 1
        while x >= 0 and y >= 0:
            if pieces[y][x] == None:
                list.append([x, y])
                y = y - 1
                x = x - 1
            else:
                list.append([x, y])
                break
        return list
