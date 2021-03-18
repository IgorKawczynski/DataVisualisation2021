# # ZAD1
#
# import math
#
# A = [1-x for x in range(1, 11, 1)]
# print(A)
# B = [pow(4, x) for x in range(0, 8, 1)]
# print(B)
# C = [x for x in B if x % 2 == 0]
# print(C)

# # ZAD2
#
# import random
#
# list1 = []
# for x in range (1, 11):
#     a = random.randint(1, 50)
#     list1.append(a)
# print(list1)
# list2 = [x for x in list1 if x % 2 == 0]
# print(list2)


# # ZAD3
#
# sklep = {'bulka': 'szt', 'cukierki kopiko': 'kg', 'papryka': 'kg',
#          'konina': 'kg', 'woda kokosowa': 'l', 'sok marchwiowy': 'l',
#          'perfumy koko szalen': 'szt', 'Bacardi': 'szt'}
# sztuki1 = {key for (key,value) in sklep.items() if value == 'szt'}   # jako slownik
# sztuki2 = [key for (key,value) in sklep.items() if value == 'szt']   # jako lista
# print(sklep)
# print(sztuki1)
# print(sztuki2)

# # ZAD4
# def prostokatny(a, b, c):
#     if c*c == a*a + b*b:
#         print("Trojkat prostokatny")
#         return c*c == a*a + b*b
#     elif b*b == a*a + c*c:
#         print("Trojkat prostokatny")
#         return b*b == a*a + c*c
#     elif a*a == c*c + b*b:
#         print("Trojkat prostokatny")
#         return a*c == c*c + b*b
#     else:
#         print("Trojkat nie jest prostokatny")
#
#
# print(prostokatny(21, 7, 15))


# # ZAD5
#
# def trapez(a=4, b=6, h=6):
#     return ((a+b)/2)*h
#
#
# print(trapez())

# # ZAD6
#
# def ciag(a=1, b=4, ile=10):
#     i = 0
#     suma = 1
#     for i in range(i, ile):
#         iloczyn = a * b
#         suma *= iloczyn
#     return suma
#
# print(ciag())
# print(ciag(9, 8, 6))

# # ZAD7
#
# def ciag2(* liczby):
#     iloczynciag = 1
#
#     for i in range(0,liczby[2]):
#         mnozenie = liczby[0]*liczby[1]
#         iloczyn = mnozenie
#         iloczynciag *= iloczyn # iloczyn ciagu lacznie
#     return iloczynciag
#
#
# print(ciag2(9, 8, 6))

# # ZAD8
#
# def paragon(** rzeczy):
#     ile = len(rzeczy)
#     koszt = sum(rzeczy.values())
#     return print("Liczba produktow :", ile, "Cena produktow :", koszt)
#
#
# paragon(konina=59, amoniak=34, wafle=25, maslo=54, perfumy=21)

# zbior = {'jeden', 'dwa', 'trzy', 'cztery', 'itd'}
# print(zbior)
#
# krotka = 123, 'slowo', [1, 2, 3, 4, 5]
# print(krotka[1])


# # PYTHON COMPREHENSIVE -- uzupełnianie list, wpisywnaie do list, pętle w jednym wierszu,
# # w samej definicjii listy zamiast pisac oddzielnie petle
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list = [x for x in a if x % 2 == 0]
# print(list)
# print(a)
#
# print("\n")
#
# list_2 = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]
# print(list_2)
#
# # zamiana w slowniku klucza z wartosciami wersja z petla i wersja python comprehensive
#
# skroty = {"XD": "IKS DE", "LOL": "LAUGH", "SKROT CZEGOS": "WARTOSC CZEGOS"}
# odwrocone = {}
#
# for a, b in skroty.items(): # gdzie a to w kolejnosci jak w slowniku -- jest KLUCZ:WARTOSC
#     odwrocone[b] = a         # --- a to klucz, b to wartosc, zamieniamy klucz z wartoscia
# print(odwrocone)
#
#
# odwrocone_2 = {a: b for b, a in skroty.items()}
# print(odwrocone_2)
#
#
#
#
# import math
#
#
# def rownanie_kwadratowe(a,b,c):
#     delta = b * b - 4 * a * c
#     if delta < 0:
#         print("Nie ma rozwiazan")
#     elif delta == 0:
#         x = ((-1) * b) / (2 * a)
#         return x
#     else:
#         x1 = (-b + math.sqrt(delta)) / (2 * a)
#         x2 = (-b - math.sqrt(delta)) / (2 * a)
#         return x1, x2
#
# print(rownanie_kwadratowe(-2, 4, 5))
#


# def dlugosc(x1=0, y1=0, x2=0, y2=0):
#     return x1, y1, x2, y2
#
#
# print(dlugosc(y2=2, y1=4 , x2=3, x1=3))

# def suma_ciagu(* liczby):
#     if len(liczby) == 0:
#         return 0
#     else:
#         suma = 0
#         for i in liczby:
#             suma = suma + i
#         return suma
#
# print(suma_ciagu(1, 2, 3, 4, 5, 6, 41, 5))

# import math
#
# from pakiety import *
#
# a = 'ala ma ale'
# b = 'kota ma kote'
# litery.wyswietl(a, b)
# print(litery.dlugosc_stringow(a, b))
#
#
# print(rownaniekwadratowe.rownanie_kwadratowe(-2, 4, 5))