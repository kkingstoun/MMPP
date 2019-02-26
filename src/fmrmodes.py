from ovf import OvfFile
import parameters
import fft
import numpy as np
import matplotlib.pyplot as plt

class FMRModes(fft.Fft):
        
    def __init__(self, mtzyxc, copyarray=False, eachX=False, eachY=False, eachZ=False):
        super().__init__(mtzyxc)
        if copyarray == True:
            self.mtzyxc = mtzyxc[:, :, :, :, :]
        else:
            self.mtzyxc = mtzyxc
        self.eachX = eachX
        self.eachY = eachY
        self.eachZ = eachZ   

    def calculateModes(self):
        
        self.MFft = self.runFft()
        print(self.MFft.shape)
        
        ax1 = plt.subplot(211)
        x = np.fft.rfftfreq(self.mtzyxc.shape[0], 2e-11)
        plt.plot(np.abs(np.average(self.MFft,axis=(1,2))))
        ax2 = plt.subplot(212)

        ax2.imshow(np.abs(self.MFft[99]),
                   origin="lower",
                   aspect="equal")



        # parms = parameters.ovfParms()

        # M_Stable = OvfFile(
        #     r"C:/Users/Mateusz/Desktop/Radek/circular_10.out/m_stable_30.ovf", parms)
            
        # ax3 = plt.subplot(313)

        # # a = M_Stable.avrComponent
        # print(a.shape)

        # ax3.imshow(a[0,1,:,:],
        #            origin="lower",
        #            aspect="equal")
        plt.show()
    



