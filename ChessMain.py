import pygame
import os
import time
import random
pygame.font.init()
from MainMenu import MainMenu
from GameOver import GameOver
from Game import Game
from AllPieces import AllPieces



#Setting up Display
WIDTH, HEIGHT = 512, 512
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

#Board
CHESS_BOARD = pygame.image.load(os.path.join("pic", "Chess-Board.png"))

#White Pieces
WHITE_KING = pygame.image.load(os.path.join("pic", "wK.png"))
WHITE_QUEEN = pygame.image.load(os.path.join("pic", "wQ.png"))
WHITE_ROOK = pygame.image.load(os.path.join("pic", "wR.png"))
WHITE_PAWN = pygame.image.load(os.path.join("pic", "wp.png"))
WHITE_KNIGHT = pygame.image.load(os.path.join("pic", "wN.png"))
WHITE_BISHOP = pygame.image.load(os.path.join("pic", "wB.png"))

#Black Pieces
BLACK_KING = pygame.image.load(os.path.join("pic", "bK.png"))
BLACK_QUEEN = pygame.image.load(os.path.join("pic", "bQ.png"))
BLACK_ROOK = pygame.image.load(os.path.join("pic", "bR.png"))
BLACK_PAWN = pygame.image.load(os.path.join("pic", "bp.png"))
BLACK_KNIGHT = pygame.image.load(os.path.join("pic", "bN.png"))
BLACK_BISHOP = pygame.image.load(os.path.join("pic", "bB.png"))

#Creating a main menu object
menu = MainMenu(WIN)


#This function creates the main menu for the game, and checks to see if the user clicks start or quit
def main():
    WIN.blit(CHESS_BOARD, (0, 0))
    menu.createMainMenu()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return -1
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if (x >= 128 and x <= 384) and (y >= 64 and y <= 192):
                return 1
            elif (x >= 128 and x <= 384) and (y >= 320 and y <= 448):
                return -1
    return 0

running = True
mainmenu = 0
curGame = True
didNotQuit = True
winner = True
startOver = 0

# Runs the program, opening up the main menu,
# followed by running the game of chess where two players have a 1 v 1
# and has a Game over screen where it displays the winner and gives the option to play again
# All while making sure the app properly closes
while running:
    if mainmenu == 0:
        mainmenu = main()
        if mainmenu == -1:
            running = False
    elif curGame:
        pieceList = AllPieces(WHITE_KING, WHITE_QUEEN, WHITE_KNIGHT, WHITE_PAWN, WHITE_ROOK, WHITE_BISHOP, BLACK_KING,
                              BLACK_QUEEN, BLACK_KNIGHT, BLACK_PAWN, BLACK_ROOK, BLACK_BISHOP)
        game = Game(CHESS_BOARD, pieceList, WIN)
        curGame = game.runGame()
        winner = game.getWinner()
        didNotQuit = game.didNotQuit()
        if not(didNotQuit):
            running = False
    elif startOver == 1:
        curGame = True
        startOver = 0
    elif startOver == 0:
        ending = GameOver(WIN, winner)
        startOver = ending.gameOverMenu(CHESS_BOARD)
    else:
        running = False



