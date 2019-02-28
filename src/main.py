import parameters
from ovf import OvfFile
import matplotlib.pyplot as plt
import numpy as np
from hslcolormap import Hslcolormap

class prepareplot():
    def __init__(self,shape):
        self.fig = plt.figure()


if __name__ == "__main__":
    parms = parameters.ovfParms(head="m_y",comp=0)

    # mtzyxc = OvfFile(
    #     r"E:/arr.npz", parms)

    mtzyxc = OvfFile(
        "C:/Users/Mateusz/Desktop/Radek/circular_10.out2/arr.npz", parms)

    # mtzyxc.save("C:/Users/Mateusz/Desktop/Radek/circular_10.out2/arr.npz")

    mtzyxc.fmrspectrum(window="hanning", eachZ=False, comp=2)

    peaks = mtzyxc.peaks(mtzyxc.fmrspectrum, thres=0.0125, min_dist=5)

    ax1 = plt.subplot(2,1,1)
    ax1.plot(mtzyxc.fmrfreq, np.abs(
        mtzyxc.fmrspectrum))
    for x in peaks:
        plt.axvline(mtzyxc.fmrfreq[x])


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

    modes = mtzyxc.calculateModes(eachZ=False, comp=0, window="hanning")

    ax2 = plt.subplot(2, 1, 2)
    ax2.imshow(np.abs(modes[peaks[3], 0, :, :, 0]),
                origin="lower",
                aspect="equal")


    # parms = parameters.ovfParms()

    # M_Stable = OvfFile(
    #     r"C:/Users/Mateusz/Desktop/Radek/circular_10.out/m_stable_30.ovf", parms)

    # ax3 = plt.subplot(313)

    # # a = M_Stable.avrComponent
    # print(a.shape)

    # ax3.imshow(a[0,1,:,:],
    #            origin="lower",
    #            aspect="equal")
    plt.show()
