import pygame
import pygame_menu

NAME = "TRIPLE TRIAD CONSOLE"
WIDTH, HEIGHT = 800, 600
HALF_WIDTH, HALF_HEIGHT = WIDTH / 2, HEIGHT / 2


def play():
    pass


def settings():
    pass


def setup_menu():
    menu = pygame_menu.Menu(NAME, WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button("Play", play)
    menu.add.button("Settings", settings)
    menu.add.button("Quit", pygame_menu.events.EXIT)
    return menu


def main():
    pygame.init()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    menu = setup_menu()
    menu.mainloop(surface)


if __name__ == "__main__":
    main()
