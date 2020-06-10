
import numpy as np

class Vector():

	def __init__(self, size, data = []):

		self.size = size
		self.data = data



	def set_data(self, new_data):
		self.data = np.array(new_data)
		self.size = len(self.data)



	def __add__(self, other):

		if self.size != other.size:
			print('sizes don\'t match' )
			return
		new_data = np.add(np.array(self.data), np.array(other.data))
		new_vector = Vector(len(new_data))
		new_vector.set_data(new_data)
		return new_vector

	def __sub__(self, other):

		if self.size != other.size:
			print('sizes don\'t match' )
			return
		new_data = np.subtract(np.array(self.data), np.array(other.data))
		new_vector = Vector(len(new_data))
		new_vector.set_data(new_data)
		return new_vector

	def __mul__(self, other):

		if self.size != other.size:
			print('sizes don\'t match' )
			return
		dot_product = np.dot(np.array(self.data), np.array(other.data))
		return dot_product


	def __getitem__(self, index):
		return self.data[index]


	def __setitem__(self, index, value):
		self.data[index] = value


	def __rmul__(self, other):
		return __mul__(self, other)


	def __str__(self):
		return str(self.data)




