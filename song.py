from random import random, choice

from midi_generator import MidiGenerator


class Song:
    def __init__(self, random_song=False):
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
            instruments_number = int(random() * 3) + 1
            for i in range(instruments_number):
                score = ""
                for note_index in range(int(random() * 10) + 4):
                    score += choice(chords) + (" " * (int(random() * 4) + 1))

                    print(score)
                self.instruments[int(random() * 128) + 1] = {"score": score * (int(random() * 4) + 1),
                                                             "volume": int(random() * 40) + 20}
