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
        # TODO
        # Gdzieś  jest błąd, przez który muszę wywoływać arr[:,0]
        return  np.fft.rfft(arr*self.get_window(len(arr)))
        

    def __init__(self):
        pass
        # shape = self._array.shape
        # print(math.ceil(shape[0]/2), shape[1], shape[2], shape[3], shape[4])
     

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
        _shape = self._array.shape
        self.MFft = np.zeros(
            (math.ceil(_shape[0]/2), _shape[1], _shape[2], _shape[3], _shape[4]),dtype=np.complex64)
        _axis = self.unSelectAxis   
        _data = self.average_magnetization()
        for z in range(_data.shape[1]):
            for y in range(_data.shape[2]):
                for x in range(_data.shape[3]):
                    a = _data[:, z, y, x, self.comp]
                    self.MFft[:, z, y, x, self.comp] = self._doFFT(a)
        if self.eachZ == True:
            self.MFft=np.average(self.MFft[:, z, y, x, self.comp], axis=1)
            self.keep_size(self.MFft, _axis)
        return self.MFft

    def keep_size(self, m, axis=1):
        tshape = list(self._data._array.shape)
        for ax in axis:
            tshape[ax] = 1
        tshape[-1]=1
        m = m.reshape(tshape)
        return m

    def average_magnetization(self):

        _axis = self.unSelectAxis

        _mag = np.average(self._data._array[:, :, :, :, self.comp], axis=_axis)

        return self.keep_size(_mag,_axis)

    def run_fft_for_spectrum(self):

        _data = self.average_magnetization()

        _spectrum=[] 

        for z in range(_data.shape[1]):
            for y in range(_data.shape[2]):
                for x in range(_data.shape[3]):
                    if self.zero_padding == True:
                        arr = _data[:, z, y, x]
                        arr = np.pad(
                            arr, (0, 1024 - len(arr) % 1024), 'constant')
                    else:
                        arr = _data[:, z, y, x]
                    _spectrum.append(self._doFFT(arr))
        _spectrum = np.array(_spectrum)
        _spectrum = np.average(np.array(_spectrum),axis=0)

        if self.zero_padding == True:
            time = self._data._time.size + 1024 - self._data._time.size % 1024
        else:
            time = self._data._time.size
        _frequencies = np.fft.rfftfreq(time, self._data.avgtime)

        return _frequencies, _spectrum
