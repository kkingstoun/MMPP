import numpy as np


class Fft:

    def _across(self, pos):
        for y in range(self.mtzyxc.shape[2]-1):
            print(y/self.mtzyxc.shape[2]*100, "%")
            for x in range(self.mtzyxc.shape[3]-1):
                self.MFft[:, y, x] = self._doFFT(
                    self.mtzyxc.array[:, 0, y, x, 0])

    def _doFFT(self, arr):
        window = np.hanning(len(arr))
        return np.fft.rfft(arr*window)

    def __init__(self):

        self.MFft = np.zeros_like(self._array[::2,:,:,:,:])

    # @staticmethod
    @property
    def selectAxis(self):

        a1 = (None, 1)[self.eachZ == True]
        a2 = (None, 2)[self.eachY == True]
        a3 = (None, 3)[self.eachX == True]
        return tuple(filter(None, [a1, a2, a3]))

    @property
    def unSelectAxis(self):
        a1 = (1, None)[self.eachZ == True]
        a2 = (2, None)[self.eachY == True]
        a3 = (3, None)[self.eachX == True]
        return tuple(filter(None, [a1, a2, a3]))



    def run_fft_for_modes(self):

        if self.eachZ == True:
            pass
        else:
            mxy = self.keep_size(np.average(
                self._array, axis=self.unSelectAxis))

            for y in range(mxy.shape[2]):
                print(y/mxy.shape[2]*100, "%")
                for x in range(mxy.shape[3]):
                    b = self._array[:, 0, y, x, self.comp]
                    a = self._doFFT(b
                        )
                    self.MFft[:, 0, y, x, self.comp] = a
        return self.MFft

    def keep_size(self,m,comp=1):
        tshape = list(self._array.shape)
        tshape[comp]=1
        m=m.reshape(tshape)
        return m

        # if self.eachX == True and self.eachY == True and self.eachZ == True:
        #     self.self._across()
        #     self._doFFT()

        # elif self.eachX == True and self.eachY == True and self.eachZ == False:

                    # tShape = self.mtzyxc._array.shape
                    # tShape = np.take(tShape, self.selectAxis)
                    # tShape[*] = 1

                    # self.mtzyxc._array = np.average(
                    #     self.mtzyxc._array, axis=self.unSelectAxis)

                    # self.mtzyxc._array = self.mtzyxc._array.reshape(tShape)

                    # self._across(self.selectAxis)

                    # self.MFft = np.array(self.MFft)

                    # return self.MFft

        # elif self.eachX == True and self.eachY == False and self.eachZ == False:
        #     tShape = self.mtzyxc._array.shape
        #     self.mtzyxc._array = np.average(self.mtzyxc._array, axis=(1, 2))
        #     self.mtzyxc._array = self.mtzyxc._array.reshape(
        #         (tShape[0], 1, 1, tShape[3], tShape[4]))
        #     self._across(3)
        #     self.MFft = np.array(self.MFft)
        #     print(self.MFft.shape)
        #     self.MFft = np.average(self.MFft, axis=0)
        #     return self.MFft

        # elif self.eachX == False and self.eachY == False and self.eachZ == False:
        #     self.mtzyxc._array = np.average(self.mtzyxc._array, axis=(1, 2, 3))
        #     self._doFFT()

        # elif self.eachX == False and self.eachY == True and self.eachZ == False:
        #     self.mtzyxc._array = np.average(self.mtzyxc._array, axis=(1, 3))
        #     self.self._across()
        #     self._doFFT()

        # elif self.eachX == False and self.eachY == False and self.eachZ == True:
        #     self.mtzyxc._array = np.average(self.mtzyxc._array, axis=(2, 3))
        #     self.self._across()
        #     self._doFFT()
