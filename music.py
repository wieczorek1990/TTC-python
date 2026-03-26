import fluidsynth
import mido

MAIN_MENU_MUSIC = "midi/fh.mid"
GAME_MUSIC = "midi/sob.mid"


class Music:
    def __init__(self, settings):
        self.midi_file = None
        self.settings = settings
        self.synthesizer = self.init_synthesizer()

    def load(self, filename):
        self.midi_file = mido.MidiFile(filename)

    def play(self):
        if not self.settings.music_enabled:
            return

        for msg in self.midi_file.play():
            if msg.type == 'note_on':
                self.synthesizer.noteon(0, msg.note, msg.velocity)
            elif msg.type == 'note_off':
                self.synthesizer.noteoff(0, msg.note)
            elif msg.type == 'program_change':
                self.synthesizer.program_change(0, msg.program)

    def stop(self):
        if not self.settings.music_enabled:
            return

    def init_synthesizer(self):
        synthesizer = fluidsynth.Synth()
        synthesizer.start()
        soundfont = synthesizer.sfload("soundfonts/FluidR3_GM.sf2")
        synthesizer.program_select(0, soundfont, 0, 0)
        return synthesizer
