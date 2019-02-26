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


class OvfFile:
    def __init__(self, path, parms):
        self._path = path
        self._parms = parms
        if os.path.isdir(self._path):
            self.file_list = self.get_files_names()
            self._headers, self._time = self.catch_headers(self.file_list[0])
            self.array_size = self.get_array_size()
            self._array, self._time = self.__readDir()
        else:
            self._headers, self._time = self.catch_headers(self._path)
            self.array_size = self.get_array_size()
            self._array, self._time = self.parse_file(self._path)

    @staticmethod
    def getKey(filename):
        return int(re.findall(r'\d+', filename)[-1])

    def catch_headers(self, path):
        headers = {}
        capture_keys = ("xmin", "ymin", "zmin", "xmin", "ymin", "zmin", "xstepsize",
                        "ystepsize", "zstepsize", "xnodes", "ynodes", "znodes", "valuedim")
        a = ""
        with open(path, 'rb') as f:
            while not "Begin: Data" in a:
                a = f.readline().strip().decode('ASCII')
                for key in capture_keys:
                    if key in a:
                        headers[key] = float(a.split()[2])
                if "Total simulation time" in a:
                    time = float(a.split(":")[-1].strip().split()[0].strip())
            return headers, time

    def get_array_size(self):
        # TODO: int conversion should be done in catch_headers if it's needed everywhere
        znodes = int(self._headers['znodes'])
        ynodes = int(self._headers['ynodes'])
        xnodes = int(self._headers['xnodes'])
        nOfComp = int(self._headers['valuedim'])
        return xnodes*ynodes*znodes*nOfComp+1

    def __readDir(self):
        print("Reading folder: " + self._path+"/" +
              self._parms.getParms["head"] + '*.ovf')
        print("N of files to process: ", len(self.file_list))
        print("Available nodes (n-1): " + str(int(mp.cpu_count()-1)))
        pool = mp.Pool(processes=int(mp.cpu_count()-1))

        # func = partial(self.parse_file)
        array, time = zip(*pool.map(self.parse_file, self.file_list))
        pool.close()
        pool.join()
        array = np.array(array).reshape([
            len(self.file_list),
            int(self._headers["znodes"]),
            int(self._headers["ynodes"]),
            int(self._headers["xnodes"]),
            int(self._headers["valuedim"]),
        ])

        print("Matrix shape:", array.shape)
        return array, np.array(time)

    def get_files_names(self):
        file_list = glob.glob(
            self._path+"/"+self._parms.getParms["head"]+'*.ovf')[::self._parms.getParms["nStep"]]  # files filtering
        return sorted(file_list, key=self.getKey)[
            self._parms.getParms["tStart"]:self._parms.getParms["tStop"]]

    def parse_file(self, path):
        with open(path, 'rb') as f:
            outArray = np.fromfile(f, '<f', count=int(self.array_size))
            outArray = outArray[1:].reshape(
                    1, int(self._headers['znodes']), int(self._headers['ynodes']), int(self._headers['xnodes']), int(self._headers['valuedim']))
            return outArray[self._parms.getParms["zStart"]:self._parms.getParms["zStop"],
                                   self._parms.getParms["yStart"]:self._parms.getParms["yStop"],
                                   self._parms.getParms["xStart"]:self._parms.getParms["xStop"],
                                   :], self._time
