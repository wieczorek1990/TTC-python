import pygame
import pygame_menu

NAME = "TRIPLE TRIAD CONSOLE"
WIDTH, HEIGHT = 800, 600
HALF_WIDTH, HALF_HEIGHT = WIDTH / 2, HEIGHT / 2
THEME = pygame_menu.themes.THEME_BLUE

MUSIC = True
SURFACE = None


def set_music(choices, choice):
    MUSIC = choice


def play():
    pass


def settings():
    menu = settings_menu()
    menu.mainloop(SURFACE)


def settings_exit():
    setup_menu()


def setup_menu():
    SURFACE = get_surface()
    menu = pygame_menu.Menu(NAME, WIDTH, HEIGHT, theme=THEME)
    menu.add.button("Play", play)
    menu.add.button("Settings", settings)
    menu.add.button("Exit", pygame_menu.events.EXIT)
    menu.mainloop(SURFACE)
    return menu


def settings_menu():
    SURFACE = get_surface()
    menu = pygame_menu.Menu("TTC Settings", WIDTH, HEIGHT, theme=THEME)
    menu.add.selector("Music: ", [("ON", True), ("OFF", False)], onchange=set_music)
    menu.add.button("Exit", settings_exit)
    menu.mainloop(SURFACE)
    return menu


def get_surface():
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    return surface


def main():
    pygame.init()
    menu = setup_menu()


if __name__ == "__main__":
    main()
