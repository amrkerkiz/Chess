import pygame
import os
import time
import random

pygame.font.init()
import math
from Yellow import Yellow
from Queen import Queen

class Game:


    def __init__(self, board, allPieces, window):
        self.board = board
        self.pieces = allPieces
        self.first = True
        self.window = window
        self.previousRow = -1
        self.previousCol = -1
        self.didntQuit = True

    def clearBoxes(self, listOfPieces):
        for row in range(8):
            for col in range(8):
                if listOfPieces[row][col] != None:
                    if listOfPieces[row][col].isYellow():
                        listOfPieces[row][col] = None
                    elif listOfPieces[row][col].isColoredRed() or listOfPieces[row][col].isColoredYellow():
                        if listOfPieces[row][col].isWhite():
                            listOfPieces[row][col].changeImageWhite()
                        else:
                            listOfPieces[row][col].changeImageBlack()

    def colorMoves(self, listOfPieces, y, x):
        listOfMoves = listOfPieces[y][x].getMoves(listOfPieces)
        YELLOW = pygame.image.load(os.path.join("pic", "yellow.png"))
        for moves in listOfMoves:
            x2 = moves[0]
            y2 = moves[1]
            if listOfPieces[y2][x2] == None:
                yel = Yellow(x2 * 64, y2 * 64, YELLOW)
                listOfPieces[y2][x2] = yel
            elif not(listOfPieces[y2][x2].isWhite()) and self.first:
                listOfPieces[y2][x2].changeImageBlackRed()
            elif listOfPieces[y2][x2].isWhite() and not(self.first):
                listOfPieces[y2][x2].changeImageWhiteRed()


    def playerTurn(self, listOfPieces):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.didntQuit = False
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                col, row = pygame.mouse.get_pos()
                col /= 64
                col = math.floor(col)
                row /= 64
                row = math.floor(row)
                if listOfPieces[row][col] != None:
                    piece = listOfPieces[row][col]
                    if self.first:
                        if not (piece.isWhite()) and not (piece.isColoredRed()) and not (piece.isColoredYellow()):
                            break
                        if piece.isColoredRed() or piece.isYellow():
                            gameOver = piece.isKing()
                            self.clearBoxes(listOfPieces)
                            if listOfPieces[self.previousRow][self.previousCol].isAPawn():
                                listOfPieces[self.previousRow][self.previousCol].hasStarted()
                                if row == 0:
                                    listOfPieces[self.previousRow][self.previousCol] = Queen(self.previousRow * 64,
                                        self.previousCol * 64, pygame.image.load(os.path.join("pic", "wQ.png")), True)
                            listOfPieces[row][col] = listOfPieces[self.previousRow][self.previousCol]
                            listOfPieces[row][col].changeCord(col, row)
                            listOfPieces[self.previousRow][self.previousCol] = None
                            listOfPieces[row][col].changeImageWhite()
                            if(gameOver):
                                return False
                            self.first = not(self.first)
                            col = -1
                            row = -1
                        elif piece.isWhite() and not(piece.isColoredYellow()):
                            self.clearBoxes(listOfPieces)
                            piece.changeImageWhiteYellow()
                            self.colorMoves(listOfPieces, row, col)
                        self.previousCol = col
                        self.previousRow = row
                    elif not(self.first):
                        if piece.isWhite() and not (piece.isColoredRed()) and not (piece.isColoredYellow()):
                            break
                        if piece.isColoredRed() or piece.isYellow():
                            gameOver = piece.isKing()
                            if listOfPieces[self.previousRow][self.previousCol].isAPawn():
                                listOfPieces[self.previousRow][self.previousCol].hasStarted()
                                if row == 7:
                                    listOfPieces[self.previousRow][self.previousCol] = Queen(self.previousCol * 64,
                                        self.previousRow * 64, pygame.image.load(os.path.join("pic", "bQ.png")), False)
                            self.clearBoxes(listOfPieces)
                            listOfPieces[row][col] = listOfPieces[self.previousRow][self.previousCol]
                            listOfPieces[row][col].changeCord(col, row)
                            listOfPieces[self.previousRow][self.previousCol] = None
                            listOfPieces[row][col].changeImageBlack()
                            if (gameOver):
                                return False
                            self.first = not (self.first)
                            col = -1
                            row = -1
                        elif not(piece.isWhite()) and not(piece.isColoredYellow()):
                            self.clearBoxes(listOfPieces)
                            piece.changeImageBlackYellow()
                            self.colorMoves(listOfPieces, row, col)
                        self.previousCol = col
                        self.previousRow = row
        return True

    def runGame(self):
        run = True
        while run:
            self.window.blit(self.board, (0, 0))
            listOfPieces = self.pieces.getBoard()
            for line in listOfPieces:
                for piece in line:
                    if piece != None:
                        piece.drawImage(self.window)
            run = self.playerTurn(listOfPieces)
            pygame.display.update()
        return False

    def getWinner(self):
        return self.first

    def didNotQuit(self):
        return self.didntQuit
