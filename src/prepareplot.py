import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from hslcolormap import Hslcolormap
import cmocean
import matplotlib.style as style
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['text.latex.unicode'] = True
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['Tahoma']


class Prepareplot():
    def __init__(self, mtzyxc, peaks):
        self.mtzyxc = mtzyxc
        self.peaks = peaks

    def plot_modes(self, path):
        for x in self.peaks:

            print(str(np.round(self.mtzyxc.fmrfreq[x]/1e-9, 3)) + " GHz")

            style.use("seaborn-white")

            fig, ax = plt.subplots()

            grid = plt.GridSpec(2, 2, wspace=0.4, hspace=0.3)

            ax1 = plt.subplot(grid[0, :2])
            ax1.set_title("Frequency " +
                          str(np.round(self.mtzyxc.fmrfreq[x]/1e9, 3)) + " GHz")

            ax1.axvline(self.mtzyxc.fmrfreq[x]/1e9, color="red")
            for y in self.peaks:
                ax1.axvline(
                    self.mtzyxc.fmrfreq[y]/1e9, color="gray", alpha=0.2)
            fmr = np.abs(self.mtzyxc.fmrspectrum) / \
                np.amax(np.abs(self.mtzyxc.fmrspectrum))
            ax1.plot(self.mtzyxc.fmrfreq/1e9, fmr)
            ax1.set_ylabel("Amplitude (a.u.)")
            ax1.set_xlabel("Frequency (GHz)")

            modes = self.mtzyxc.calculateModes(
                eachZ=False, comp=0, window="hanning")

            ax2 = fig.add_subplot(grid[1, 0])
            # ax2.set_title("Amplitude (a.u)")
            ax2.set_ylabel("y (nm)")
            ax2.set_xlabel("x (nm)")

            mod = np.abs(modes[x, 0, :, :, 0]) / \
                np.amax(np.abs(modes[x, 0, :, :, 0]))
            amp = ax2.imshow(mod,
                             origin="lower",
                             cmap=cmocean.cm.haline,
                             extent=[0, modes.shape[2]*self.mtzyxc._headers["xstepsize"]/1e-9,
                                     0, modes.shape[3]*self.mtzyxc._headers["ystepsize"]/1e-9],
                             aspect="equal")
            cba = plt.colorbar(amp, ax=ax2)
            cba.set_label("Amplitude (a.u)")
            ax3 = fig.add_subplot(grid[1, 1])
            # ax3.set_title("Phase (degree)")

            phase = ax3.imshow(np.angle(modes[x, 0, :, :, 0], deg=1),
                               origin="lower",
                               cmap="hsv",
                               extent=[0, modes.shape[2]*self.mtzyxc._headers["xstepsize"]/1e-9,
                                       0, modes.shape[3]*self.mtzyxc._headers["ystepsize"]/1e-9],
                               aspect="equal")

            ax3.set_ylabel("y (nm)")
            ax3.set_xlabel("x (nm)")

            phase.set_clim(-180, 180)
            cbp = plt.colorbar(phase, ax=ax3, ticks=[-180, 0, 180])
            cbp.set_clim(-180, 180)
            cbp.set_label("Phase (degree)")
            ticks = [-1, 0, 1]

            cba.outline.set_linewidth(0.5)
            cbp.outline.set_linewidth(0.5)

            # cb.set_clim(-180, 180)
            for ax in [ax1, ax2, ax3]:
                ax.spines['top'].set_linewidth(0.5)
                ax.spines['right'].set_linewidth(0.5)
                ax.spines['bottom'].set_linewidth(0.5)
                ax.spines['left'].set_linewidth(0.5)
                ax.patch.set_linewidth(0.1)

            # plt.tight_layout()
            plt.savefig(path +
                        str(np.round(self.mtzyxc.fmrfreq[x]/1e9, 3)) + "GHz.pdf", dpi=600)
