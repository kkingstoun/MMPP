from ovf import OvfFile
from fmrmodes import FMRModes
from fmrspectrum import FMRSpectrum

class Marray:
    def __init__(self, path, parms, array=None):
        self._path = path
        self._parms = parms
        #
        # (self._arr=OvfFile(path, parms), self._arr=array)[array != None]
        if array == None:
            self._arr = OvfFile(path, parms)
        else:
            self._arr = array

    def fmrspectrum(self, window, eachZ):
        fmrspectrum = FMRSpectrum()
        # self.fmrspectrum()
        pass

    def x(self, copy):
        if copy is False:
            self._arr = self.arr[:, :, :, :, 2]
            return(self)
        else:
            return M(self._arr)

    def y(self, copy):
        if copy is False:
            self._arr = self.arr[:, :, :, :, 1]
            return(self)
        else:
            return M(self._arr)

    def z(self, copy):
        if copy is False:
            self._arr = self.arr[:, :, :, :, 0]
            return(self)
        else:
            return M(self._arr)
