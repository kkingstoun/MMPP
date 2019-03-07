import fft
import numpy as np
import peakutils


class FMRSpectrum(fft.Fft):

	def __init__(self, name=None):
		self.spectrum = []
		self.frequencies = []
		self.peak_list = []
		self.name = name

	def calculate_fmr_spectrum(self, marray, eachX=False, eachY=False, eachZ=False, window=None, comp=None, zero_padd=True):
		self.comp = comp
		self.eachX = eachX
		self.eachY = eachY
		self.eachZ = eachZ
		self.zero_padding = zero_padd
		self.window = window
		self.frequencies, self.spectrum = self.run_fft_for_spectrum(marray.data)
		# return(self.frequencies, self.mods)

	def peaks(self, data, thres=0.5, min_dist=30):
		self.peak_list = peakutils.indexes(np.abs(data), thres, min_dist)
		return self.peak_list

	def load(self, path):
		with np.load(path) as data:
			self.spectrum = data["spectrum"]
			self.frequencies = data["frequencies"]
		print("Data loaded successfully from  ", path)

	def save(self, path):
		np.savez(path, frequencies=self.frequencies, spectrum = self.spectrum)

		print("Data saved to the ", path)
