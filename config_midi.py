class ConfigMidi:
    def __init__(self, instruments, tempo):
        self.channel_number = len(instruments)
        self.track_number = len(instruments)
        self.instruments = instruments
        self.tempo = tempo
