import pygame
import os
import time
import random
pygame.font.init()

#This class will create a game over screen where you can restart the game or quit
class GameOver:

    def __init__(self, window, winner):
        self.window = window
        self.first = winner

    def createGameOverMenu(self):
        pygame.draw.rect(self.window, (255, 255, 255), (128, 192, 256, 128))
        pygame.draw.rect(self.window, (255, 255, 255), (128, 384, 256, 128))
        winner_font = pygame.font.SysFont("comicsans", 90)
        again_font = pygame.font.SysFont("comicsans", 70)
        quit_font = pygame.font.SysFont("comicsans", 90)
        winner = ""
        if self.first:
            winner = "White"
        else:
            winner = "Black"
        winner_label = winner_font.render("Winner is" + " " + winner, 1, (0, 255, 255))
        again_label = again_font.render("Play Again", 1, (0, 0, 0))
        quit_label = quit_font.render("Quit", 1, (0, 0, 0))
        widthWinner = winner_label.get_width()
        heightWinner = winner_label.get_height()
        widthAgain = again_label.get_width()
        heightAgain = again_label.get_height()
        widthQuit = quit_label.get_width()
        heightQuit = quit_label.get_height()
        self.window.blit(again_label, (256 - widthAgain/2, 256 - heightAgain/2))
        self.window.blit(winner_label, (256 - widthWinner / 2, heightWinner / 2))
        self.window.blit(quit_label, (256 - widthQuit/2, 448 - heightQuit/2))

    def gameOverMenu(self, CHESS_BOARD):
        self.window.blit(CHESS_BOARD, (0, 0))
        self.createGameOverMenu()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (x >= 128 and x <= 384) and (y >= 192 and y <= 320):
                    return 1
                elif (x >= 128 and x <= 384) and (y >= 384 and y <= 512):
                    return -1
        return 0