import parameters
from ovf import OvfFile
import matplotlib.pyplot as plt
import numpy as np
from hslcolormap import Hslcolormap

if __name__ == "__main__":
    parms = parameters.ovfParms(head="m_y",comp=0)

    mtzyxc = OvfFile(
        "C:/Users/Mateusz/Desktop/Radek/circular_10.out2/arr.npz", parms)

    #Przykład zapisu do pliku
    # mtzyxc.save("C:/Users/Mateusz/Desktop/Radek/circular_10.out2/arr.npz")

    mtzyxc.fmrspectrum(window="hanning", eachX=True,
                       eachY=True, eachZ=False, comp=2)

    peaks = mtzyxc.peaks(mtzyxc.fmrspectrum, , thres=0.5, min_dist=5)

    plt.plot(mtzyxc.fmrfreq, np.abs(
        mtzyxc.fmrspectrum))
    for x in peaks:
        plt.axvline(mtzyxc.fmrfreq[x])


    # M_szer_0 = Hslcolormap.TransformToColor(mtzyxc._array[100, 1, :, :, :])
    

    # plt.imshow(M_szer_0,
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

    # plt.plot(spectrum. )11
    # modes, peaks, = mtzyxc.calculateModes(eachX=True, eachY=True, comp=0, window="hanning")
    # vm.calculateModes()

    # print(peaks)

    # ax1 = plt.subplot(211)
    # x = np.fft.rfftfreq(mtzyxc._array.shape[0], 2e-11)
    # y = np.abs(np.average(modes[:, 0, :, :, 0], axis=(1, 2)))
    # print(y.shape)
    # # y = self.MFft
    # # print(y.shape)
    # plt.plot(y)
    # # print(y)
    # ax2 = plt.subplot(212)

    # ax2.imshow(np.abs(modes[105, 0, :, :, 0]),
    #             origin="lower",
    #             aspect="equal")

    plt.show()
