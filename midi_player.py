import pygame


class MidiPlayer:
    def __init__(self, midi_file=""):
        super().__init__()
        self.midi_file = midi_file

    def play(self):
        pygame.init()
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            pygame.quit()
            pygame.init()

        pygame.mixer.music.load(self.midi_file)
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                print("Music stopped playing.")
                break
