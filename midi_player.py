import pygame


class MidiPlayer:
    def __init__(self, midi_file=""):
        super().__init__()
        self.midi_file = midi_file

    def play(self):
        pygame.init()
        pygame.mixer.music.load(self.midi_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
