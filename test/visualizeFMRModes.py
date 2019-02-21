import fft
import numpy as np


class VisualizeModes:

    def __init__(self, path, params):

        a = Ovf(ef)
        self.matix = Mtxyzc(path, params)
        self.Mfft = []

    def calculateModes(self, Mtxyz, eachX=False, eachY=False, eachZ=False, comp=0):

        self.eachX = eachX
        self.eachY = eachY
        self.eachZ = eachZ

        Mfft = fft.Fft(Mtxyz, eachX, eachY, eachZ, comp)

        self.Mfft = np.array(self.Mfft)
        print(self.Mfft.shape)
