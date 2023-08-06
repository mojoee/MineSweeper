import pygame
from src.field import Field, Minions, GrassTile, Minion
from config import Config
import random

class Game():
    def __init__(self, n, screen) -> None:
        self.field = None
        self.minions = None
        self.alive = True
        self.screen = screen
        self.paddingH = Config.screenResolution[0]/2-n/2*16
        self.paddingV = Config.screenResolution[1]/2-n/2*16
        self.clock = pygame.time.Clock()
        self.clockFont = pygame.font.SysFont(Config.clockFont, 30)
        self.setup(n)

    def setup(self, n):
        self.field = Field()
        self.minions = Minions()
        for i in range(n):
            for j in range(n):
                minionHide = (random.random() > Config.bombPerc)
                GrassTile(self.field, top=i*16, left=j*16,
                          paddingH=self.paddingH, paddingV=self.paddingV)
                if minionHide:
                    Minion(self.minions, top=i*16, left=j*16,
                           paddingL=self.paddingH, paddingR=self.paddingV)

        self.field.draw(self.screen)


    def game_over(self):
        self.alive = False