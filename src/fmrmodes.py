# from ovf import OvfFile
import parameters
import fft
import numpy as np
import matplotlib.pyplot as plt
import peakutils

class FMRModes(fft.Fft):
        
    # def __init__(self, mtzyxc, copyarray=False, eachX=False, eachY=False, eachZ=False):
    def __init__(self):
        pass
        # 
        # if copyarray == True:
        #     self.mtzyxc = mtzyxc[:, :, :, :, :]
        # else:
        #     self.mtzyxc = mtzyxc
        # self.eachX = eachX
        # self.eachY = eachY
        # self.eachZ = eachZ   

    @property
    def check_component(self):
        if self._array.shape[-1] == 1:
            return 0

    def calculateModes(self, copyarray=False, eachZ=False, comp=2, window=None):
        
        super().__init__()
        
        self.eachX = True
        self.eachY = True
        self.eachZ = eachZ

        self.comp = self.check_component

        self.window = window


        Mfft = self.run_fft_for_modes()

        return Mfft
        
    def peaks(self, data, thres=0.5, min_dist=30):
        return peakutils.indexes(np.abs(data), thres, min_dist)
        
    



