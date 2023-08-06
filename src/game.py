import pygame
from src.field import Field, GrassTile
from config import Config

class Game():
    def __init__(self, n, screen) -> None:
        self.field = None
        self.alive = True
        self.screen = screen
        self.paddingH = Config.screenResolution[0]/2-n/2*16
        self.paddingV = Config.screenResolution[1]/2-n/2*16

        self.setup(n)

    def setup(self, n):
        self.field = Field()
        for i in range(n):
            for j in range(n):
                GrassTile(self.field, top=i*16, left=j*16, paddingL=self.paddingH, paddingR=self.paddingV)
        self.field.draw(self.screen)



    def game_over(self):
        self.alive = False