import numpy as np

class CalculateFFT:

    def acrossX(self,mfft):
        pass

    def acrossY(self,mfft):
        pass

    def acrossZ(self,mfft):
        pass

    def runFFTxyz(self):
        if eachX == True:
            self.acrossX(self._Mtxyz)
        else:
            np.average(self._Mtxyz,axis=3)
    def doFFT(self,M):
        return(np.fft.rfft(M))

    def __init__(self, Mtxyz, eachX, eachY, eachZ, comp):

        Mtxyz = Mtxyz[:,:,:,:,comp]

        if eachX == True and eachY == True and eachZ == True:
            self.acrossx(Mtxyz)
            self.acrossy(Mtxyz)
            self.acrossz(Mtxyz)

        elif eachX == True and eachY == True and eachZ == False:
            Mtxyz = np.average(Mtxyz, axis=(2, 3))
            self.acrossZ(Mtxyz)
        
        elif eachX == True and eachY == False and eachZ == False:
            Mtxyz = np.average(Mtxyz, axis=(3))
            self.acrossZ(Mtxyz)

        elif eachX == False and eachY == False and eachZ == False:
            Mtxyz = np.average(Mtxyz, axis=(1, 2, 3))

        elif eachX == False and eachY == True and eachZ == False:
            Mtxyz = np.average(Mtxyz, axis=(3,1))
            self.acrossy(Mtxyz)
        
        elif eachX == False and eachY == False and eachZ == True:
            Mtxyz = np.average(Mtxyz, axis=(3,1))
            self.acrossy(Mtxyz)
        
        


        self.runFFTxyz()
        # if eachX == True:
        #     for x in range(Mtxyz._mShape[3]):
        #         if eachY == True:
        #             for y in range(Mtxyz._mShape[2]):
        #                 if eachZ == True:
        #                     for z in range(Mtxyz._mShape[1]):
        #                         self.Mfft.append(cf.CalculateFFT(
        #                             Mtxyz._Mtxyzcarray[:, z, y, x, comp]))
        #                 else:
        #                     Mtxy = np.average(Mtxyz[:, :, y, x, comp], axis=1)
        #                     self.Mfft.append(cf.CalculateFFT(
        #                         Mtxyz.Mtxy))
        #         else:
        #             Mtxz = np.average(Mtxyz[:, :, :, x, comp],axis = 2)
        #             if eachZ == True:
        #                 for z in range(Mtxyz._mShape[1]):
        #                 self.Mfft.append(cf.CalculateFFT(
        #                     Mtxz[:, z, x, comp]))
        #             else:
        #                 Mtxy = np.average(Mtxz, axis=1)
        #                 self.Mfft.append(cf.CalculateFFT(
        #                     Mtxyz.Mtxy))
        # else:
        #     Mtyz = np.average(Mtxyz[:, :, :, :, comp],axis = 3)
