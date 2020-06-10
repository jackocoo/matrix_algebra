# matrix_algebra


Basic algebra with matrices and vectors.

New vectors can be created as:
new_vector = Vector(size, data) #size is the number of entries in the vector and data is the list of entries (default empty)

Vectors support addition (v1 + v2), substraction (v1 - v2), and multiplication (v1 * v2) which is a dot product. 


New matrices can be created as:
new_mat = Matrix(rows, columns, data) #rows is number of rows, columns is number of columns, and data is the list of column                                          vectors ex) [Vector(3), Vector(3), Vector(3)] for 3x3 matrix (default empty). 

Matrices support addition (mat1 + mat2) and substraction (mat1 - mat2).
