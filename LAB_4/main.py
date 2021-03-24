import random
import sys

# # ZAD 1
# plik = open('zadanie1.txt', 'w+')
#
#                                                   # TRYB W KASUJE POPRZEDNI ZAPIS I WSTAWIA NOWY --
#                                 # TRYB A NIE MOZNA UZYC PRINT I NIE KASUJE POPRZEDNIEGO ZAPISU TYLKO DODAJE KOLEJNY --
# for x in range(10):                                    # TRYB R to samo co A
#     x = random.randint(0, 30)
#     x = x * 2
#     plik.writelines(str(x))
#     plik.writelines('\n')
#
# print(plik.readlines())        # ???

# # ZAD 2
#
# plik = open('zadanie1.txt', 'r+')
# print(plik.readlines())       # teraz dziala przy trybie otwarcia r+


# # ZAD 3
#
# with open('zadanie3.txt', 'w+') as plik2:
#     for x in range(10):
#         dane = input()
#         plik2.write(dane)
#         plik2.write('\n')
#
# plik2 = open('zadanie3.txt', 'r')
# print(plik2.readlines())

# # ZAD 4

# class NaZakupy:
#
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#
#     def wyswietl(self):
#         print(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed)
#
#     def ile_produktu(self):
#         print(self.ilosc + self.jednostka_miary)
#
#     def ile_kosztuje(self):
#         return int(self.cena_jed) * int(self.ilosc)
#
#
# nr1 = NaZakupy('Domestos', '5', 'L', '150')
# nr2 = NaZakupy('Lody Ekipa', '2000', 'szt', '3')
# print(nr1.wyswietl())
# print(nr1.ile_produktu())
# print(nr1.ile_kosztuje())
# print(nr2.wyswietl())
# print(nr2.ile_produktu())
# print(nr2.ile_kosztuje())

# ZAD 5


# class CiagArytmetyczny:
#
#     a1 = 0
#     n = 0
#     r = 0
#     an = 0
#     liczba_elementow = 0
#
#     def wyswietl_dane(self):  # wyswietla dane ciągu
#         print('Wyraz pierwszy :', self.a1,
#               'Liczba wyrazów :', self.n,
#               'Reszta :', self.r)
#
#     def n_wyraz(self):  # liczy n-ty wyraz ciągu
#         self.an = self.a1 + (self.n - 1) * self.r
#         return self.an
#
#     def pobierz_parametry(self): # pobiera parametry ciągu
#         self.a1 = float(input("Pierwszy element ciągu:"))
#         self.n = float(input("Liczba elementów ciągu:"))
#         self.r = float(input("Różnica ciągu:"))
#
#     def policz_sume(self):  # liczy sume ciągu
#         suma = (self.a1 + self.an) / 2 * self.n
#         return suma
#
#     def policz_elementy(self):
#         self.liczba_elementow = ((self.an - self.a1) / self.r) + 1
#         return self.liczba_elementow
#
#
# ciag1 = CiagArytmetyczny()
# ciag1.pobierz_parametry()
# wyraz_n_ciagu = ciag1.n_wyraz()
# print('Wyraz n-ty tego ciągu to:',wyraz_n_ciagu)
# suma_ciagu = ciag1.policz_sume()
# print('Suma tego ciągu to:', suma_ciagu)
# liczba_elementow_ciagu = ciag1.policz_elementy()
# print('Liczba elementów tego ciągu to:', liczba_elementow_ciagu)

# # ZAD 5 II SPOSÓB

# class CiagArytmetyczny:
#
#     an = 0
#     liczba_elementow = 0
#
#     def __init__(self, a1, n, r):  # pobiera elementy ciągu od użytkownika //pobierz_elementy, pobierz_parametry
#         self.a1 = a1
#         self.n = n
#         self.r = r
#
#     def wyswietl_dane(self):  # wyswietla dane ciągu
#         print('Wyraz pierwszy :', self.a1,
#               'Liczba wyrazów :', self.n,
#               'Reszta :', self.r)
#
#     def n_wyraz(self):  # liczy n-ty wyraz ciągu
#         self.an = self.a1 + (self.n - 1) * self.r
#         return self.an
#
#     def policz_sume(self):  # liczy sume ciągu
#         suma = (self.a1 + self.an) / 2 * self.n
#         return suma
#
#     def policz_elementy(self):
#         self.liczba_elementow = ((self.an - self.a1) / self.r) + 1
#         return self.liczba_elementow

