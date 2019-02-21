from ovf import OvfFile

class Mtzyxc(OvfFile):

    def __init__(self, mtzyxc):
        self.mtzyxc=mtzyxc
        
    @property
    def array(self):
        return self.mtzyxc._array

    @property
    def shape(self):
        return self._array.shape

    @property
    def time(self):
        return self._time

    @property
    def headers(self):
        return self._headers

    # def __init__(self):
    #     self.mtzyxc = mtzyxc
    #     self.headers = headers
    #     self.time = time
