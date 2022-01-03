import pandas

from dataset.Attribute import Attribute
import math
import matplotlib.pyplot as plt
import seaborn as sns

class Dataset:
	"""This class represents a dataset where there are multiple columns, an index and the size"""

	def __init__(self):
		"""Constructor function"""
		self.index = Attribute([], "index")
		self.size = 0
		self.columns = []
		self.target = Attribute([], "target")

	def add_column(self, name, values=None):
		"""Adds a column/attribute to the dataset. For that, a vector of values can be passed to initialize the attribute. """
		if not values is None:
			if not len(values) == self.size:
				print("Please, provide a value for all the rows")
				return self
			else:
				a = Attribute(values, name)
		else:
			a = Attribute([None] * self.size, name)
		self.columns.append(a)
		return self

	def append(self, v):
		"""Adds a row to the dataset. For that, the vector needs to have as many elements as columns are im the dataset plus the
		target class"""
		if len(v) != len(self.columns) + 1:
			print("please, you have to provide one value for each column and the class value")
			return self
		else:
			self.size += 1
			self.index.append(self.size)
			cont = 0
			for col in self.columns:
				col.append(v[cont])
				cont += 1
			self.target.append(v[cont])
		return self

	def estandarize_dataset(self):
		"""Estandarizes all the attributes in the dataset that are numeric. The others remain the same"""
		for i, col in enumerate(self.columns):
			self.columns[i] = col.estandarize()
		return self

	def normalize_dataset(self):
		"""Normalizes all the attributes in the dataset that are numeric. The others remain the same"""
		for i, col in enumerate(self.columns):
			self.columns[i] = col.estandarize()
		return self

	def col_entropy(self):
		"""Computes the entropy per each of the columns that have categorical data. The result is a vector where each position
		corresponds to each of the columns. A None is placen when the column is not categorical"""
		res = []
		for col in self.columns:
			res.append(col.entropy())
		return res

	def col_var(self):
		"""Computes the variance per each of the columns that have numeric data. The result is a vector where each position
		corresponds to each of the columns. A None is placen when the column is not numeric"""
		res = []
		for col in self.columns:
			res.append(col.variance())
		return res

	def discretize_dataset(self, method='EF', num_bins=3):
		"""Discretizes all the columns in the dataset following the method and the number of bins provided. As a result, all the
		variables in the dataset will be categorical"""
		for i, col in enumerate(self.columns):
			if method == 'EF':
				self.columns[i], _ = col.discretizeEF(num_bins=num_bins)
			else:
				self.columns[i], _ = col.discretizeEW(num_bins=num_bins)
		return self

	def __str__(self):
		"""Outputs the dataset in a string format"""
		res = "Dataset object"
		res += "\n------------------------"
		res += "\nSize: " + str(self.size)
		res += "\n"
		for col in self.columns:
			res += str(col)
		res += str(self.target)
		return res

	def normalized_entropy_plot(self):
		"""Plots the normalized entropy plot, by computing the entropy of each of the columns in the data DataFrame
        and dividing it by the maximum achievable value for the entropy per column"""
		res = []
		for col in self.columns:
			maximum = math.log(len(set(col.v)), 2)
			res.append((col.entropy() / maximum))
		plt.bar([x.name for x in self.columns], res)

	def correlation_plot(self):
		"""Plots the correlation heatmap by computing the correlation between each of the columns of the dataset"""
		df = pandas.DataFrame({c.name: c.v for c in self.columns})
		cor = df.corr()
		sns.heatmap(cor)