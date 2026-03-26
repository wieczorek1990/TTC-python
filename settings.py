from py_singleton import singleton


@singleton
class Settings:
    music_enabled: bool

    def __init__(self):
        self.music_enabled = True

    def set_music(self, _, choice):
        self.music_enabled = choice
