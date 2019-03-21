from ovf import OvfFile
import os
import numpy as np
import random
import copy


class Marray():
    def __init__(self, path=None, parms=None, data=None, comp=None):
        self.name = str(random.randint(0, 10))
        self._path = path
        self._parms = parms

        if data is None:
            self.data = OvfFile(path, parms)
        else:
            self.data = copy.copy(data)
            if self.check_component is True:
                self.data.array = self.data.array[:, :, :, :, :]
                print("WARNING: THERE IS ONLY ONE COMPONENT")
            else:
                self.data.array = self.data.array[:, :, :, :, comp:comp+1]

    @property
    def check_component(self):
        if self.data.array.shape[-1] is 1:
            return True

    def x(self, copy=False):
        if copy is False:
            if self.check_component is True:
                return(self)
            else:
                self.data.array = self.data.array[:, :, :, :, 0]
                return(self)
        else:
            print("As")
            return Marray(data=self.data, comp=0, path=self._path, parms=self._parms)

    def y(self, copy=False):
        if copy is False:
            if self.check_component is True:
                return(self)
            else:
                self.data.array = self.data.array[:, :, :, :, 1]
                return(self)
        else:
            print("As")
            return Marray(data=self.data, comp=1, path=self._path, parms=self._parms)

    def z(self, copy=False):
        if copy is False:
            if self.check_component is True:
                return(self)
            else:
                self.data.array = self.data.array[:, :, :, :, 2]
                return(self)
        else:
            print("As")
            return Marray(data=self.data, comp=2, path=self._path, parms=self._parms)

    # def load(self):
    #     with np.load(self._path) as data:
    #         self.data = data["data"]
    #         # self.data.array = data["array"]
    #         # self.data._headers = data["headers"][()]
    #         # self._path = data["path"]
    #         # self.data.time = data["time"]
    #         print("Data loaded successfully from  ", self._path)

    def save(self, path=None):
        self.data.save(path)
        # if path is None:
        #     save_path = os.path.dirname(os.path.realpath(self._path)) + "/arr.npz"
        # np.savez(save_path, data=self.data)
        # print("Data saved to the ", save_path)
