# from ovf import OvfFile
import parameters
import fft
import numpy as np
import peakutils


class FMRmods(fft.Fft):

	def __init__(self, name=None):
		self.mods = []
		self.frequencies = []
		self.peak_list = []
		self.name = name

	def check_component(self, comp):
		if self.array.shape[-1] == 1:
			return 0
		else:
			return comp

	def calculate_fmr_mods(self, marray, eachZ=False, window=None, comp=None, zero_padd=True):
		self.comp = comp
		self.eachX = True
		self.eachY = True
		self.eachZ = eachZ
		self.zero_padding = zero_padd
		self.window = window
		self.frequencies, self.mods = self.run_fft_for_mods(marray.data)
		
	def load(self, path):
		with np.load(path) as data:
			self.mods = data["mods"]
			self.frequencies = data["frequencies"]
		print("Data loaded successfully from  ", path)

	def save(self, path):
		np.savez(path, frequencies=self.frequencies, mods=self.mods)
		print("Data saved to the ", path)

	def peaks(self, data, thres=0.5, min_dist=30):
		self.peak_list = peakutils.indexes(np.abs(data), thres, min_dist)
