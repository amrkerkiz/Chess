import pygame
import os
import time
import random
pygame.font.init()

#This class will create a main menu for the chess game
class MainMenu:

    def __init__(self, window):
        self.window = window

    def createMainMenu(self):
        pygame.draw.rect(self.window, (255, 255, 255), (128, 64, 256, 128))
        pygame.draw.rect(self.window, (255, 255, 255), (128, 320, 256, 128))
        start_font = pygame.font.SysFont("comicsans", 115)
        quit_font = pygame.font.SysFont("comicsans", 115)
        start_label = start_font.render("Start", 1, (0, 0, 0))
        quit_label = quit_font.render("Quit", 1, (0, 0, 0))
        widthStart = start_label.get_width()
        heightStart = start_label.get_height()
        widthQuit = quit_label.get_width()
        heightQuit = quit_label.get_height()
        self.window.blit(start_label, (256 - widthStart/2, 128 - heightStart/2))
        self.window.blit(quit_label, (256 - widthQuit/2, 384 - heightQuit/2))