import pygame
import os
import time
import random

pygame.font.init()
from Piece import Piece


class Pawn(Piece):

    def __init__(self, x, y, image, notBlack):
        super().__init__(x, y, image, notBlack)
        self.start = True

    def toString(self):
        return "pawn"

    def changeImageWhiteYellow(self):
        WHITE_PAWN_YELLOW = pygame.image.load(os.path.join("pic", "wpy.png"))
        self.image = WHITE_PAWN_YELLOW
        self.changedToYellow()

    def changeImageWhiteRed(self):
        WHITE_PAWN_RED = pygame.image.load(os.path.join("pic", "wpr.png"))
        self.image = WHITE_PAWN_RED
        self.changedToRed()

    def changeImageWhite(self):
        WHITE_PAWN = pygame.image.load(os.path.join("pic", "wp.png"))
        self.image = WHITE_PAWN
        self.cleared()

    def changeImageBlackRed(self):
        BLACK_PAWN_RED = pygame.image.load(os.path.join("pic", "bpr.png"))
        self.image = BLACK_PAWN_RED
        self.changedToRed()

    def changeImageBlack(self):
        BLACK_PAWN = pygame.image.load(os.path.join("pic", "bp.png"))
        self.image = BLACK_PAWN
        self.cleared()

    def changeImageBlackYellow(self):
        BLACK_PAWN_YELLOW = pygame.image.load(os.path.join("pic", "bpy.png"))
        self.image = BLACK_PAWN_YELLOW
        self.changedToYellow()

    def getMoves(self, pieces):
        thisX = int(self.x / 64)
        thisY = int(self.y / 64)
        list = []
        if self.start:
            j = 3
        else:
            j = 2
        i = 1
        while i < j:
            thisX2 = int(thisX)
            if self.isWhite():
                thisY2 = int(thisY - i)
            else:
                thisY2 = int(thisY + i)
            if (thisY2 >= 0 and thisY2 < 8):
                if(pieces[thisY2][thisX2] != None):
                    break
                list.append([thisX2, thisY2])
            i += 1
        if self.isWhite():
            # UpLeft
            x = thisX - 1
            y = thisY - 1
            if (x >= 0 and y >= 0) and (pieces[y][x] != None and not(pieces[y][x].isWhite())):
                list.append([x, y])
            # UpRight
            x = thisX + 1
            y = thisY - 1
            if (x < 8 and y >= 0) and (pieces[y][x] != None and not(pieces[y][x].isWhite())):
                list.append([x, y])
            return list
        else:
            # BottomRight
            x = thisX + 1
            y = thisY + 1
            if (x < 8 and y < 8) and (pieces[y][x] != None and pieces[y][x].isWhite()):
                list.append([x, y])
            # UpRight
            x = thisX - 1
            y = thisY + 1
            if (x >= 0 and y < 8) and (pieces[y][x] != None and pieces[y][x].isWhite()):
                list.append([x, y])
            return list


    def changeImageRed(self):
        BLACK_PAWN_RED = pygame.image.load(os.path.join("pic", "bpy.png"))
        self.image = BLACK_PAWN_RED
        self.changedToRed()
    def changeImageBlack(self):
        BLACK_PAWN = pygame.image.load(os.path.join("pic", "bp.png"))
        self.image = BLACK_PAWN
        self.cleared()

    def isAPawn(self):
        return True

    def hasStarted(self):
        self.start = False

