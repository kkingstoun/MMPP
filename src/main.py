import parameters
from ovf import OvfFile
from prepareplot import PreparePlot, SubPlot
from marray import Marray
from statistics import Statistics
from fmrmods import FMRmods
from hslcolormap import Hslcolormap
from fmrspectrum import FMRSpectrum

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    stat = Statistics()

    parms = parameters.ovfParms(head="m0", comp=0)
    mtzyxc = Marray("E:/Mumax3-Projekty/Radek/circular_10.out/arr.npz", parms)
    # mtzyxc.save()

    # exit()
    #SPEKTRUM
    spectrum = FMRSpectrum("Spektrum macierzy")
    # spectrum.calculate_fmr_spectrum(mtzyxc.y(copy=True), window="hanning", eachX=False, eachY=False, eachZ=False, zero_padd=True)
    # spectrum.save("E:/Mumax3-Projekty/Radek/circular_10.out2/arr_spectrum.npz")
    spectrum.load("E:/Mumax3-Projekty/Radek/circular_10.out2/arr_spectrum.npz")
    #KONIEC SPEKTRUM


    #MODY
    mody = FMRmods()
    # mody.calculate_fmr_mods(mtzyxc.y(copy=True),
        # window="hanning", eachZ=False, zero_padd=True)
    # mody.save("E:/Mumax3-Projekty/Radek/circular_10.out2/arr_mody.npz")
    mody.load("E:/Mumax3-Projekty/Radek/circular_10.out2/arr_mody.npz")

    plot = PreparePlot(2, 2)

    m_stable = Marray(
        "E:/Mumax3-Projekty/Radek/circular_10.out/m_stable_30.ovf", parms)

    sp = SubPlot(desc=mtzyxc.data._headers)

    
    freq = 440

    sp1 = sp.add("plot", (spectrum.frequencies,spectrum.spectrum),freq)
    sp2 = sp.add("imshow", Hslcolormap.TransformToColor(
        m_stable.data.array[0, 0, :, :, :]))


   

    sp3 = sp.add("amplitude", (mody.frequencies, mody.mods), freq)
    sp4 = sp.add("phase", (mody.frequencies, mody.mods), freq)
    plot.fig.suptitle("Frequency " +
                      str(np.round(mody.frequencies[freq]/1e9, 3)) + " GHz", fontsize=16)
    # Rysunek #POŁOŻENIE
    plot.place(sp1, (0, 1, 0, 1))
    plot.place(sp2, (0, 1, 1, None))
    plot.place(sp3, (1, 2, 0, 1))
    plot.place(sp4, (1, 2, 1, None))
    # plot.place(sp,(0,2,None,0))
    # plot.place(sp,(0,1,None,1))
    plot.adjust()
    plot.show()
    # snapshot = stat.trace.take_snapshot()

    # stat.display_top(snapshot)

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
    # p.plot_mods("C:/Users/Mateusz/Desktop/Radek/nowe/abc")


# def plot_colormap():
#     pass
# M_szer_0 = Hslcolormap.TransformToColor(mtzyxc.array[100, 1, :, :, :])

# ax2 = plt.subplot(3, 1, 2)

# ax2.imshow(M_szer_0,
#            origin="lower",
#                        aspect="equal")

# X, Y = np.meshgrid(np.arange(0, mtzyxc.array.shape[2],1),
#                    np.arange(0, mtzyxc.array.shape[3], 1))
# U = mtzyxc.array[100, 1, X, Y, 0]
# V = mtzyxc.array[100, 1, X, Y, 1]
# C = mtzyxc.array[100, 1, X, Y, 2]
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
