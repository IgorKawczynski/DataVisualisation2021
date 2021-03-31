# Zad 1
#
# class Material:
#     def __init__(self, rodzaj, dlugosc, szerokosc):
#         self.rodzaj = rodzaj
#         self.dlugosc = dlugosc
#         self.szerokosc = szerokosc
#
#     def wyswietlnazwe(self):
#         return "Rodzaj - {}, Dlugosc - {}, Szerokosc - {}".format(self.rodzaj, self.dlugosc, self.szerokosc)
#
#
# class Ubrania(Material):
#
#     def __init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo):
#         Material.__init__(self, rodzaj, dlugosc, szerokosc)
#         self.rozmiar = rozmiar
#         self.kolor = kolor
#         self.dla_kogo = dla_kogo
#
#     def wyswietl_dane_ubrania(self):
#         return "Rozmiar - {}, Kolor - {}, Dla kogo - {}" .format(self.rozmiar, self.kolor, self.dla_kogo)
#
#
# class Sweter(Ubrania):
#
#     def __init__(self, rodzaj_swetra, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo):
#         Ubrania.__init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo) # JESLI W KLASIE JEST DZIEDZICZENIE (Ubrania, to tutaj mozna tylko odwolac sie do klasy dziedziczonej ( w dziedziczonej juz bylo odniesienie do klasy material i dlatego w niej dodaj wszystko ) )
#         self.rodzaj_swetra = rodzaj_swetra
#
#     def wyswietl_dane_swetra(self):
#         return "Rodzaj swetra - {}," \
#                "Rodzaj materiału - {}, " \
#                "Dlugosc - {}, " \
#                "Szerokosc - {}, ""Rozmiar - {}, " \
#                "Kolor - {}, Dla - {}" \
#                    .format(self.rodzaj_swetra,
#                            self.rodzaj,
#                            self.dlugosc,
#                            self.szerokosc,
#                            self.rozmiar,
#                            self.kolor,
#                            self.dla_kogo) \
#
#
#
# Material1 = Material("Bawelna", "150", "122")
# Ubranie1 = Ubrania("Bawelna", "150cm", "122cm", "L", "Biały", "płci pięknej")
# Sweter1 = Sweter("Rozpinany", "Bawelna", "150cm", "122cm", "L", "Biały", "płci pięknej")
#
# print(Material1.wyswietlnazwe())
# print(Ubranie1.wyswietl_dane_ubrania())
# print(Sweter1.wyswietl_dane_swetra())

# Zad 2 ?????????????????????????


# class Kwadrat:
#     def __init__(self, x):
#         self.x = x
#
#     def __add__(self, y):
#         return self.x + (4 * self.x)
#
#
# kwadrat1 = Kwadrat(25)
# print(kwadrat1.__add__(5000))


# # Zad 3 ??????????????????????????????
#
# class Kwadrat:
#
#     def __init__(self, x):
#         self.x = x
#         self.y = x
#
#     def __ge__(self, other):
#         return self.x >= other.x
#
#     def __gt__(self, other):
#         return self.x > other.x
#
#     def __lt__(self, other):
#         return  self.x < other.x
#
#     def __le__(self, other):
#         return  self.x <= other.x
#
#
# kwadrat1 = Kwadrat(24)
# kwadrat2 = Kwadrat(21)
# print(kwadrat1.__ge__(kwadrat2))
# print(kwadrat2.__gt__(kwadrat1))
# print(kwadrat1.__le__(kwadrat2))
# print(kwadrat2.__lt__(kwadrat1))


# # Zad 4 ????????????????
#
# class Point:
#     counter = []
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def update(self, n):
#         self.counter.append(n)
#
#
# point1 = Point(5, 4)
# point2 = Point(6, 8)
#
# print(point1)
# print(point2)
#
# print(point1.counter)
# print(point2.counter)
#
# point1.update(10)
# print(point1.counter)
# print(point2.counter)
#

# # Zad 5
#
# class Osoba:
#     def __init__(self, imie, nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko
#
#     def przedstawsie(self):
#         return " Jestem {}  {}" .format(self.imie, self.nazwisko)
#
#
# class Pracownik:
#     def __init__(self, pensja):
#         self.pensja = pensja
#
#     def przedstawsie(self):
#         return " Jestem {}  {} i zarabiam  {}" .format(self.imie, self.nazwisko, self.pensja)
#
#
# class Menadzer(Osoba, Pracownik):
#     def __init__(self, imie, nazwisko, pensja):
#         Osoba.__init__(self, imie, nazwisko)
#         Pracownik.__init__(self, pensja)
#
#     def przedstawsie(self):
#         return " Jestem Menager {} {} i zarabiam {}" .format(self.imie, self.nazwisko, self.pensja)
#
#
# x = isinstance(Pracownik, Osoba)
# x2 = isinstance(Pracownik, Pracownik)
# x3 = isinstance(Pracownik, Menadzer)
# y = issubclass(Menadzer, Osoba)
# y2 = issubclass(Menadzer, Pracownik)
# y3 = issubclass(Menadzer, Menadzer)
# print(x)
# print(x2)
# print(x3)
# print(y)
# print(y2)
# print(y3)










# class Ksztalty:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def pole(self):
#         return self.x * self.y
#
#     def obwod(self):
#         return 2 * self.x + 2 * self.y
#
#
# class Kwadrat(Ksztalty):
#     def __init__(self, x):
#         self.x = x
#         self.y = x
#
#
# class KwadratCyfra8(Kwadrat):
#     def obwod(self):
#         return 6 * self.x
#
#     def pole(self):
#         return 2 * (self.x * self.x)
#
#
# ksztalt = Ksztalty(4, 5)
# kwadrat = Kwadrat(6)
# print(ksztalt.obwod())
# print(kwadrat.pole())
# print(kwadrat.obwod())
# figura8 = KwadratCyfra8(4)
# print("\n")
# print(figura8.pole())
# print(figura8.obwod())
#
#
# # WIELOKROTNE DZIEDZICZENIE KLASY :
#
#
# class Osoba:
#     def __init__(self, imie, nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko
#
#     def przedstawsie(self):
#         return " Jestem {}  {}" .format(self.imie, self.nazwisko)
#
#
# class Pracownik:
#     def __init__(self, pensja):
#         self.pensja = pensja
#
#     def przedstawsie(self):
#         return " Jestem {}  {} i zarabiam  {}" .format(self.imie, self.nazwisko, self.pensja)
#
#
# class Menadzer(Osoba, Pracownik):
#     def __init__(self, imie, nazwisko, pensja):
#         Osoba.__init__(self, imie, nazwisko)
#         Pracownik.__init__(self, pensja)
#
#     def przedstawsie(self):
#         return " Jestem Menager {} {} i zarabiam {}" .format(self.imie, self.nazwisko, self.pensja)
#
#
# Igorkox = Menadzer("Igor", "Kox", 495)
# print(Igorkox.przedstawsie())
#
# imie = "REKIN"
# it = iter(imie) # iteratory
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it)) # to juz jest bledne -- bo iterator sie skonczyl
#
#

# class Backwards:
#     """Iterator returning values in backward order"""
#
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]


