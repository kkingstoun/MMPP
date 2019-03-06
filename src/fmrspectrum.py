import fft
import numpy as np
import peakutils


class FMRSpectrum(fft.Fft):

    def calculate_fmr_spectrum(self, eachX=False, eachY=False, eachZ=False, window=None, comp=None, zero_padd=True):
        self.comp = comp
        self.eachX = eachX
        self.eachY = eachY
        self.eachZ = eachZ
        self.zero_padding = zero_padd
        self.window = window
        return self.run_fft_for_spectrum()

    # @property
    def peaks(self, data, thres=0.5, min_dist=30):
        return peakutils.indexes(np.abs(data), thres, min_dist)
        

