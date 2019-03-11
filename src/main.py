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
import matplotlib.gridspec as gridspec
import numpy as np

if __name__ == "__main__":
    stat = Statistics()

    #DATA
    #INIT
    parms = parameters.ovfParms(head="m0", comp=0)
    #RUN
    mtzyxc = Marray("E:/Mumax3-Projekty/Radek/circular_10.out/arr.npz", parms)
    #SAVE
    #mtzyxc.save()
    #DATA

    #SPECTRUM
    #INIT
    spectrum = FMRSpectrum("Spektrum macierzy")
    #RUN
    # spectrum.calculate_fmr_spectrum(mtzyxc.y(copy=True), window="hanning", eachX=False, eachY=False, eachZ=False, zero_padd=False)
    #SAVE
    # spectrum.save("E:/Mumax3-Projekty/Radek/circular_10.out2/arr_spectrum.npz")
    spectrum.load("E:/Mumax3-Projekty/Radek/circular_10.out2/arr_spectrum.npz")
    #SPECTRUM


    #MODS
    #INIT
    mody = FMRmods()
    #RUN
    # mody.calculate_fmr_mods(mtzyxc.y(copy=True),
        # window="hanning", eachZ=True, zero_padd=False)
    #SAVE
    # mody.save("E:/Mumax3-Projekty/Radek/circular_10.out2/arr_mody.npz")
    mody.load("E:/Mumax3-Projekty/Radek/circular_10.out2/arr_mody.npz")
    #MODS

    ### PLOT EXAMPLE
    peaks = spectrum.peaks(thres=0.009, min_dist=2.5)

    for freq in peaks:

        plot = PreparePlot(2, 3)

        m_stable = Marray(
            "E:/Mumax3-Projekty/Radek/circular_10.out/m_stable_30.ovf", parms)
        
        sp1 = SubPlot(
                    position=plot.add(plot.grid[0:1, 0:2]),
                    ptype="plot", 
                    data = (spectrum.frequencies, spectrum.spectrum),
                    selected_freq = freq,
                    desc=mtzyxc.data._headers)
        sp1.ax.set_xlim((5e9, 15e9))
        sp1.add_peaks(spectrum.peaks(thres=0.009, min_dist=2.5))

        sp2 = SubPlot(
            position=plot.add(plot.grid[0:1, 2:None]),
            ptype="imshow",
            data=Hslcolormap.TransformToColor(
                    m_stable.data.array[0, 0, :, :, :]),
            desc=mtzyxc.data._headers)

        bottom_row = gridspec.GridSpecFromSubplotSpec(
            1, 2, subplot_spec=plot.grid[1:2, :])

        sp3 = SubPlot(
            position=plot.add(bottom_row[:, :1]),
            ptype="amplitude",
            data=(mody.frequencies, mody.mods),
            selected_freq=freq,
            desc=mtzyxc.data._headers)

        sp4 = SubPlot(
            position=plot.add(bottom_row[:, 1:]),
            ptype="phase",
            data=(mody.frequencies, mody.mods),
            selected_freq=freq,
            desc=mtzyxc.data._headers)

        plot.fig.suptitle("Frequency " +
                        str(np.round(mody.frequencies[freq]/1e9, 3)) + " GHz", fontsize=16)
    
        plot.adjust()
        # plot.show()
        plot.save(path="E:/Mumax3-Projekty/Radek/circular_10.out/" +
                  str(np.round(mody.frequencies[freq]/1e9, 3)) + " GHz.pdf")

    snapshot = stat.trace.take_snapshot()

    stat.display_top(snapshot)



