import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# from matplotlib import rcParams
from mpl_toolkits.axes_grid1 import make_axes_locatable
from hslcolormap import Hslcolormap
import cmocean
import random
import seaborn as sns
import matplotlib.style as style
# matplotlib.rcParams['mathtext.fontset'] = 'stix'
# matplotlib.rcParams['text.latex.unicode'] = True
# matplotlib.rcParams['font.family'] = 'sans-serif'
# matplotlib.rcParams['font.sans-serif'] = ['Tahoma']


class SubPlot():
	def __init__(self, ptype=None, data=None, freq=None, desc=None):
		self.title = None

		self.shapex = desc['xnodes']*desc['xstepsize']
		self.shapey = desc['ynodes']*desc['ystepsize']
		self.colorbar = None

		self._data = data
		self._freq = freq
		self._ptype = ptype
		self.result = None
		self._desc = desc

	def add(self, ptype, data, freq=None):
		return SubPlot(ptype, data, freq, desc=self._desc)

	def select_plot(self, ax):
		if self._ptype is "plot":
			self.prepare_plot(ax)
		elif self._ptype is "amplitude":
			self.prepare_imshow_amplitude(ax)
		elif self._ptype is "phase":
			self.prepare_imshow_phase(ax)
		elif self._ptype is "imshow":
			self.prepare_imshow(ax)
		else:
			pass

	def add_avlines(self,peaks):

		for y in self.peaks:
				ax1.axvline(
					self.mtzyxc.fmrfreq[y]/1e9, color="gray", alpha=0.2)

	def prepare_plot(self, ax,freq):
		self.plot = ax.plot(self._data[0], np.abs(self._data[1]))
		ax.axvline(self._data[0][freq], color="red")
		ax.set_ylabel("Amplitude (a.u.)")
		ax.set_xlabel("Frequency (GHz)")
		return self.plot

	def prepare_imshow_amplitude(self, ax):
		im = ax.imshow(np.abs(self._data[1][self._freq, :, :]),
					   origin="lower",
                 	   extent=[0, self.shapex,
                         	   0, self.shapey],
						cmap=cmocean.cm.haline,
						aspect="equal"
					   )
		divider = make_axes_locatable(ax)
		cax = divider.append_axes("right", size="5%", pad=0.05)

		self.colorbar = plt.colorbar(im, cax=cax)
		self.colorbar.set_label("Amplitude (a.u.)")

		return im

	def prepare_imshow(self, ax):
		im = ax.imshow(self._data, 
				 origin="lower",
                 extent=[0, self.shapex,
                         0, self.shapey]
				 )
		ax.set_title="Magnetic configuration"
		return im

	def prepare_imshow_phase(self, ax):
		# print(np.abs(self._data[1][self._freq, :, :]).shape)
		shape = self._data[1]
		im = ax.imshow(np.angle(self._data[1][self._freq, :, :], deg=True),
						origin="lower",
						extent=[0, self.shapex,
								0, self.shapey],
						cmap=cmocean.cm.haline,
						aspect="equal"
						)
		divider = make_axes_locatable(ax)
		cax = divider.append_axes("right", size="5%", pad=0.05)

		self.colorbar  = plt.colorbar(im, cax=cax, ticks=[-180, 0, 180])
		im.set_clim(-180, 180)
		self.colorbar.set_clim(-180, 180)
		self.colorbar.set_label("Phase (degree)")
		return im

	def get(self, ax):
		if self._desc is not None:
			self.make_it_beuty(ax)
		self.select_plot(ax)

	def make_it_beuty(self, ax):
		ax.set_ylabel("y (nm)")
		ax.set_xlabel("x (nm)")
		pass


class PreparePlot():
	def __init__(self, lpx, lpy):
		self.fig, self.axes = plt.subplots(lpx*lpy)
		self.colorbars = []
		self.ai =0
		self.grid = plt.GridSpec(lpx, lpy, wspace=0.4, hspace=0.3)
		self.grid.update(hspace=0.5)
		style.use("seaborn-white")

	def def_add_element(self, data, par1=None):
		self.axes.append()

	def place(self, obj, axis):
		
		print(axis[0], ":", axis[1], axis[2], ":", axis[3])
		self.axes[self.ai] = plt.subplot(self.grid[axis[0]: axis[1], axis[2]: axis[3]])
		obj.get(self.axes[self.ai])
		if obj.colorbar != None:
			self.colorbars.append(obj.colorbar)
		self.ai += 1

	def adjust(self):
		for ax in self.axes:
			ax.spines['top'].set_linewidth(0.5)
			ax.spines['right'].set_linewidth(0.5)
			ax.spines['bottom'].set_linewidth(0.5)
			ax.spines['left'].set_linewidth(0.5)
			ax.patch.set_linewidth(0.1)
		for cb in self.colorbars:
			cb.outline.set_linewidth(0.5)

	def show(self):
		plt.show()

	def plot_mods(self, path):
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

			mods = self.mtzyxc.calculatemods(
				eachZ=False, comp=0, window="hanning")

			ax2 = fig.add_subplot(grid[1, 0])
			# ax2.set_title("Amplitude (a.u)")
			ax2.set_ylabel("y (nm)")
			ax2.set_xlabel("x (nm)")

			mod = np.abs(mods[x, 0, :, :, 0]) / \
				np.amax(np.abs(mods[x, 0, :, :, 0]))
			amp = ax2.imshow(mod,
							 origin="lower",
							 cmap=cmocean.cm.haline,
							 extent=[0, mods.self.shape[2]*self.mtzyxc._headers["xstepsize"]/1e-9,
									 0, mods.self.shape[3]*self.mtzyxc._headers["ystepsize"]/1e-9],
							 aspect="equal")
			cba = plt.colorbar(amp, ax=ax2)
			cba.set_label("Amplitude (a.u)")
			ax3 = fig.add_subplot(grid[1, 1])
			# ax3.set_title("Phase (degree)")

			phase = ax3.imshow(np.angle(mods[x, 0, :, :, 0], deg=1),
							   origin="lower",
							   cmap="hsv",
							   extent=[0, mods.self.shape[2]*self.mtzyxc._headers["xstepsize"]/1e-9,
									   0, mods.self.shape[3]*self.mtzyxc._headers["ystepsize"]/1e-9],
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
