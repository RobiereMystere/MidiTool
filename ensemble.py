from instrument import Instrument


class Ensemble:

    def __init__(self):
        self.indexes = {
            Instrument.MELODIC: 0,
            Instrument.PERCUSSIVE: 0
        }
        self.channels = {
            Instrument.MELODIC: {
                0: None,
                1: None,
                2: None,
                3: None,
                4: None,
                5: None,
                6: None,
                7: None,
                8: None,
                11: None,
                12: None,
                13: None,
                14: None,
                15: None
            },
            Instrument.PERCUSSIVE: {
                9: None,
                10: None

            }
        }

    def append(self, instrument: Instrument):
        self.channels[instrument.get_type()][
            list(self.channels[instrument.get_type()].keys())[self.indexes[instrument.get_type()]]] = instrument

        self.indexes[instrument.get_type()] += 1
