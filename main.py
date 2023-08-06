# Example file showing a basic pygame "game loop"
import pygame
from config import Config
from src.game import Game

# pygame setup
pygame.init()
screen = pygame.display.set_mode(Config.screenResolution)
clock = pygame.time.Clock()
running = True
config = Config()

#game setup
game = Game(config.fieldSize, screen)

while game.alive:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.game_over()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(Config.BGColor)
    game.field.draw(screen)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()