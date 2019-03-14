# -*- coding: utf-8 -*-
import os
import numpy as np
import glob
import re
import multiprocessing as mp
from src.parameters import ovfParms


class OvfFile:
    def __init__(self, path, parms=None):
        self._path = path
        if parms is None:
            self._parms = ovfParms()
        else:
            self._parms = parms

        if self._path.split(".")[-1] == "npz":
            self.array, self.headers, self.time = self.load_npz(self._path)
            print("Data loaded successfully from  ", path)
        else:
            if os.path.isdir(self._path):
                self.headers = self.load_file(self.get_files_names()[0])[1]
                self.array, self.time = self.parse_dir()
            else:
                self.array, self.headers = self.load_file(self._path)
                self.array = self.parse_array(self.array)
                self.time = self.headers['Desc']

        if any((self._parms.getParms["tStart"], self._parms.getParms["tStop"],
                self._parms.getParms["zStart"], self._parms.getParms["zStop"],
                self._parms.getParms["yStart"], self._parms.getParms["yStop"],
                self._parms.getParms["xStart"], self._parms.getParms["xStop"])):
            self.array = self.array[self._parms.getParms["zStart"]:self._parms.getParms["zStop"],
                         self._parms.getParms["yStart"]:self._parms.getParms["yStop"],
                         self._parms.getParms["xStart"]:self._parms.getParms["xStop"],
                         :]

    def __eq__(self, other):
        return np.allclose(self, other)

    def load_npz(self, path):
        with np.load(path) as data:
            return data["array"], data["headers"][()], data["path"]

    def parse_dir(self):
        file_list = self.get_files_names()

        print("Reading folder: " + self._path + "/" +
              self._parms.getParms["head"] + '*.ovf')
        print("N of files to process: ", len(file_list))
        print("Available nodes (n-1): " + str(int(mp.cpu_count() - 1)))

        pool = mp.Pool(processes=int(mp.cpu_count() - 1))

        array, time = zip(*[(i, j["Desc"]) for i, j in pool.map(self.load_file, file_list)])
        pool.close()
        pool.join()
        array = np.array(array, dtype=np.float32).reshape([
            len(file_list),
            int(self.headers["znodes"]),
            int(self.headers["ynodes"]),
            int(self.headers["xnodes"]),
            int(self.headers["valuedim"]),
        ])

        print("Matrix shape:", array.shape)
        return array, np.array(time)

    def get_files_names(self):
        file_list = glob.glob(
            self._path + "/" + self._parms.getParms["head"] + '*.ovf')[
                    ::self._parms.getParms["nStep"]]  # files filtering
        return sorted(file_list, key=lambda x: int(re.findall(r'\d+', x)[-1]))[
               self._parms.getParms["tStart"]:self._parms.getParms["tStop"]]

    def load_file(self, path):
        with open(path, 'rb') as f:
            a = self.catch_headers(f)
            out_arr = np.fromfile(f, '<f4', count=int(a['znodes'] * a['ynodes'] * a['xnodes'] * a['valuedim'] + 1))
            return out_arr[1:], a

    def catch_headers(self, file):
        headers = {}
        capture_keys = ("xmin:", "ymin:", "zmin:", "xmin:", "ymin:", "zmin:", "xstepsize:",
                        "ystepsize:", "zstepsize:", "xnodes:", "ynodes:", "znodes:", "valuedim:", "Desc:")
        while True:
            a = file.readline().strip().decode('ASCII')
            a = a.split()
            if a[1] in capture_keys:
                headers[a[1][:-1]] = float(a[-2]) if a[-1] is 's' else float(a[-1])
            elif a[2] == 'Data':
                break
        return headers

    def parse_array(self, arr):
        return arr.reshape(1,
                           int(self.headers['znodes']),
                           int(self.headers['ynodes']),
                           int(self.headers['xnodes']),
                           int(self.headers['valuedim']))

    def getarray_size(self):
        znodes = int(self.headers['znodes'])
        ynodes = int(self.headers['ynodes'])
        xnodes = int(self.headers['xnodes'])
        nOfComp = int(self.headers['valuedim'])
        return xnodes * ynodes * znodes * nOfComp + 1

    def save(self, path=None):
        if path is None:
            path = os.path.dirname(os.path.realpath(self._path)) + "/arr.npz"
        np.savez(path, array=self.array, headers=self.headers,
                 path=self._path, time=self.time)
        print("Data saved to the ", path)

    @property
    def avgtime(self):
        if os.path.isdir(self._path):
            return (self.time[-1] - self.time[0]) / len(self.time)
        else:
            return self.time

    @property
    def shape(self):
        return self.array.shape

    @property
    def geom_shape(self):
        return self.array.shape[1:4]

    @property
    def x(self):
        return self.array[0, 0, :, :, 0]

    @property
    def y(self):
        return self.array[0, 0, :, :, 1]

    @property
    def z(self):
        return self.array[0, 0, :, :, 2]


if __name__ == "__main__":
    pass

