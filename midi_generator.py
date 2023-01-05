from midiutil import MIDIFile

from loglib import log


class MidiGenerator:
    notes = {
        "A": 21,
        "A#": 22,
        "BB": 22,
        "B": 23,
        "C": 24,
        "C#": 25,
        "CB": 25,
        "D": 26,
        "D#": 27,
        "EB": 27,
        "E": 28,
        "F": 29,
        "F#": 30,
        "GB": 30,
        "G": 31,
        "G#": 32,
        "AB": 32
    }
    chords = {
        "A": ["A", "C#", "E"],
        "Am": ["A", "C", "E"],
        "B": ["B", "D#", "F#"],
        "Bm": ["B", "D", "F#"],
        "C": ["C", "E", "G"],
        "Cm": ["C", "Eb", "G"],
        "D": ["D", "F#", "A"],
        "Dm": ["D", "F", "A"],
        "E": ["E", "G#", "B"],
        "Em": ["E", "G", "B"],
        "F": ["F", "A", "C"],
        "Fm": ["F", "Ab", "C"],
        "G": ["G", "B", "D"],
        "Gm": ["G", "Bb", "D"],
        "A#": ["A#", "D", "F"],
        "A#m": ["A#", "C#", "F"],
        "C#": ["C#", "F#", "G#"],
        "C#m": ["C#", "F", "G#"],
        "D#": ["D#", "G", "A#"],
        "D#m": ["D#", "F#", "A#"],
        "F#": ["F#", "A#", "C#"],
        "F#m": ["F#", "A", "C#"],
        "G#": ["G#", "C#", "D#"],
        "G#m": ["G#", "C", "D#"],
        "A7": ["A", "C#", "E", "G"],
        "Am7": ["A", "C", "E", "G"],
        "B7": ["B", "D#", "F#", "A"],
        "Bm7": ["B", "D", "F#", "A"],
        "C7": ["C", "E", "G", "Bb"],
        "Cm7": ["C", "Eb", "G", "Bb"],
        "D7": ["D", "F#", "A", "C"],
        "Dm7": ["D", "F", "A", "C"],
        "E7": ["E", "G#", "B", "D"],
        "Em7": ["E", "G", "B", "D"],
        "F7": ["F", "A", "C", "Eb"],
        "Fm7": ["F", "Ab", "C", "Eb"],
        "G7": ["G", "B", "D", "F"],
        "Gm7": ["G", "Bb", "D", "F"],
        "G#7": ["G#", "C#", "D#", "F#"],
        "G#m7": ["G#", "C", "D#", "F#"],
        "Aadd9": ["A", "C#", "E", "B"],
        "Amadd9": ["A", "C", "E", "B"],
        "Badd9": ["B", "D#", "F#", "C#"],
        "Bmadd9": ["B", "D", "F#", "C#"],
        "Cadd9": ["C", "E", "G", "D"],
        "Cmadd9": ["C", "Eb", "G", "D"],
        "Dadd9": ["D", "F#", "A", "E"],
        "Dmadd9": ["D", "F", "A", "E"],
        "Eadd9": ["E", "G#", "B", "F#"],
        "Emadd9": ["E", "G", "B", "F#"],
        "Fadd9": ["F", "A", "C", "G"],
        "Fmadd9": ["F", "Ab", "C", "G"],
        "Gadd9": ["G", "B", "D", "A"],
        "Gmadd9": ["G", "Bb", "D", "A"],
        "A#add9": ["A#", "D", "F", "C"],
        "A#madd9": ["A#", "C", "F", "C"],
        "C#add9": ["C#", "F#", "G#", "D"],
        "C#madd9": ["C#", "F", "G#", "D"],
        "D#add9": ["D#", "G", "A#", "E"],
        "D#madd9": ["D#", "F#", "A#", "E"],
        "F#add9": ["F#", "A#", "C#", "G"],
        "F#madd9": ["F#", "A", "C#", "G"],
        "G#add9": ["G#", "C#", "D#", "A"],
        "G#madd9": ["G#", "C", "D#", "A"]
    }

    def __init__(self, config=None):
        super().__init__()
        self.time = 0
        if config is not None:
            self.track_number = config.track_number
            self.channel_number = config.channel_number
            self.instruments = config.instruments
            self.tempo = config.tempo
            self.default_volume = config.default_volume
        else:
            self.default_volume = 20
            self.track_number = 1
            self.channel_number = 1
            self.instruments = {1: "Piano"}
            self.tempo = 120

        self.midi = MIDIFile(self.channel_number)
        track = 0
        for instrument_index, instrument_name in self.instruments.items():
            self.midi.addTrackName(track, 0, "Track" + str(track))
            self.midi.addTempo(track, 0, self.tempo)
            self.midi.addProgramChange(track, 0, 0, instrument_index)
            track += 1

    def read_score(self, delimiter, channel=1):
        track = 0
        for instrument, caracteristics in self.instruments.items():
            self.time = 0
            notes = caracteristics["score"].split(delimiter)
            previous = ""
            duration = 1
            for note in notes:
                if note == "":
                    duration += 1
                    if previous == "":
                        self.time += 1
                        duration = 1
                else:
                    if previous != "" and duration:
                        if previous[0].isupper():
                            self.add_chord(track, previous, duration, caracteristics["volume"],
                                           caracteristics["channel"])
                        else:
                            self.add_note(track, previous, duration, caracteristics["volume"],
                                          caracteristics["channel"])
                        duration = 1

                    previous = note
            track += 1

    def add_chord(self, track, chord, duration, volume, channel):
        for note in self.chords[chord]:
            log(track, track, self.notes[note.upper()], self.time, duration, volume)
            self.midi.addNote(track, channel, self.notes[note.upper()] + 12, self.time, duration, volume)

        self.time += duration

    def add_note(self, track, note, duration, volume, channel):
        log(track, track, self.notes[note.upper()], self.time, duration, volume)
        self.midi.addNote(track, channel, self.notes[note.upper()] + 12, self.time, duration, volume)
        self.time += duration

    def write_file(self, filename):
        with open(filename, "wb") as f:
            self.midi.writeFile(f)
