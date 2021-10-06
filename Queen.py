import pygame
import os
import time
import random

pygame.font.init()
from Piece import Piece


class Queen(Piece):

    def __init__(self, x, y, image, notBlack):
        super().__init__(x, y, image, notBlack)

    def toString(self):
        return "queen"

    def changeImageWhiteYellow(self):
        WHITE_QUEEN_YELLOW = pygame.image.load(os.path.join("pic", "wQy.png"))
        self.image = WHITE_QUEEN_YELLOW
        self.changedToYellow()

    def changeImageWhiteRed(self):
        WHITE_QUEEN_RED = pygame.image.load(os.path.join("pic", "wQr.png"))
        self.image = WHITE_QUEEN_RED
        self.changedToRed()

    def changeImageWhite(self):
        WHITE_QUEEN = pygame.image.load(os.path.join("pic", "wQ.png"))
        self.image = WHITE_QUEEN
        self.cleared()

    def changeImageBlackRed(self):
        BLACK_QUEEN_RED = pygame.image.load(os.path.join("pic", "bQr.png"))
        self.image = BLACK_QUEEN_RED
        self.changedToRed()

    def changeImageBlack(self):
        BLACK_QUEEN = pygame.image.load(os.path.join("pic", "bQ.png"))
        self.image = BLACK_QUEEN
        self.cleared()

    def changeImageBlackYellow(self):
        BLACK_QUEEN_YELLOW = pygame.image.load(os.path.join("pic", "bQy.png"))
        self.image = BLACK_QUEEN_YELLOW
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
        # Down
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