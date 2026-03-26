import pygame
from games import Game
from music import Music, MAIN_MENU_MUSIC
from settings import Settings
from visualizer import Visualizer


def main():
    running = True

    pygame.init()

    settings = Settings()

    music = Music(settings)
    music.load(MAIN_MENU_MUSIC)
    music.play()

    game = Game()
    visualizer = Visualizer()

    while running:
        game.tick()
        visualizer.draw(game)


if __name__ == "__main__":
    main()
