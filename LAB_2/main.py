# # ZAD 1
#
# lista_filmy = ["The Lord of the Rings", 'Pirates of the Caribbean',
#                'Léon', 'The Godfather',
#                'Inglourious Basterds', 'Scarface',
#                'The Gentlemen', 'Iron Man']
# lista_filmy.reverse()
# lista_filmy.insert(5, 'Drive')
# lista_filmy.insert(5, 'Schindlers List')
# print(lista_filmy)
#
# # ZAD 2
#
# slownik_filmy = {'film przygodowy': 'The Lord of the Rings, Pirates of the Caribbean',
#                  'dramat': 'Leon, The Godfather, Scarface, Iron Man',
#                  'kryminał': 'The Gentlemen',
#                  'wojenny': 'Inglourious Basterds'}
# print(slownik_filmy['film przygodowy'])
#
# # ZAD 3
#
# slownik_przedmioty = {'CAD': 'Komputerowe wspomoganie projektowania',
#               'PS': 'Programowanie Strukturalne',
#               'WD': 'Wizualizacja Danych',
#               'MD': 'Matematyka Dyskretna',
#               'AM': 'Analiza Matematyczna dla Informatyków',
#               'ET': 'Etyka',
#               'ENG': 'Język Angielski'}
#
# print(len(slownik_przedmioty))
#
# # ZAD 4
#
# a = input("Wprowadz liczbe")
# a = float(a)
# a = pow(a, a)
# print(a)

# ZAD 5

# import sys as system
# system.stdout.write("wpisz byle co")
# litera_a = system.stdin.readline()
# system.stdout.write(litera_a)
# print(litera_a.count('a'))

# ZAD 6
#
# import math
#
# a = input("Wprowadz liczbe a: ")
# b = input("Wprowadz liczbe b: ")
# c = input("Wprowadz liczbe c: ")
# a = int(a)
# b = int(b)
# c = int(c)
#
# if (a % 2 == 0) & (b > c):
#     print("Liczba a jest parzysta oraz jednocześnie b jest większe od c...")
# else:
#     print('oba warunki nie sa jednoczesnie spelnione')

# ZAD 7

# x = input("Wprowadz indeks x: ")
# x = int(x)
# list = [1, 2, 3, 4, 1.5, 2.5, 3.5, 4.5]
# x = list[x] + list[x - 1]
# print(x)
# Nie bardzo rozumiem, o co chodzi w poleceniu, zliczam element obecny ( poprzez podanie indeksu listy )
# z elementem poprzednim, aczkolwiek nie bardzo rozumiem jak powinienem zrobić to za pomocą pętli for

# ZAD 8

# list=[]
# z = 1
# a = 1
#
# while a < 11:
#     z = input("Wprowadz " + str(a) + " liczbe: ")
#     z = int(z)
#     a = a + 1
#     if z % 2 == 0:
#         list.append(z)
# print(list)

# ZAD 9

# a = 0
# list = [1, 2, 3, 4, 5, 6]
# for a in list:
#     if a == 1:
#         print('OOOOOO')
#     if a == 6:
#         print('OOOOOO')
#     else:
#         print('O    O')

# ZAD 10

# while 1:
#     try:
#         a = input("wprowadź cyfrę")
#         a = int(a)
#         break
#     except ValueError:
#         print('Błąd! Musisz podać cyfrę! Spróbuj jeszcze raz...')

