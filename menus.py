import pygame_menu

from constants import NAME, WIDTH, HEIGHT, THEME
from actions import game, settings, set_music, settings_exit


def generate_main_menu():
    menu = pygame_menu.Menu(NAME, WIDTH, HEIGHT, theme=THEME)
    menu.add.button("Start game", game)
    menu.add.button("Edit settings", settings)
    menu.add.button("Exit game", pygame_menu.events.EXIT)
    return menu


def generate_settings_menu():
    menu = pygame_menu.Menu("TTC Settings", WIDTH, HEIGHT, theme=THEME)
    menu.add.selector("Music: ", [("ON", True), ("OFF", False)], onchange=set_music)
    menu.add.button("Exit", settings_exit)
    return menu
