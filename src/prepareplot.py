import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# from matplotlib import rcParams
from hslcolormap import Hslcolormap
import cmocean
import random
import matplotlib.style as style
# matplotlib.rcParams['mathtext.fontset'] = 'stix'
# matplotlib.rcParams['text.latex.unicode'] = True
# matplotlib.rcParams['font.family'] = 'sans-serif'
# matplotlib.rcParams['font.sans-serif'] = ['Tahoma']

class SubPlot():
    def __init__(self, ptype, data, freq = None):
        self.title = None
        self._data = data
        self._freq = freq
        self._ptype = ptype


        self.result = None

    def select_plot(self,ax):
        if self._ptype is "plot":
            self.prepare_plot(ax)
        elif self._ptype is "imshow":
            self.prepare_imshow(ax)
        else:
            pass
    def prepare_plot(self,ax):
        return ax.plot(self._data[0], np.abs(self._data[1]))
        
    def prepare_imshow(self,ax):
        
        return ax.imshow(np.abs(self._data[1][self._freq,:,:]))

    def get(self,ax):
        self.select_plot(ax)

    def make(self, acction):
        self.ax = acction


class PreparePlot():
    def __init__(self, lpx, lpy):
        self.fig, self.axes = plt.subplots(lpx*lpy)
        self.grid = plt.GridSpec(lpx, lpy, wspace=0.4, hspace=0.3)


    def def_add_element(self, data, par1 = None):
        self.axes.append()

    def place(self, obj, axis):
# 
        # _ax = plt.subplot( self.grid[0: None, None : 1] )
        print(axis[0], ":", axis[1], axis[2],":", axis[3])
        _ax = plt.subplot( self.grid[axis[0] : axis[1], axis[2] : axis[3]] )
        _ax = obj.get(_ax)
        # _ax 
        
        # self.axes[0]=obj.ax

    # def add_plot(self, axes=None, data_x, data_y):
    #     ax = plt.subplot(grid[axes])
    #     ax1.set_title("Frequency " +
    #                   str(np.round(self.mtzyxc.fmrfreq[x]/1e9, 3)) + " GHz")

    #     self.axes.append(ax)

    def show(self):
        plt.plot
        plt.show()


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
