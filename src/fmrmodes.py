# from ovf import OvfFile
import parameters
import fft
import numpy as np
import matplotlib.pyplot as plt
# import peakutils

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

    def calculateModes(self, copyarray=False, eachX=False, eachY=False, eachZ=False, comp=2, window=None):
        
        super().__init__()
        
        self.eachX = eachX
        self.eachY = eachY
        self.eachZ = eachZ
        self.comp = comp
        self.window = window


        Mfft = self.run_fft_for_modes()

        indexes = peakutils.indexes(Mfft, thres=0.5, min_dist=Mfft.shape[0]/300)


        print(indexes)

        return Mfft,indexes
        
        
    



