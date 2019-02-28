import parameters
from ovf import OvfFile
from prepareplot import Prepareplot

if __name__ == "__main__":
    parms = parameters.ovfParms(head="m_y", comp=0)

    # mtzyxc = OvfFile(
    #     r"E:/arr.npz", parms)

    mtzyxc = OvfFile(
        "C:/Users/Mateusz/Desktop/Radek/circular_10.out2/arr.npz", parms)

    # mtzyxc.save("C:/Users/Mateusz/Desktop/Radek/circular_10.out2/arr.npz")

    mtzyxc.fmrspectrum(window="hanning", eachZ=False, comp=2)

    peaks = mtzyxc.peaks(mtzyxc.fmrspectrum, thres=0.009, min_dist=2.5)

    p = Prepareplot(mtzyxc, peaks)
    p.plot_modes("C:/Users/Mateusz/Desktop/Radek/circular_10.out2/")



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
