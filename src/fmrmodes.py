# from ovf import OvfFile
import parameters
import fft
import numpy as np
import matplotlib.pyplot as plt

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

    def calculateModes(self, copyarray=False, eachX=False, eachY=False, eachZ=False, comp=2):
        super().__init__()
        self.eachX = eachX
        self.eachY = eachY
        self.eachZ = eachZ
        self.comp = comp

        self.MFft = self.run_fft_for_modes()
        print(self.MFft)
        print(self.MFft.shape)
        
        ax1 = plt.subplot(211)
        x = np.fft.rfftfreq(self._array.shape[0], 2e-11)
        y = np.abs(np.average(self.MFft[:,0,:,:,comp], axis=(1, 2)))
        print(y.shape)
        # y = self.MFft
        # print(y.shape)
        plt.plot(y)
        # print(y)
        ax2 = plt.subplot(212)

        ax2.imshow(np.abs(self.MFft[105,0,:,:,comp]),
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
    



