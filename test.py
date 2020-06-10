
from vector import Vector
from matrix  import Matrix


def test():


	vec_one = Vector(3)
	vec_two = Vector(3)

	data_one = [1, 2, 3]
	vec_one.set_data(data_one)

	data_two = [4, 5, 6]
	vec_two.set_data(data_two)

	print(vec_one)
	print(vec_two)

	vec_three = vec_one + vec_two
	print("v1 + v2 = {0}".format(vec_three))

	column_vectors = [vec_one, vec_two, vec_three]

	mat_one = Matrix(3, 3, column_vectors)

	print(mat_one)

	mat_two = mat_one - mat_one
	print(mat_two)

	print(mat_one.transpose())

	print(mat_one * mat_two)


test()




