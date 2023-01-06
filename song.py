import random

from ensemble import Ensemble
from instrument import Instrument
from midi_generator import MidiGenerator


class Song:
    def __init__(self, random_song=False, seed=None):

        # chords = list(range(35, 82))
        # chords.append(" ")
        # chords = ["Am", "F", "C", "G", "a", "f", "g", "c", " "]
        chords = ["c", "d", "e", "g", "a", " "]
        # chords = ["c#", "d", "d#", "f#", "g", "a", " "]
        # chords += list(MidiGenerator.chords.keys())
        drumsnote = list(range(35, 82))
        drumsnote.append(" ")
        drumkits = [0, 8, 16, 24, 25, 32, 40]

        if seed is None:
            print("noSeed")
            seed = random.randrange(99999999)

        self.seed = seed
        print("seed : ", self.seed)
        random.seed(self.seed)
        self.ensemble = Ensemble()
        weights = [1] * len(chords)
        weights[len(weights) - 1] = 3 * int(len(weights) / 4)
        times = int(random.random() * 10) + 4
        if random_song:
            instruments_number = int(random.random() * 4) + 2
            note_number = (int(random.random() * 4) + 4) * (int(random.random() * 2) + 2)
            for i in range(instruments_number):
                program = int(random.random() * 128)
                volume = int(random.random() * 50) + 20
                score = ""
                for note in random.choices(chords, weights=weights, k=note_number):
                    score += str(note) + " "
                self.ensemble.append(Instrument(Instrument.MELODIC, program, volume, score * times))
            volume = int(random.random() * 50) + 20
            program = random.choice(drumkits)
            score = ""
            weights = []
            for i in range(len(drumsnote)):
                weights.append(1)
            weights[len(weights) - 1] = len(weights)
            for note in random.choices(drumsnote, weights=weights, k=note_number):
                score += str(note) + " "
            self.ensemble.append(Instrument(Instrument.PERCUSSIVE, program, volume, score * times))
