from typing import Sequence, Union
import pygame
from pygame.sprite import AbstractGroup, Sprite
from abc import ABC
from src.spritesheet import SpriteSheet
from config import Config



class Field(pygame.sprite.Group):
    def __init__(self, *sprites: Sprite | Sequence[Sprite]) -> None:
        super().__init__(*sprites)


class Tile(pygame.sprite.Sprite, ABC):
    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)


class GrassTile(Tile):
    def __init__(self, *groups: AbstractGroup, top, left, paddingL, paddingR) -> None:
        super().__init__(*groups)
        self.spritesheet = SpriteSheet("./assets/Tilesets/Grass.png")
        self.image = self.spritesheet.image_at((0, 0, 16, 16))
        self.top =  paddingL+top
        self.left = paddingR+left
        self.bottom = paddingL+top+16
        self.right = paddingR+left+16
        self.rect = (self.top, self.left, self.bottom, self.right)
        #self.image = self.image.copy()
        pygame.draw.rect(self.image, (0, 0, 0), self.image.get_rect(), 2) 

