import math
from pandas import DataFrame
import numpy as np
from pandas import DataFrame

class Attribute:
	"""The Attribute class offers and manages information about an specific feature of the dataset"""


	def __init__(self, v, name):
		"""Constructor function"""
		self.v = v
		self.size = len(v)
		self.name = name

	def discretizeEW(self, num_bins):
		"""Discretize the data to map the numeric values to categorical values, using equal width as the method to create intervals."""
		if isinstance(self.v[0], int) or isinstance(self.v[0], float):
			if num_bins < 1:
				print("num_bins has to be equal or greater than 1")
				return self
			minimum = min(self.v)
			maximum = max(self.v)
			step = (maximum - minimum) / num_bins
			levels = [(minimum + step) * (x + 1) for x in range(num_bins)]
			x_discretized = self.get_labels(self.v, levels)
			a = Attribute(x_discretized, self.name)
			return a, set(x_discretized)
		return self, None

	def get_labels(self, x, levels):
		"""Given the limits of each interval and the data, maps the data to the corresponding label with shape (lower, upper)."""
		res = []
		for value in x:
			# Identify to what range it belongs
			rang = self.get_value_range(value, levels)
			if rang == 0:
				label = "(inf," + str(levels[rang]) + ")"
			elif rang == len(levels):
				label = "(" + str(levels[rang - 1]) + ",inf)"
			else:
				label = "(" + str(levels[rang - 1]) + "," + str(levels[rang]) + ")"
			res.append(label)
		return res

	def get_value_range(self, x, levels):
		"""Given a value and a vector of each of the limits, it return the index of the upper limit of the value, where the value is
		between the previous value and the upper limit value"""
		pos = 0
		for rang in levels:
			if x < rang:
				return pos
			pos += 1
		return len(levels)

	def discretizeEF(self, num_bins):
		"""Discretize the data to map the numeric values to categorical values, using equal width as the method to create intervals."""
		if isinstance(self.v[0], int) or self.isinstance(self.v[0], float):
			if num_bins < 1:
				print("num_bins has to be equal or greater than 1")
				return self
			length = len(self.v)
			step = int(length / num_bins)
			sort = sorted(self.v)
			count = 1
			levels = []
			while count * step < length:
				levels.append(sort[count*step])
				count = count + 1
			if (count * step != length):
				levels.append(sort[-1])
			x_discretized = self.get_labels(sort, levels)
			a = Attribute(x_discretized, self.name)
			return a, set(x_discretized)
		return self, None

	def discretize(self, cut_points):
		"""Discretize the data using the cut_points for mapping the numeric data into categorical data"""
		if isinstance(self.v[0], int) or isinstance(self.v[0], float):
			if cut_points is None:
				print("cut_points has to be an array")
				return self
			x_discretized = self.get_labels(self.v, cut_points)
			a = Attribute(x_discretized, self.name)
			return a, set(x_discretized)
		return self, None

	def entropy(self):
		"""Calculates the entropy of a categorical vector"""
		res = 0
		for label in set(self.v):
			prob = len(list(filter(lambda x: x == label, self.v))) / len(self.v)
			res = res - (prob * math.log(prob, 2))
		return res

	def estandarize(self):
		"""Estandarizes the data following this formula: (x - mean) / sd"""
		if isinstance(self.v[0], int) or isinstance(self.v[0], float):
			mean = np.mean(self.v)
			module = np.linalg.norm(self.v, 2)
			a = Attribute(list((np.array(self.v) - mean) / module), name=self.name)
			return a
		return self

	def normalize(self):
		"""Normalizes the data dividing all the elements by the maximum"""
		if (isinstance(self.v[0], int) or isinstance(self.v[0], float)) and len(self.v) > 0:
			maxim = max(self.v)
			a = Attribute(list(np.array(self.v) / maxim), name=self.name)
			return a
		return self

	def variance(self):
		"""Computes the variance of numeric data"""
		if isinstance(self.v[0], int) or isinstance(self.v[0], float):
			avg = sum(self.v) / len(self.v)
			var = sum((x - avg) ** 2 for x in self.v) / len(self.v)
			return var

	def __str__(self):
		"""String output of the data"""
		res = "\n Attribute object"
		res += "\n ----------------"
		res += "\n Name: " + self.name
		res += "\n Size: " + str(self.size)
		res += "\n Values: \n\t" + str(self.v)
		return res

	def append(self, elem):
		"""Adds en element to the attribute"""
		self.v.append(elem)
		self.size += 1
