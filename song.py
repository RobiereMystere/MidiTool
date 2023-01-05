import random

from midi_generator import MidiGenerator


class Song:
    def __init__(self, random_song=False):
        self.seed = 13101991
        random.seed(self.seed)
        self.instruments = {}
        chords = list(MidiGenerator.chords.keys())
        if not random_song:
            epiano = "Em    Am    D7    B7    Em    C    Am    B7    Em    Am    D7    B7    Em    C    Am    B7    Em    " \
                     "Am    D7    B7    Em    C    Am    B7    stop "
            piano = " e    a    d    b    e    c    a    b    e    a    d    b    e    c    a    b    e    a" \
                    "    d    b    e    c    a    b    stop "
            violon = "  e    a    d    b    e    c    a    b    e    a    d    b    e    c    a    b    e    a" \
                     "    d    b    e    c    a    b    stop "
            self.instruments = {
                4: {"score": epiano, "volume": 40},
                1: {"score": piano, "volume": 30},
                51: {"score": violon, "volume": 20},
            }

        else:
            instruments_number = int(random.random() * 3) + 1
            for i in range(instruments_number):
                score = ""
                for note_index in range(int(random.random() * 10) + 4):
                    score += random.choice(chords) + (" " * (int(random.random() * 4) + 1))

                    print(score)
                self.instruments[int(random.random() * 128) + 1] = {"score": score * (int(random.random() * 10) + 3),
                                                                    "volume": int(random.random() * 40) + 20}
