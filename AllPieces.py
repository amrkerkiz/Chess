import pygame
import os
import time
import random
pygame.font.init()
from King import King
from Queen import Queen
from Knight import Knight
from Pawn import Pawn
from Bishop import Bishop
from Rook import Rook


class AllPieces:


    def __init__(self, wk, wq, wkn, wp, wr, wb, bk, bq, bkn, bp ,br, bb):
        self.gameBoard = [
            [Rook(0, 0, br, False), Knight(64, 0, bkn, False), Bishop(128, 0, bb, False), Queen(192, 0, bq, False),
             King(256, 0, bk, False), Bishop(320, 0, bb, False), Knight(384, 0, bkn, False), Rook(448, 0, br, False)],
            [Pawn(0, 64, bp, False), Pawn(64, 64, bp, False), Pawn(128, 64, bp, False), Pawn(192, 64, bp, False),
             Pawn(256, 64, bp, False), Pawn(320, 64, bp, False), Pawn(384, 64, bp, False), Pawn(448, 64, bp, False)],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn(0, 384, wp, True), Pawn(64, 384, wp, True), Pawn(128, 384, wp, True),
             Pawn(192, 384, wp, True), Pawn(256, 384, wp, True), Pawn(320, 384, wp, True),
             Pawn(384, 384, wp, True), Pawn(448, 384, wp, True)],
            [Rook(0, 448, wr, True), Knight(64, 448, wkn, True), Bishop(128, 448, wb, True),
             Queen(192, 448, wq, True), King(256, 448, wk, True), Bishop(320, 448, wb, True),
             Knight(384, 448, wkn, True), Rook(448, 448, wr, True)]
        ]

    def getBoard(self):
        return self.gameBoard


