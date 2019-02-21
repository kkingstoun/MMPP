import numpy as np


class Fft:

    def _across(self, pos):
        self.MFft.append(self._doFFT(
            np.take(self.mtzyxc._array[:], pos, axis=pos)))
            # np.append(self.MFft, )

    def _doFFT(self, arr):
        return np.fft.rfft(arr.reshape(len(arr)))
       

    def __init__(self, mtzyxc):

        pass

    def runFft(self):

        if self.eachX == True and self.eachY == True and self.eachZ == True:
            self.self._across()
            self._doFFT()

        elif self.eachX == True and self.eachY == True and self.eachZ == False:


            tShape = self.mtzyxc._array.shape

            self.mtzyxc._array = np.average(self.mtzyxc._array, axis=(1))

            self.mtzyxc._array = self.mtzyxc._array.reshape(
                (tShape[0], 1, 1, tShape[3], tShape[4]))

            self._across(2,3)

            self.MFft = np.array(self.MFft)

            print(self.MFft.shape)

            self.MFft = np.average(self.MFft, axis=0)

            return self.MFft

        elif self.eachX == True and self.eachY == False and self.eachZ == False:
            tShape = self.mtzyxc._array.shape
            self.mtzyxc._array = np.average(self.mtzyxc._array, axis=(1, 2))
            self.mtzyxc._array = self.mtzyxc._array.reshape(
                (tShape[0], 1, 1, tShape[3], tShape[4]))
            self._across(3)
            self.MFft = np.array(self.MFft)
            print(self.MFft.shape)
            self.MFft = np.average(self.MFft, axis=0)
            return self.MFft

        elif self.eachX == False and self.eachY == False and self.eachZ == False:
            self.mtzyxc._array = np.average(self.mtzyxc._array, axis=(1, 2, 3))
            self._doFFT()

        elif self.eachX == False and self.eachY == True and self.eachZ == False:
            self.mtzyxc._array = np.average(self.mtzyxc._array, axis=(1, 3))
            self.self._across()
            self._doFFT()

        elif self.eachX == False and self.eachY == False and self.eachZ == True:
            self.mtzyxc._array = np.average(self.mtzyxc._array, axis=(2, 3))
            self.self._across()
            self._doFFT()
