import os 
import numpy as np
import glob 
import re
import multiprocessing as mp
from functools import partial

def loadSingleOvf(parms, file):
    return OvfFile(file,parms).array

class OvfFile:

    @staticmethod
    def getKey(filename):
        return int(re.findall(r'\d+',filename)[-1])

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

        self._array = outArray
        self._headers = headers
        self._time = time

    def __readDir(self):
        print("Reading folder: " + self._path+"/"+self._parms.head+'*.ovf')
        file_list = glob.glob(
            self._path+"/"+self._parms.head+'*.ovf')[::self._parms.nStep]  # files filtering

        file_list = sorted(file_list, key=self.getKey)[
            self._parms.tStart:self._parms.tStop]

        shape = OvfFile(file_list[0], self._parms).headers

        print(shape["xnodes"])
        # self.M = np.zeros(
        #         [len(file_list), int(shape["znodes"]), int(shape["ynodes"]), int(shape["xnodes"]),1]
        #     )
        
        print(self.M.shape)
        print("Available nodes: " + str(int(mp.cpu_count())))
        self.pool = mp.Pool(processes=int(mp.cpu_count()-1))
        func = partial(loadSingleOvf,self._parms)
        self.M = self.pool.map(func, file_list)
        self.pool.close()
        self.pool.join()
        self.M = np.array(self.M)
        print(len(self.M), self.M.shape)

        # self.M[:, :, :, 0] = self.Mp


        # 

        # i = 0

        # if self._parms.getParms["oneComp"] == True:
        #     print("test")
        #     M = pool.map(loadOVF, self._parms.getParms)



    @property
    def array(self):
        return self._array

    @property
    def time(self):
        return self._time

    @property
    def headers(self):
        return self._headers

    @property
    def txyArray(self):
        return self._txyarray

    def __init__(self, path, parms):

        self._path = path
        self._parms = parms

        if os.path.isdir(self._path):
            self.__readDir()
        else:
            self.__parseFile(self._path)
