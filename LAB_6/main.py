# Zad 1

import numpy as np

# a = np.arange(0, 80, 4)
# print(a)
#
# # Zad 2
#
# a2 = np.arange(1, 10, 0.2)
# print(a2)
# print(a2.dtype)
# a2_int32 = a2.astype('int32')
# print(a2_int32.dtype)

# Zad 3

#
# def function(n):
#     table = []
#     for x in range(0, n*n+1):
#         table.append(2 ** x)
#     table = np.array(table)
#     print(type(table))
#     return table
#
#
# print(function(3))  # table is gonna increment to element 2 ^ (n*n)

# # as in the instruction, table(matrix) of n*n x n*n dimension
# def function(n):
#     tablica = ([])
#     for x in range(0, (n*n)):
#         tablica.append(2 ** x)
#     tablica = np.array(tablica)
#     tablica = tablica.reshape(n, n)
#     print(tablica)
#     print(type(tablica))
#
#
# a = function(5)
# print(a)

# Zad 4

# # ???????????????????????????????????????????????????
# def generate_table(n, m):
#     for x in range(1, m+1):
#         a = np.logspace(# ?????)
#         print(a)
#
#
# print(generate_table(2, 4))


# def generate_table(n, m):
#     table = []
#     for x in range(1, m+1):
#         table.append(2 ** x)
#     table = np.array(table)
#     print(type(table))
#     return table
#
#
# print(generate_table(2, 4))

# Zad 5
#

# def generate_vector(n):
#     matrix = (np.array([x for x in range(n)]))
#     reversed_matrix = np.flip(matrix)
#     print(matrix)
#     print(reversed_matrix)
#     matrix_diag = np.diag([x for x in range(n)], 2)
#     print(matrix_diag)  # ????????????????????????????????????????????????????????????????????????????????
#
#
# print(generate_vector(5))

# Zad 6
#
# w = np.array([np.flip(['d', 'o', 'b', 'rz', 'e']),
#               ['ź', 'p', 'r', 'e', 'd'],
#               ['l', 'f', 'i', 'x', 'd'],
#               ['e', 'a', 'r', 'k', 'x'],
#               ['b', 'c', 'd', 'e', 'a']
#               ])
# print(w)

# Zad 7
# ????????????????????????????????????????????????????????? ? ? ?
# def generate(n):
#     macierz = np.zeros([n, n])
#     print(macierz)
#     macierz_diag2 = np.diag([2 for x in range(3)], 0)
#     macierz_diag4 = np.diag([4 for x in range(2)], 1)
#     macierz_diag4_2 = np.diag([4 for x in range(2)], -1)
#     macierz_diag6 = np.diag([6 for b in range(1)], 2)
#     macierz_diag6_2 = np.diag([6 for b in range(1)], -2)
#     macierz = macierz + macierz_diag2 + macierz_diag6_2 + macierz_diag4_2 + macierz_diag4 + macierz_diag6
#     print(macierz)
#
#
# print(generate(3))

# Zad 8 ????????????????????????????????????

# Zad 9
# ciag arytmetyczny o roznicy 2
A = np.arange(1, 50, 2)
A = A.reshape((5, 5))
print(A)



