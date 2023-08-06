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
                if self.rect.collidepoint(event.pos):
                    self.on_click()

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

    def on_click(self):
        self.remove(self.groups)



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