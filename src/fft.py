import numpy as np
import math
import matplotlib.pyplot as plt
import multiprocessing as mp


class Fft:

	def _across(self, pos):
		for y in range(self.mtzyxc.shape[2]-1):
			print(y/self.mtzyxc.shape[2]*100, "%")
			for x in range(self.mtzyxc.shape[3]-1):
				self.MFft[:, y, x] = self._doFFT(
					self.mtzyxc.array[:, 0, y, x, 0])

	def _doFFT(self, arr):
		if self.zero_padding == True:
			arr = np.pad(
				arr, (0, 1024 - len(arr) % 1024), 'constant')
		return np.fft.rfft(arr*self.get_window(len(arr)))

	def __init__(self):
		pass
		# shape = self.array.shape
		# print(math.ceil(shape[0]/2), shape[1], shape[2], shape[3], shape[4])

	@property
	def selectAxis(self):

		a1 = (None, 1)[self.eachZ == True]
		a2 = (None, 2)[self.eachY == True]
		a3 = (None, 3)[self.eachX == True]
		return tuple(filter(None, [a1, a2, a3]))

	@property
	def unSelectAxis(self):
		a1 = (1, None)[self.eachZ == True]
		a2 = (2, None)[self.eachY == True]
		a3 = (3, None)[self.eachX == True]
		return tuple(filter(None, [a1, a2, a3]))

	def get_window(self, lenght):
		if self.window == "hanning":
			return np.hanning(lenght)
		else:
			return np.hanning(lenght)

	def run_fft_for_mods(self, data):
		data.array = self.average_magnetization(data)
		_shape = data.array.shape


		_pool = mp.Pool(processes=int(mp.cpu_count()-1))

		_arr = data.array.reshape(_shape[0], np.prod(_shape[1:4])).T
		_mody = _pool.map(self._doFFT, _arr)
		_pool.close()
		_pool.join()
		_mody = np.array(_mody).T
		_mody = _mody.reshape(
			_mody.shape[0], _shape[1], _shape[2], _shape[3])
		print(_mody.shape)
		_mody = np.average(_mody, axis=1)

		if self.zero_padding == True:
			_time = data.time.size + 1024 - data.time.size % 1024
		else:
			_time = data.time.size
		_frequencies = np.fft.rfftfreq(_time, data.avgtime)

		return _frequencies, _mody

	# def run_fft_for_mods2(self):
	# 	_shape = self.array.shape
	# 	self.MFft = np.zeros(
	# 		(math.ceil(_shape[0]/2), _shape[1], _shape[2], _shape[3], _shape[4]), dtype=np.complex64)
	# 	_axis = self.unSelectAxis
	# 	data = self.average_magnetization()
	# 	for z in range(data.shape[1]):
	# 		for y in range(data.shape[2]):
	# 			for x in range(data.shape[3]):
	# 				a = data[:, z, y, x, self.comp]
	# 				self.MFft[:, z, y, x, self.comp] = self._doFFT(a)
	# 	if self.eachZ == True:
	# 		self.MFft = np.average(self.MFft[:, z, y, x, self.comp], axis=1)
	# 		self.keep_size(self.MFft, _axis)
	# 	return self.MFft

	def keep_size(self, m, axis=None):
		tshape = list(self.data.array.shape)
		for ax in axis:
			tshape[ax] = 1
		# tshape[-1]=1
		m = m.reshape(tshape)
		return m

	def average_magnetization(self, data):

		_axis = self.unSelectAxis

		if _axis is None:
			_mag = np.average(
				data.array[:, :, :, :, self.comp], axis=_axis)
			return self.keep_size(_mag, _axis)
		else:
			return data.array[:, :, :, :, 0]

	def run_fft_for_spectrum(self,data):

		###
		# TODO:
		# 1. Multiprocessing
		###

		data.array = self.average_magnetization(data)

		_spectrum = []
		print(data.array.shape)
		for z in range(data.array.shape[1]):
			for y in range(data.array.shape[2]):
				for x in range(data.array.shape[3]):
					arr = data.array[:, z, y, x]
					_spectrum.append(self._doFFT(arr))

		_spectrum = np.array(_spectrum)
		_spectrum = np.average(_spectrum, axis=0)

		if self.zero_padding == True:
			time = data.time.size + 1024 - data.time.size % 1024
		else:
			time = data.time.size
		_frequencies = np.fft.rfftfreq(time, data.avgtime)

		return _frequencies, _spectrum
