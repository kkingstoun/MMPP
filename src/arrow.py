# import matplotlib


# from matplotlib.collections import PolyCollection
# from matplotlib import pyplot
import math
# import matplotlib.pyplot as plt
import parameters
from ovf import OvfFile
from marray import Marray
import numpy as np
import matplotlib.pyplot as plt
from hslcolormap import Hslcolormap

class Arrow:

    def drawArrows(self,data,arrowsize):
        Na = list(data.shape)
        h = Na[2]
        Na[2] = int(self.imax(Na[2]/arrowsize,1))
        Na[1] = int(self.imax(Na[1]/arrowsize,1))
        Na[0] = 1

        small = self.downSample(data, Na)
        small = np.swapaxes(small, 1, 2)
    
        self.arrows = []
        for iy in range(Na[2]):
            Ay = h - (iy+0.5)*arrowsize
            for ix in range(Na[1]):
                Ax = (ix + 0.5)*arrowsize
                mx = small[0, iy, ix, 2]
                my = small[0, iy, ix, 1]
                mz = small[0, iy, ix, 0]
                self.arrows.append(self.arrow(Ay,Ax,mz,my,mx,arrowsize))
        return self.arrows

    def arrow(self, x,y,mx,my,mz,arrowsize):
            arrlen = 0.4*arrowsize
            arrw = 0.2*arrowsize

            norm = math.sqrt(mx*mx+my*my +mz*mz)

            if norm == 0:
                return
            if norm > 1:
                norm = 1

            theta = math.atan2(my,mx)
            cos = math.cos(theta)
            sin = math.sin(theta)
            r1 = arrlen * norm * math.cos(math.asin(mz))
            r2 = arrw * norm
            
            points = []

            points.append(((r1*cos)+x, -(r1*sin)+y))
            points.append(((r2*sin-r1*cos)+x, -(-r2*cos-r1*sin)+y))
            points.append(((-r2*sin-r1*cos)+x, -(r2*cos-r1*sin)+y))
            return(points)

    def imax(self, a,b):
        if a > b:
            return a
        else:
            return b

    def downSample(self, In, shape):
        Out = np.zeros(shape)

        srcsize = In.shape
        dstsize = Out.shape

        Dx = dstsize[2]
        Dy = dstsize[1]
        Dz = dstsize[0]
        Sx = srcsize[2]
        Sy = srcsize[1]
        Sz = srcsize[0]

        scalex = int(Sx / Dx)
        scaley = int(Sy / Dy)
        scalez = int(Sz / Dz)

        for c in range(In.shape[3]):
            for iz in range(Dz):
                for iy in range(Dy):
                    for ix in range(Dx):
                        suma, n = 0.0, 0.0
                        for I in range(scalez):
                            i2 = iz *scalez + I
                            for J in range(scaley):
                                j2 = iy * scaley + J
                                for K in range(scalex):
                                    k2 = ix*scalex + K
                                    if i2 < Sz and j2 < Sy and k2 < Sx:
                                        # print(k2, j2, i2, c)
                                        suma += In[i2,j2,k2,c]
                                        n +=1
                        Out[iz, iy, ix, c] = suma/n
        return Out




