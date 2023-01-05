# Press the green button in the gutter to run the script.
import pygame

from config_midi import ConfigMidi
from midi_generator import MidiGenerator
from midi_player import MidiPlayer

if __name__ == '__main__':
    midi_filename = "test_midi.mid"

    instruments = {4: "saw"}
    config_midi = ConfigMidi(instruments, 120)
    score = "Em    Am    D7    B7    Em    C    Am    B7    Em    Am    D7    B7    Em    C    Am    B7    Em    Am    D7    B7    Em    C    Am    B7    stop"
    #score = "Bm    G    D    D    Bm    G    D    D    Bm    G    D    D    Bm    G    D    D    Bm    G    D    D    stop"
    midi_generator = MidiGenerator(score, config_midi)
    midi_generator.read_score(" ")
    midi_generator.write_file(midi_filename)
    midi_player = MidiPlayer(midi_filename)
    midi_player.play()
    input()
