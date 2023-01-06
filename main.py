from config_midi import ConfigMidi
from midi_generator import MidiGenerator
from midi_player import MidiPlayer
from song import Song

if __name__ == '__main__':
    #song1 = Song(True,34535778)
    song1 = Song(True)
    MIDI_FILENAME = "test_midi.mid"
    config_midi = ConfigMidi(song1.ensemble, 180, 30)
    midi_generator = MidiGenerator(config_midi)
    midi_generator.read_score(" ")
    midi_generator.write_file(MIDI_FILENAME)
    midi_player = MidiPlayer(MIDI_FILENAME)
    midi_player.play()
