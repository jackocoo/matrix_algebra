

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


	#NEW_MATRIX = SELF + OTHER
	def __add__(self, other):

		if self.rows != other.rows or self.columns != other.columns:
			return false

		new_column_list = []
		for i in range(self.columns):
			new_column = self.data[i] + other.data[i]
			new_column_list.append(new_column)

		new_matrix = Matrix(self.rows, self.columns, new_column_list)
		return new_matrix


	#NEW_MATRIX = SELF - OTHER
	def __sub__(self, other):

		if self.rows != other.rows or self.columns != other.columns:
			return false

		new_column_list = []
		for i in range(self.columns):
			new_column = self.data[i] - other.data[i]
			new_column_list.append(new_column)
			
		new_matrix = Matrix(self.rows, self.columns, new_column_list)
		return new_matrix


	#in new matrix, column 1 of self becomes row 1 of new matrix, etc
	def transpose(self):

		new_vec_list = []

		for j in range(self.columns):
			new_column = []
			for i in range(self.rows):
				new_column.append(self.data[i][j])
			new_col_vec = Vector(len(new_column), new_column)
			new_vec_list.append(new_col_vec)
		new_matrix = Matrix(new_vec_list[0].size, len(new_vec_list), new_vec_list)
		return new_matrix

	
	#applies multiplication as NEW_MAT = SELF * OTHER 
	def __mul__(self, other):

		if self.columns != other.rows:
			print("shapes do not align for matrix multiplication")
			return 

		self_transpose = self.transpose()
		new_column_list = []
		#choose a column vector in other 
		for col in other.data: 
			new_column = []

			for vec in self_transpose.data:
				new_column.append(col * vec)

			new_vec = Vector(len(new_column), new_column)
			new_column_list.append(new_vec)

		new_mat = Matrix(new_column_list[0].size, len(new_column_list), new_column_list)
		return new_mat
	

	def __str__(self):

		output = "matrix: \n["
		for j in range(self.columns):
			for i in range(self.rows):
				output += str(self.data[i][j]) + ' '
			output = output[0: -1] + ']\n['
		output = output[0: -2]
		return output


