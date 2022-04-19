import numpy as np

#Zad 1
# a = np.arange(3).reshape((1,3))
# b = np.array([2,4.4,3.2])
# print(a*b)

#Zad 2
# a = np.array([[2,5,3],
#               [12,3,-4],
#               [4,8,0]])
# print(a)
# print(a.min(axis=1))
# print(a.min(axis=0))
# b = np.arange(16)
# b = b.reshape((4,4))
# print()
# print(b)
# print(b.min(axis=1))
# print(b.min(axis=0))

#Zad 3
# print(a.dot(b))

#Zad 4
# a = np.array([3,4,-3])
# b = np.arange(0.5,2,0.5).reshape((1,3))
# print(a*b)

#Zad 5
# matrix = np.arange(6).reshape((2,3))
# a = np.sin(matrix)
# print(a)

#Zad 6
# matrix = np.arange(6).reshape((2,3))
# b = np.cos(matrix)
# print(b)

#Zad 7
# print(a+b)

#Zad 8
# matrix = np.arange(9).reshape((3,3))
# for row in matrix:
#     print(row)

#Zad 9
# matrix = np.arange(0.1,1,0.1).reshape((3,3))
# for element in matrix.flat:
#     print(element)

#Zad 10
# matrix = np.arange(81).reshape((9,9))
# print(matrix)
# matrix2 = matrix.reshape((3,27))
# matrix3 = matrix.reshape((1,81))

#Zad 11
# vector1 = np.arange(12)
# vector1 = vector1.reshape((3,4))
# vector2 = vector1.reshape((4,3))
# vector3 = vector1.reshape((2,6))
# print(vector1.ravel())
# print(vector2.ravel())
# print(vector3.ravel())