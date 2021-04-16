import numpy as np
import math as mat

# # HOMEWORK

# # ZAD 1

# a = np.arange(1, 5, 1)
# print(a)
# b = np.arange(4, 8, 1)
# print(b)
# c = a * b
# print(c)

# # ZAD 2

# a = np.arange(11, 20, 1)
# a = a.reshape(3, 3)
# print(a)
# print("\n")
# print(a.min(axis=0))
# print("\n")
# print(a.min(axis=1))
# print("\n")
# b = np.arange(14, 30, 1)
# b = b.reshape(4, 4)
# print(b)
# print("\n")
# print(b.min(axis=0))
# print("\n")
# print(b.min(axis=1))

# # ZAD 3

# a = np.arange(1, 5, 1)
# print(a)
# print("\n")
# b = np.arange(4, 8, 1)
# print(b)
# print("\n")
# print(np.dot(a, b))

# # ZAD 4

# a = np.ones(3, dtype='int32')
# b = np.linspace(0, np.pi, 3)
# c = a * b
# d = np.dot(a, b)
# print(c)
# print(c.dtype)
# print("\n")
# print(d)
# print(d.dtype)

# # ZAD 5, 6, 7

# matrix = np.linspace(0, np.pi, 6)
# matrix = matrix.reshape(2, 3)
# print(matrix)
# print("\n")
# a = np.sin(matrix)
# print(a)
# print("\n")
#
# matrix2 = np.linspace(0, np.pi, 6)
# matrix2 = matrix2.reshape(2, 3)
# print(matrix2)
# print("\n")
# b = np.cos(matrix2)
# print(b)
# print("\n")
#
# c = np.add(a, b)
# print(c)

# # ZAD 8

# a = np.arange(9)
# a = a.reshape(3, 3)
# for x in a:
#     print(x)

# # ZAD 9

# a = np.arange(9)
# a = a.reshape(3, 3)
# for x in a.flat:
#     print(x)

# # ZAD 10

# a = np.arange(81)
# print(a)
# # Mamy mnóstwo sposobów na zmianę kształtu macierzy :
# # Możemy to zrobić poprzez komendę reshape :
# a = a.reshape(9, 9)
# # W pętli możemy to zrobić poprzez komendę flat, która ,,spłaszczy'' nam całą macierz do jednej kolumny :
# for x in a.flat:
#     print(x)
# # Możemy to zrobić poprzez komendę ravel, która ,,spłaszczy'' nam całą macierz, przywróci ją do pierwotnego stanu :
# a = a.ravel()
# print(a)
# # Możemy również dokonać transpozycji macierzy, która jednak nie zmieni nam wymiaru tablicy, a jedynie
# # przemieni wartości z kolumn z wartościami wierszy
# a = a.reshape(9, 9)
# a = a.T
# print(a)

# # ZAD 11

a = np.arange(12)
print(a)
print("\n")
a = a.reshape(3, 4)
print(a)
print("\n")
a = a.ravel()
print(a)
print("\n")
a = a.reshape(4, 3)
print(a)
print("\n")
a = a.ravel()
print(a)
print("\n")
a = a.reshape(2, 6)
print(a)
print("\n")
a = a.ravel()
print(a)
print(u"Są identyczne")


# # # # UZUPELNIENIE LECKJI

# # # # Operations on vectors -- arrays -- matrix

# a = np.array([50, 40, 30, 20, 40])
# b = np.arange(5)
# print(a)
# print("\n")
# print(b)
# print("\n")
# c = a - b
# print(c)
# print("\n")
# print(pow(b, 2))
# a = a + a
# print("\n")
# print(a)
# print("\n")
#
# # # # # OPERATIONS ON AXISES
#
# a = np.arange(20).reshape(4, 5)
# print(a)
# print(a.sum())
# # # # Sum of columns
# print(a.sum(axis=0))
# print("\n")
# print(a.sum(axis=1))
# print("\n")
# print(a.max(axis=1))
# print("\n")
# print(a.min(axis=1))
# print("\n")
# print(a.max(axis=1))
# print("\n")
# print(a.cumsum(axis=1))
#
# # # # # PRODUCT
#
# a = np.arange(3)
# b = np.arange(3)
# print(a.dot(b))  # matrix product
# print(np.dot(a, b))  # secound solution for matrix product
# print("\n")
#
# # # # # OPERATIONS ON ARRAYS WITH DIFFERENT ACCURATENESS
#
# # INT MATRIX
# a = np.ones(3, dtype='int32')
# print(a.dtype)
# print(a)
# print("\n")
# # FLOAT MATRIX
# a = np.linspace(0, np.pi, 3)
# print(a.dtype)
# print(a)
# print("\n")
# # TYPE OF SUM OF THOSE 2 MATRIX IS FLOAT
# c = a + b
# print(c.dtype)
# print(c)
# print("\n")
# # ZESPOLONES MATRIX
# d = np.exp(c * 1j)
# print(d.dtype)
# print(d)
# print("\n")
# # FUNCTIONS
# b = np.arange(5)
# print(b)
# print(np.exp(b))
# print(np.sqrt(b))
# print(pow(b, 2))
# c = np.array([2., -1., 5.4, 4., 6.])
# print(c)
# print(np.add(b, c))  # SUM OF VALUES, EACH ELEMENT
# print("\n")
# # ITERATION ON ARRAYS ( AXIS X )
# a = np.arange(12).reshape(3, 4)
# print(a)
# for x in a:
#     # iteration within first axis -- AXIS  X
#     print(x)
# print("\n")
# # FULL ITERATION ON ARRAYS ( AXIS X AND Y )
# a = np.arange(12).reshape(3, 4)
# print(a)
# for x in a.flat:
#     # iteration within AXIS  X and AXIS Y -- matrix called as FLAT
#     print(x)
# print("\n")
# # PRZEKSZTALCENIAS
# a = np.arange(6)
# a = a.reshape(2, 3)
# print(a)
# print(a.shape)  # PRINT SHAPE, colums and rows
# print("\n")
# b = np.array([np.arange(3),
#               np.arange(3),
#               np.arange(3)])
# print(b)
# print(b.shape)  # PRINT SHAPE
# print("\n")
# # SHAPING ARRAYS
# a = np.arange(20)
# print(a)
# print("\n")
# a = a.reshape(4, 5)
# print(a)
# print("\n")
# a = a.reshape(5, 4)
# print(a)
# print("\n")
# a = a.ravel()
# print(a)
# print("\n")
# # TRANSPOSITION
# e = np.arange(6)
# e = e.reshape(2,3)
# e = e.T
# print(e)









