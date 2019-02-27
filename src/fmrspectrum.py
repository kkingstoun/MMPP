import fft
import numpy as np
# import peakutils


class FMRSpectrum(fft.Fft):

    def __init__(self):
        pass

    @property
    def check_component(self):
        if self._array.shape[-1] == 1:
            return 0

    def fmrspectrum(self, comp=2, eachX=False, eachY=False, eachZ=False, window=None):

        super().__init__()

        self.eachX = eachX
        self.eachY = eachY
        self.eachZ = eachZ
        self.comp = self.check_component
        self.window = window
        self.fmrspectrum, self.fmrfreq = self.run_fft_for_spectrum()

