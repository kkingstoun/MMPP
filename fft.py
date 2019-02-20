import numpy as np


class Fft(object):

    def acrossX(self):
        for x in self._Mtxyzc.shape[3]:
            np.insert(self._MFft, self.__doFFT(self._Mtxyzc[-1]))

    def acrossY(self):
        for x in self._Mtxyzc.shape[2]:
            np.insert(self._MFft, self.__doFFT(self._Mtxyzc[-1]))

    def acrossZ(self):
        for x in self._Mtxyzc.shape[1]:
            np.insert(self._MFft, self.__doFFT(self._Mtxyzc[-1]))

    @property
    def __doFFT(self):
        pass
        # return(np.fft.rfft(M))

    def __init__(self):

        self._MFft = np.array([])

    def calculateFFT(self, Mtxyz, eachX, eachY, eachZ, comp):

        if eachX == True and eachY == True and eachZ == True:
            self.acrossx()
            self.acrossy()
            self.acrossz()
            self.__doFFT()

        elif eachX == True and eachY == True and eachZ == False:
            self._Mtxyzc = np.average(self._Mtxyzc, axis=(2, 3))
            self.acrossZ()
            self.__doFFT()

        elif eachX == True and eachY == False and eachZ == False:
            self._Mtxyzc = np.average(self._Mtxyzc, axis=(1, 2))
            self.acrossX()

        elif eachX == False and eachY == False and eachZ == False:
            self._Mtxyzc = np.average(self._Mtxyzc, axis=(1, 2, 3))
            self.__doFFT()

        elif eachX == False and eachY == True and eachZ == False:
            self._Mtxyzc = np.average(self._Mtxyzc, axis=(1, 3))
            self.acrossY()
            self.__doFFT()

        elif eachX == False and eachY == False and eachZ == True:
            self._Mtxyzc = np.average(self._Mtxyzc, axis=(2, 3))
            self.acrossZ()
            self.__doFFT()
