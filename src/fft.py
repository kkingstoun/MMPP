import numpy as np
import math

class Fft:

    def _across(self, pos):
        for y in range(self.mtzyxc.shape[2]-1):
            print(y/self.mtzyxc.shape[2]*100, "%")
            for x in range(self.mtzyxc.shape[3]-1):
                self.MFft[:, y, x] = self._doFFT(
                    self.mtzyxc.array[:, 0, y, x, 0])

    def _doFFT(self, arr):
        #Gdzieś  jest błąd, przez który muszę wywoływać arr[:,0]
        return  np.fft.rfft(arr[:, 0]*self.get_window(len(arr[:, 0])))
        

    def __init__(self):
        pass
        # shape = self._array.shape
        # print(math.ceil(shape[0]/2), shape[1], shape[2], shape[3], shape[4])
        # self.MFft = np.zeros(
        #     (math.ceil(shape[0]/2)+1, shape[1], shape[2], shape[3], shape[4]))

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

    def get_window(self,lenght):
        if self.window == "hanning":
            return np.hanning(lenght)

    def run_fft_for_modes(self):
        mxy = self.keep_size(np.average(self._array, axis=self.unSelectAxis))
        if self.eachZ == True:
            for x in range(mxy.shape[3]):
                print(x/mxy.shape[2]*100, "%")
                for y in range(mxy.shape[2]):
                    for z in range(mxy.shape[1]):
                        b = self._array[:, z, y, x, self.comp]
                        a = self._doFFT(b
                                        )
                        self.MFft[:, z, y, x, self.comp] = a
        else:
            for y in range(mxy.shape[2]):
                print(y/mxy.shape[2]*100, "%")
                for x in range(mxy.shape[3]):
                    b = self._array[:, 0, y, x, self.comp]
                    a = self._doFFT(b
                                    )
                    self.MFft[:, 0, y, x, self.comp] = a
        return self.MFft

    def keep_size(self, m, comp=1):
        tshape = list(self._array.shape)
        for c in comp:
            tshape[c] = 1
        m = m.reshape(tshape)
        return m

    def average_magnetization(self):

        _axis = self.selectAxis

        _mag = np.average(self._array[:, :, :, :, self.comp], axis=_axis)

        return self.keep_size(_mag,_axis)

    def run_fft_for_spectrum(self):

        _data = self.average_magnetization()

        _spectrum=[] 

        for z in range(_data.shape[1]):
            for y in range(_data.shape[2]):
                for x in range(_data.shape[3]):
                    print(z,y,x)
                    _spectrum.append(self._doFFT(_data[:,z,y,x]))
        _spectrum = np.array(_spectrum)
        _spectrum = np.average(np.array(_spectrum),axis=0)

        _frequencies = np.fft.rfftfreq(self._array.shape[0], self.avgtime)

        return _spectrum, _frequencies
