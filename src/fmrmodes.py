import fft
import numpy as np
import matplotlib.pyplot as plt

class FMRModes(fft.Fft):
        
    def __init__(self, mtzyxc, copyarray=False, eachX=False, eachY=False, eachZ=False):
    
        if copyarray == True:
            self.mtzyxc = mtzyxc[:, :, :, :, :]
        else:
            self.mtzyxc = mtzyxc
        self.eachX = eachX
        self.eachY = eachY
        self.eachZ = eachZ
        self.MFft = np.array([])    

    def calculateModes(self):
        self.MFft = []
        self.MFft = self.runFft()
        plt.plot(np.abs(self.MFft))
        plt.show()
    



