import numpy as np


class Fft:

    def _across(self, pos):
        for y in range(self.mtzyxc.shape[2]-1):
            print(y/self.mtzyxc.shape[2]*100,"%")
            for x in range(self.mtzyxc.shape[3]-1):
                self.MFft[:, y, x] = self._doFFT(
                    self.mtzyxc.array[:, 0, y, x, 0])


    def _doFFT(self, arr):
        window = np.hanning(len(arr))
        return np.fft.rfft(arr*window)
       
    def __init__(self, mtzyxc):
        self.MFft = np.zeros_like(mtzyxc.array[::2, 0, :, :, 0])
        print(self.MFft.shape)
        pass

    def runFft(self):

        if self.eachX == True and self.eachY == True and self.eachZ == True:
            self.self._across()
            self._doFFT()

        elif self.eachX == True and self.eachY == True and self.eachZ == False:


            tShape = self.mtzyxc._array.shape

            self.mtzyxc._array = np.average(self.mtzyxc._array, axis=(1))

            self.mtzyxc._array = self.mtzyxc._array.reshape(
                (tShape[0], 1, tShape[2], tShape[3], tShape[4]))

            self._across((2,3))

            self.MFft = np.array(self.MFft)

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
