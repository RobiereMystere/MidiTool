from ensemble import Ensemble
from instrument import Instrument


class ConfigMidi:
    def __init__(self, ensemble: Ensemble, tempo, default_volume):
        self.ensemble = ensemble
        self.channels = []
        self.track_number = 0
        self.default_volume = default_volume
        self.tempo = tempo

        for channel, instrument in ensemble.channels[Instrument.MELODIC].items():
            if instrument is not None:
                self.channels.append(channel)
                self.track_number += 1
        for channel, instrument in ensemble.channels[Instrument.PERCUSSIVE].items():
            if instrument is not None:
                self.channels.append(channel)
                self.track_number += 1
