class ConfigMidi:
    def __init__(self, instruments, tempo, default_volume):
        self.channel_number = len(instruments)
        self.track_number = len(instruments)
        self.instruments = instruments
        self.tempo = tempo
        self.default_volume = default_volume
