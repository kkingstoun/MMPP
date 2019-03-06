import parameters
from ovf import OvfFile
from prepareplot import PreparePlot, SubPlot
from marray import Marray
from statistics import Statistics

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
if __name__ == "__main__":
    stat = Statistics()

    parms = parameters.ovfParms(head="m_y", comp=0)    
    mtzyxc = Marray("E:/Mumax3-Projekty/Radek/circular_10.out2/arr.npz", parms)
    # mtzyxc.save()
    spectrum = mtzyxc.y(copy=True).calculate_fmr_spectrum(
        window="hanning", eachX=True, eachY=True, eachZ=True, zero_padd=False)

    mody = mtzyxc.y(copy=True).calculate_fmr_modes(
        window="hanning", eachZ=True, zero_padd=True)

    plot = PreparePlot(3,3)

    x = np.arange(0,10,1)
    y = np.arange(0,20,2)

    sp1 = SubPlot("plot",spectrum)
    freq = 20

    ###########Rysunek #POŁOŻENIE
    plot.place(sp1, (0,1 , None,None))
    plot.place(sp2, (1,2 , None,-1))
    plot.place(sp1, (1,None, -1,None))
    # plot.place(sp,(0,2,None,0))
    # plot.place(sp,(0,1,None,1))
    plot.show()
    snapshot = stat.trace.take_snapshot()

    stat.display_top(snapshot)


    # mtzyxc = OvfFile(
    #     "E:/Mumax3-Projekty/Radek/Rect/", parms)

    # mtzyxc = OvfFile(
    #     "E:/Mumax3-Projekty/Radek/Rect/arr.npz", parms)

    # mtzyxc.save()
    
    # mtzyxc.fmrspectrum(window="hanning", eachZ=False, comp=0)
    # mtzyxc.x().fmrspectrum(window="hanning", eachZ=False)

    # mtzyx.c=

    # peaks = mtzyxc.peaks(mtzyxc.fmrspectrum, thres=0.009, min_dist=2.5)

    # p = Prepareplot(mtzyxc, peaks)
    # p.plot_modes("C:/Users/Mateusz/Desktop/Radek/nowe/abc")



# def plot_colormap():
#     pass
# M_szer_0 = Hslcolormap.TransformToColor(mtzyxc._array[100, 1, :, :, :])

# ax2 = plt.subplot(3, 1, 2)

# ax2.imshow(M_szer_0,
#            origin="lower",
#                        aspect="equal")

# X, Y = np.meshgrid(np.arange(0, mtzyxc._array.shape[2],1),
#                    np.arange(0, mtzyxc._array.shape[3], 1))
# U = mtzyxc._array[100, 1, X, Y, 0]
# V = mtzyxc._array[100, 1, X, Y, 1]
# C = mtzyxc._array[100, 1, X, Y, 2]
# Q = plt.quiver( X[::2, ::2],
#                 Y[::2, ::2],
#                 U[::2, ::2],
#                 V[::2, ::2],
#                 # C[::2, ::2],
#                 # units='x',
#                 # pivot='mid',
#                 color="black",
#                 # minlength = 2,
#                 # pivot='tip',
#                 # width=0.022,
#                 # scale=1/10
#                )
