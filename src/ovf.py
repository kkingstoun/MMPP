# -*- coding: utf-8 -*-
"""Dokumentacja

Do zrobienia:
    * W tym momencie sprwadziłem, że dobrze działa wczytywanie jedno kompozytowych plików, nie wiem czy dla trzech.
    ** Miałem problem z multiprocessingiem, klasa wywołuje siebie, nie wiem czy to najlepsze rozwiązanie
    *** Benchmarki są konieczne
"""
import os
import numpy as np
import glob
import re
import multiprocessing as mp
from functools import partial

def loadSingleOvf(parms, file):
    return OvfFile(file, parms).array, OvfFile(file, parms).time[0]


class OvfFile():
    """

    """
    @staticmethod
    def getKey(filename):
        return int(re.findall(r'\d+', filename)[-1])

    def __parseFile(self, path):
        with open(path, 'rb') as f:
            _headers = {}
            capture_keys = ("xmin", "ymin", "zmin", "xmin", "ymin", "zmin", "xstepsize",
                            "ystepsize", "zstepsize", "xnodes", "ynodes", "znodes", "valuedim")

            a = ""
            while not "Begin: Data" in a:
                a = f.readline().strip().decode('ASCII')
                for key in capture_keys:
                    if key in a:
                        _headers[key] = float(a.split()[2])

                if "Total simulation time" in a:
                    time = float(a.split(":")[-1].strip().split()[0].strip())

            znodes = int(_headers['znodes'])
            ynodes = int(_headers['ynodes'])
            xnodes = int(_headers['xnodes'])
            nOfComp = int(_headers['valuedim'])

            array_size = xnodes*ynodes*znodes*nOfComp+1
            outArray = np.fromfile(f, '<f', count=int(array_size))

            if outArray[0] == 1234567:
                outArray = outArray[1:].reshape(
                    1, znodes, ynodes, xnodes, nOfComp)
            else:
                "sequence 1234567 not detected!"

            # print(outArray.shape, outArray1.shape, array_size)
            # the last 2 lines of OVF files are as follows:
            # # End: Data Binary 4
            # # End: Segment

            # print(f.readline())  # temporary verification
            # print(f.readline())  # temporary verification

        self._array = outArray[self._parms.getParms["zStart"]:self._parms.getParms["zStop"],
                               self._parms.getParms["yStart"]:self._parms.getParms["yStop"],
                               self._parms.getParms["xStart"]:self._parms.getParms["xStop"],
                               :]
        self._headers = _headers
        self._time.append(time)

    def __readDir(self):
        print("Reading folder: " + self._path+"/" +
              self._parms.getParms["head"] + '*.ovf')

        file_list = glob.glob(
            self._path+"/"+self._parms.getParms["head"]+'*.ovf')[::self._parms.getParms["nStep"]]  # files filtering

        file_list = sorted(file_list, key=self.getKey)[
            self._parms.getParms["tStart"]:self._parms.getParms["tStop"]]

        _headers = OvfFile(file_list[0], self._parms)._headers

        print("N of files to process: ", len(file_list))

        print("Available nodes (n-1): " + str(int(mp.cpu_count()-1)))
        self.pool = mp.Pool(processes=int(mp.cpu_count()-1))
        func = partial(loadSingleOvf, self._parms)
        self._array, self._time = zip(*self.pool.map(func, file_list))
        self.pool.close()
        self.pool.join()

        self._array = np.array(self._array).reshape([
            len(file_list),
            int(_headers["znodes"]),
            int(_headers["ynodes"]),
            int(_headers["xnodes"]),
            int(_headers["valuedim"]),
        ])
        self._time = np.array(self._time)

        print("Matrix shape:", *self._array.shape)
        self._headers = _headers 

    @property
    def array(self):
        return self._array

    @property
    def avrComponent(self):
        return np.average(self._array,axis=(4))

    @property
    def shape(self):
        return self._array.shape

    @property
    def time(self):
        return self._time

    @property
    def headers(self):
        return self._headers

    def __init__(self, path="", parms=[]):

        self._path = path
        self._parms = parms
        self._time = []
        self._headers = []
        self._array = []

        if os.path.isdir(self._path):
            self.__readDir()
        else:
            self.__parseFile(self._path)
