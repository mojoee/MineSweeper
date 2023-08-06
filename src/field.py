from typing import Sequence, Union
import pygame
from pygame.sprite import AbstractGroup, Sprite
from abc import ABC
from src.spritesheet import SpriteSheet
from config import Config



class Field(pygame.sprite.Group):
    def __init__(self, *sprites: Sprite | Sequence[Sprite]) -> None:
        super().__init__(*sprites)


class Minions(pygame.sprite.Group):
    def __init__(self, *sprites: Sprite | Sequence[Sprite]) -> None:
        super().__init__(*sprites)


class Tile(pygame.sprite.Sprite, ABC):
    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button ==1:
                    if self.rect.collidepoint(event.pos):
                        self.on_click()
                elif event.button == 3:
                    if self.rect.collidepoint(event.pos):
                        self.draw_text(self.bombs)

    def on_click(self):
        pass


class GrassTile(Tile):
    def __init__(self, *groups: AbstractGroup, top, left, paddingH, paddingV) -> None:
        super().__init__(*groups)
        self.spritesheet = SpriteSheet("./assets/Tilesets/Grass.png")
        self.groups = groups
        self.width = 16
        self.image = self.spritesheet.image_at((0, 0, 16, 16))
        self.top = paddingH+top
        self.left = paddingV+left
        self.bottom = top+self.width
        self.right = left+self.width
        self.rect = pygame.Rect(self.top, self.left, self.width, self.width)
        # self.image = self.image.copy()
        pygame.draw.rect(self.image, (0, 0, 0), self.image.get_rect(), Config.borderWidth)
        self.clicked = False
        self.font = pygame.font.SysFont("Arial", 12)

    def on_click(self):
        self.remove(self.groups)

    def on_right_click(self):
        # need to count how many bombs around
        pass

    def draw_text(self, text):
        self.textSurf = self.font.render(str(text), 1, (0, 0, 0))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [self.width/2 - W/2, self.width/2 - H/2])

    def add_bombs(self, bomb):
        self.bombs = bomb

class Minion(Tile):
    def __init__(self, *groups: AbstractGroup, top, left, paddingL, paddingR) -> None:
        super().__init__(*groups)
        self.spritesheet = SpriteSheet("./assets/Objects/Egg.png")
        self.image = self.spritesheet.image_at((0, 0, 16, 16))
        self.top = paddingL+top
        self.left = paddingR+left
        self.bottom = paddingL+top+16
        self.right = paddingR+left+16
        self.rect = pygame.Rect(self.top, self.left, self.bottom, self.right)