#
# ciag1 = CiagArytmetyczny(1, 10, 5)
# print(ciag1.wyswietl_dane())
# wyrazn1 = ciag1.n_wyraz()
# print(wyrazn1)
# suma1 = ciag1.policz_sume()
# print(suma1)
# liczba_elementow_ciagu1 = ciag1.policz_elementy()
# print(liczba_elementow_ciagu1)
#
# ciag2 = CiagArytmetyczny(25, 26, 3)
# print(ciag2.wyswietl_dane())
# wyrazn2 = ciag2.n_wyraz()
# print(wyrazn2)
# suma2 = ciag2.policz_sume()
# print(suma2)
# liczba_elementow_ciagu2 = ciag2.policz_elementy()
# print(liczba_elementow_ciagu2)


# # ZAD 6

# class Robaczek:
#
#     def __init__(self, x, y, krok):
#         self.x = x
#         self.y = y
#         self.krok = krok
#
#     def idz_w_gore(self, ile_krokow):
#         self.y = self.y + (ile_krokow * self.krok)
#
#     def idz_w_dol(self, ile_krokow):
#         self.y = self.y - (ile_krokow * self.krok)
#
#     def idz_w_prawo(self, ile_krokow):
#         self.x = self.x + (ile_krokow * self.krok)
#
#     def idz_w_lewo(self, ile_krokow):
#         self.x = self.x - (ile_krokow * self.krok)
#
#     def pokaz_gdzie_jestes(self):
#         return self.x, self.y
#
#
# robaczek1 = Robaczek(0, 0, 1)
# robaczek1.idz_w_gore(5)
# robaczek1.idz_w_dol(7)
# robaczek1.idz_w_prawo(3)
# robaczek1.idz_w_lewo(6)
# pokaz = robaczek1.pokaz_gdzie_jestes()
# print(pokaz)


# # OPERACJE NA PLIKACH - PODSTAWY
# plik = open('gzibi.txt', 'r')
#
# znaki = plik.read(8)
#
# wers = plik.readline()
#
# wszystkiewiersze = plik.readlines()
#
# print(wszystkiewiersze)
# print(wers)
# print(znaki)
#
# plik.close()
#
# # po zamknieciu juz pliku
#
# print(znaki)
# print('\n')
# print(wers)
# print('\n')
# print(wszystkiewiersze)
# print('\n')

# # DODANIE DO PLIKU

# import sys

# plik = open('gzibi.txt', 'r+')
# print("Podaj kierunek i specjalizacje studiow")
# dane = sys.stdin.readline()
# dane2 = input()
# plik.write(dane)
# plik.write(dane2)
# print(plik.readlines())
#
# plik.close()
#
# list = []
# for x in range(10):
#     list = list + [x]
#
# print(list)
#
# plik = open('gzibi.txt', 'r+')
# plik.writelines(str(list))
# print(plik.readlines())
# plik.close()
#
# # DODATKOWA OPCJA

# with open('gzibi.txt', 'r+') as plik:  # w takiej konstrukcji plik sam wykona na koncu funkcje .close() wiec nie trzeba sie martwic
#     for linia in plik:
#         print(linia, end='')


# # # PROGRAMOWANIE OBIEKTOWE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#
# class Klasa:
#     'Pierwsza klasa w Pythonie'
#     atrybut = 2001
#     def pierwsza_metoda(self):
#         return 'Tutaj dziala pierwsza metoda, tzn funkcja'
#
#
# obiekt = Klasa()
# print(obiekt)
# print(obiekt.atrybut)
# print(obiekt.pierwsza_metoda())
# obiekt.tekst = 'ha ha ha'
# print(obiekt.tekst)
# print(obiekt)
# nowy_obiekt = Klasa()
# print(nowy_obiekt)
#
#
# class Ksztalt:
#
#     def __init__(self, x, y):  # self oznacza ze chodzi o zmienne tej klasy  # __ __ oznaczaja, ze to jest tylko zarezerwowane dla tej klasy
#         self.x = x
#         self.y = y
#         self.opis = 'To będzie klasa dla ogólnych ksztaltow'
#
#     def pole(self):
#         return self.x * self.y
#
#     def obwod(self):
#         return 2 * self.x + 2 * self.y
#
#     def dodajopis(self, text):
#         self.opis = text
#
#     def skalowanie(self, czynnik):
#         self.x = self.x * czynnik
#         self.y = self.y * czynnik
#
#
# kwadrat = Ksztalt(10, 30)
# print(kwadrat.pole())
# print(kwadrat.obwod())
#
# kwadrat.dodajopis("Kwadrat")
# print(kwadrat.opis)
# kwadrat.skalowanie(0.5)
# print(kwadrat.x)
# print(kwadrat.y)
