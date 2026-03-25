#!/bin/sh
# Installs pygame with dependencies.

brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf pkg-config portmidi
pip3 install --break-system-packages pygame pygame-menu
