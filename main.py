# Press the green button in the gutter to run the script.
from config_midi import ConfigMidi
from midi_generator import MidiGenerator
from midi_player import MidiPlayer
from song import Song

if __name__ == '__main__':
    # song1 = Song(True,34535778)
    song1 = Song(True)
    midi_filename = "test_midi.mid"
    config_midi = ConfigMidi(song1.instruments, 180, 30)
    # score = "Bm    G    D    D    Bm    G    D    D    Bm    G    D    D    Bm    G    D    D    Bm    G    D    D
    # stop"
    midi_generator = MidiGenerator(config_midi)
    midi_generator.read_score(" ")
    midi_generator.write_file(midi_filename)
    midi_player = MidiPlayer(midi_filename)
    midi_player.play()