# a = np.arange(5)            # lista do pięciu
# print(a)
# b = np.array([0, 1, 3, 4])  # macierz
# print(b)
# print(type(b))
# print(b.dtype)
# b = np.array([0, 1, 3, 4], dtype='int64')  # stworzenie tablicy od razu z nadanym typem
# print(b.dtype)
# b = b.astype('float')
# print(b)
# print(b.dtype)  # nadanie tablicy innego typu, tym razem float
# print(b.shape)  # rozmiar tablicy
# print(b.ndim)   # ilość wymiarów tablicy
# w = np.array([np.arange(5), np.arange(5), np.arange(5), np.arange(5)])  # stworzenie macierzy 5-elem. o 4 wymiarach
# print(w)
# print(w.shape)
#
# a = np.zeros((5, 5))  # stworzenie macierzy 5-elem. 5-wymiarowej wypelnionej zerami
# b = np.ones(6)        # stworzenie macierzy 5-elem. 1-wymiarowej wypelnionej jedynkami
# print(a)
# print(b)
#
# pusta = np.empty((2, 4))  # W MACIERZACH NAJPIERW PODAJEMY LICZBĘ WIESZY, POTEM LICZBĘ KOLUMN
# print(pusta)              # tworzymy pusta macierz, ktora tak naprawde pusta nie jest
#
# poz1 = pusta[1, 1]        # mozna odwolac sie do elementu tablicy, podajac w indeksie ktory wiersz i kolumna,
# poz2 = pusta[0, 1]        # pamietajac ze inkrementacja jest od 0
# print(poz1)
# print(poz2)
#
# # tworzenie macierzy
#
# macierz1 = np.array([[1, 1, 5],
#                      [2, 3, 4],
#                      [7, 8, 9]
#                      ])
# print(macierz1)
#
# liczby1 = np.arange(1, 2, 0.25)
# print(liczby1)
#
# liczby_linspace = np.linspace(1, 2, 5)  # to samo co wyzej, ale metodą linspace, hgw
# print(liczby_linspace)
#
# d = np.indices((5, 4))  # tworzenie tablicy metodą, gdzie elementy się inkrementują, najpierw podaj wiersze potem klumny
# print(d)
# d2 = np.indices((2, 3))
# print(d2)
#
# x, y = np.mgrid[0:5, 0:5]
# print(x)
# print(y)
#
# macierz_diag = np.diag([a for a in range(5)])      # macierz diagonalna
# print(macierz_diag)
#
# macierz_diag2 = np.diag([b for b in range(5)], 1)  # okreslamy na jakiej przekatnej ma sie ten wektor znalezc
# print(macierz_diag2)
#
# z = np.fromiter(range(4), dtype='int32')           # w numpy mozna do macierzy wrzucic dowolny iterowany element,
# print(z)                                           # int czy float czy double czy inny
#
# marcin = b'MarcinMostowiak'                        # funkcja frombuffer dzieki ktorej mozna stworzyc np tablice znakow
# mar = np.frombuffer(marcin, dtype='S1')
# print(mar)
# # mar2 = np.frombuffer(marcin, dtype='S2')         # ten sposob ma w nowym pythonie jednak wade i trzeba wypisac b
# # print(mar2)
# # mar3 = np.frombuffer(marcin, dtype='S3')         # S1 znaczy, że wypisze po 1 literce, S3 ze program wypisze 3 litery
# # print(mar3)
#
# marcin = 'MarcinMostowiak'                         # sposób bez pisania b, lepszy dla pythona 3.x.x
# mar_x = np.array(list(marcin))
# mar_1 = np.array(list(marcin), dtype='S1')
# mar_2 = np.array(list(marcin), dtype='S2')
# mar_b = np.array(list(b'MarcinMostowiak'))
# mar_U = np.array(list(marcin), dtype='U1')
# mar_fromitter1 = np.fromiter(marcin, dtype='S1')
# mar_fromitter2 = np.fromiter(marcin, dtype='U1')
# print(mar_x)
# print(mar_1)
# print(mar_2)
# print(mar_b)
# print(mar_U)
# print(mar_fromitter1)
# print(mar_fromitter2)
#
# # TABLICE W NUMPY MOZNA DODAWAC, ODEJMOWAC, MNOZYC, DZIELIC, WSZYSTKO
#
# mat = np.ones((2, 2))
# mat1 = np.ones((2, 2))
# mat2 = np.array([[3, 3], [3, 3]])
# mat_arytmetyka = mat + mat1
# mat_arytmetyka2 = mat + mat2
# print(mat_arytmetyka)
# print(mat_arytmetyka2)
# # albo
# print(mat + mat1)
# print(mat/mat2)
#
# # Cięcia, indeksowanie tablic
#
# a = np.arange(11)
# print(a)
# s = slice(2, 7, 2)                               # slice = cięcie, START, STOP, STEP
# s2 = slice(2, 11, 2)
# print(a[s])
# print(a[s2])
#
# s = range(2, 7, 2)                               # 2-gi sposób
# print(a[s])
#
# print(a[2:7:2])                                  # 3-ci sposób
# print(a[1:])   # od jedynki do konca bez kroków
# print(a[2:5])  # od dwojki do piatki
#
# # i tak samo wzgledem tablic wielowymiarowych
#
# macierz = np.arange(25)
# macierz = macierz.reshape((5, 5))                # zmieniamy teraz, aby powyzsza macierz byla 5x5
# print(macierz)
# print(macierz[1:])        # od 2-giego wiersza
# print(macierz[:, 1])      # 2-ga kolumna jako wektor
# print(macierz[:, 1:2])    # 2-ga kolumna jako ndarray
# print(macierz[:, -1:])    # ostatnia kolumna
# print(macierz[2:6, 1:3])  # 2-ga i 3-cia kolumna dla 3,4,5 wierszy
#
#
# # inny sposób, bardziej zaawansowany
#
# x = np.array([[0, 1, 2],
#               [3, 4, 5],
#               [4, 2, 6],
#               [10, 8, 11]
#               ])
# print(x)
#
# wiersze = np.array([[0, 0], [3, 3]])
# kolumny = np.array([[0, 2], [0, 2]])
# y = x[wiersze, kolumny]
# print(y)              # y jako wierzchołki macierzy x
