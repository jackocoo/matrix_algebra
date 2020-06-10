

from vector import Vector

import numpy as np


class Matrix():

	def __init__(self, rows, columns, column_vectors = []):

		self.rows = rows
		self.columns = columns

		self.data = column_vectors


	def set_data(self, column_vectors):
		self.data = new_data
		self.rows = self.data[0].size
		self.columns = len(column_vectors)


	def __add__(self, other):

		if self.rows != other.rows or self.columns != other.columns:
			return false

		new_column_list = []
		for i in range(self.columns):
			new_column = self.data[i] + other.data[i]
			new_column_list.append(new_column)

		new_matrix = Matrix(self.rows, self.columns, new_column_list)
		return new_matrix

	def __sub__(self, other):

		if self.rows != other.rows or self.columns != other.columns:
			return false

		new_column_list = []
		for i in range(self.columns):
			new_column = self.data[i] - other.data[i]
			new_column_list.append(new_column)
			
		new_matrix = Matrix(self.rows, self.columns, new_column_list)
		return new_matrix

	def __str__(self):

		output = "matrix: \n["
		for j in range(self.columns):
			for i in range(self.rows):
				output += str(self.data[i][j]) + ' '
			output = output[0: -1] + ']\n['
		output = output[0: -2]
		return output


