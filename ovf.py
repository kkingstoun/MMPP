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
    return OvfFile(file, parms).array


class OvfFile:
    """

    """
    @staticmethod
    def getKey(filename):
        return int(re.findall(r'\d+', filename)[-1])

    def __parseFile(self, path):
        with open(path, 'rb') as f:
            headers = {}
            capture_keys = ("xmin", "ymin", "zmin", "xmin", "ymin", "zmin", "xstepsize",
                            "ystepsize", "zstepsize", "xnodes", "ynodes", "znodes")

            a = ""
            while not "Begin: Data" in a:
                a = f.readline().strip().decode('ASCII')
                for key in capture_keys:
                    if key in a:
                        headers[key] = float(a.split()[2])

                if "Total simulation time" in a:
                    time = float(a.split(":")[-1].strip().split()[0].strip())

            znodes = int(headers['znodes'])
            ynodes = int(headers['ynodes'])
            xnodes = int(headers['xnodes'])

            array_size = xnodes*ynodes*znodes

            outArray = np.fromfile(f, '<f', count=int(
                array_size)).reshape(znodes, ynodes, xnodes)

        self._array = outArray[self._parms.getParms["zStart"]:self._parms.getParms["zStop"],
                               self._parms.getParms["yStart"]:self._parms.getParms["yStop"], 
                               self._parms.getParms["xStart"]:self._parms.getParms["xStop"]]
        self._headers = headers
        self._time = time

    def __readDir(self):
        print("Reading folder: " + self._path+"/" +
              self._parms.getParms["head"] + '*.ovf')

        file_list = glob.glob(
            self._path+"/"+self._parms.getParms["head"]+'*.ovf')[::self._parms.getParms["nStep"]]  # files filtering

        file_list = sorted(file_list, key=self.getKey)[
            self._parms.getParms["tStart"]:self._parms.getParms["tStop"]]

        shape = OvfFile(file_list[0], self._parms).headers

        print(shape["xnodes"])

        print("Available nodes (n-1): " + str(int(mp.cpu_count()-1)))
        self.pool = mp.Pool(processes=int(mp.cpu_count()-1))
        func = partial(loadSingleOvf, self._parms)
        self._Mtxyzcarray = np.array(self.pool.map(func, file_list)).reshape([
                                                                                len(file_list), 
                                                                                int(shape["znodes"]),
                                                                                int(shape["ynodes"]),
                                                                                int(shape["xnodes"]),
                                                                                1
                                                                            ])
        self.pool.close()
        self.pool.join()
        print("Matrix shape:", *self.mShape)
        self._mShape = self.mShape

    @property
    def array(self):
        return self._array

    @property
    def shape(self):
        return self._array.shape

    @property
    def mShape(self):
        return self._Mtxyzcarray.shape

    @property
    def time(self):
        return self._time

    @property
    def headers(self):
        return self._headers

    @property
    def txyzcArray(self):
        return self._Mtxyzcarray

    def __init__(self, path, parms):

        self._path = path
        self._parms = parms

        if os.path.isdir(self._path):
            self.__readDir()
        else:
            self.__parseFile(self._path)
