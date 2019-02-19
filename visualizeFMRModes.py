import calculateFFT as cf
import numpy as np

class VisualizeModes():
    def __init__(self, Mtxyz, eachX=False, eachY=False, eachZ=False, comp=0):
        self.Mfft = []
        cf.CalculateFFT(Mtxyz, eachX, eachY, eachZ, comp)
      

        self.Mfft = np.array(self.Mfft)
        print(self.Mfft.shape)
