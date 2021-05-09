import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# # ZAD 1
# x = np.arange(1, 20)
# plt.plot(x, 1/x, label="1/x")
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
# plt.title('WYKRES ZADANIE 1')
# plt.axis([0, 1, 1, 20])  # ?
# plt.show()
#
# # ZAD 2
# plt.plot(x, 1/x, 'g>:', label="1/x")
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
# plt.title('WYKRES ZADANIE 1')
# plt.axis([1, 20, 0, 1]) # mod
# plt.show()

# # ZAD 3
# x = np.arange(0, 30, 0.1)
# plt.plot(x, np.sin(x), 'r', label="sin(x)")
# plt.plot(x, np.cos(x), 'violet', label="cos(x)")
# plt.xlabel('x')
# plt.ylabel('six(x)')
# plt.title('Wykres zadanie 3')
# plt.legend()
# plt.show()
#
# # ZAD 4
# x = np.arange(0, 30, 0.1)
# plt.plot(x, 2+np.sin(x), 'blue', label="sin(x)")
# plt.plot(x, np.sin(-x), 'orange', label="sin(x)")
# plt.xlabel('x')
# plt.ylabel('six(x)')
# plt.title('Wykres sin(x), sin(x)')
# plt.legend()
# plt.show()

# # ZAD 5
# dane = pd.read_csv("iris.csv", )
# datafrejm = pd.DataFrame(dane)
#
# plt.scatter('sepal_length', 'sepal_width', c='c', s=abs(datafrejm['sepal_length'] - datafrejm['sepal_width']), data=datafrejm)
# plt.xlabel('sepal_length')
# plt.ylabel('sepal_width')
# plt.show()

# # ZAD 6
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# df['Rok'] = df['Rok'].astype(str)  # konwersja, aby na wykresie data zostala odpowiednio odczytana
# df_mezczyzni = df[(df['Plec'] == 'M')]
# df_kobiety = df[(df['Plec'] == 'K')]
#
# x1 = df['Plec']
# x2_kobiety = df_kobiety['Rok']
# x2_mezczyzni = df_mezczyzni['Rok']
# x3 = df['Rok']
#
# y1 = df['Liczba']
# y2_kobiety = df_kobiety['Liczba']
# y2_mezczyzni = df_mezczyzni['Liczba']
# y3 = df['Liczba']
#
# plt.subplot(1, 3, 1)
# plt.bar(x1, y1)
# plt.title('wykres 1')
# plt.ylabel('liczba urodzen')
# plt.xlabel('plec')
#
# plt.subplot(1, 3, 2)
# plt.plot(x2_kobiety, y2_kobiety, 'r', x2_mezczyzni, y2_mezczyzni, 'b')
# plt.title('wykres 2')
# plt.ylabel('liczba urodzen kobiet i mezczyzn na poszczegolny rok')
# plt.xlabel('rok')
#
# plt.subplot(1, 3, 3)
# plt.plot(x3, y3, 'green')
# plt.title('wykres 3')
# plt.ylabel('liczba urodzen na kazdy rok')
# plt.xlabel('rok')
#
# plt.show()

# # ZAD 7
# df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal=',')
# grouped_df = df.groupby(['Sprzedawca'])
# grouped_df = df.groupby(['Sprzedawca']).agg({'idZamowienia': "nunique"})
# grouped_df = grouped_df.reset_index()
# print(grouped_df)
# sprzedawcy = grouped_df['Sprzedawca']
# zamowienia = grouped_df['idZamowienia']
# explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0) # explode musi miec wymiar identyczny jak wektor X
# wedges, texts, autotexts = plt.pie(zamowienia, labels=sprzedawcy, autopct=lambda pct: # zastosowany cień oraz explode
#                                    "{:.1f}%".format(pct), shadow=True, explode=explode, textprops=dict(color="black"))
# plt.setp(autotexts, size=11, weight="bold")
# plt.title("SUMA ZAMOWIEN NA POSZCZEGOLNA FIRME")
# plt.show()

# # NOTATKI
#
# # Dokumentacja MATplotLIB : matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
#
# # 1WSZY WYKRES
# plt.plot([4, 5, 6, 2, 3, 4])  # podajemy tylko jeden wektor - będą to wartości osi Y, osią X będą natomiast indeksy
# plt.ylabel("Losowe Liczby")
# plt.xlabel("oś X")
# plt.show()
#
# # 2GI WYKRES
# #            X          Y        styl
# plt.plot([0, 1, 2], [1, 4, 16], '-ro')  # teraz podajemy natomiast dwa wektory - jeden jako oś X, drugi to oś Y + styl
# plt.ylabel("f(x) = 4^x")
# plt.xlabel("oś X")
# #     [xmin, xmax, ymin, ymax]
# plt.axis([0, 10, 0, 20]) # tu mozemy okreslic dziedzine wykresu, jak wielki zostanie narysowany
# plt.show()
#
# # 3CI WYKRES - DWUKOLOROWY ( nalezy nalozyc na siebie dwa wykresy )
# plt.plot([0, 1, 2], [1, 4, 16], 'ro')
# plt.plot([0, 1, 2], [1, 4, 16], 'b')
# plt.show()
#
# # 4TY WYKRES - wiele wykresow na jednym rysunku ( płótnie - canvas'ang' ) - WSZYSTKO MOZNA W JEDNYM PLOT (    ) ZROBIC
# t = np.arange(0., 5., 0.2)  # floats
# plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t**3, 'g^')  # wiele wykresow,kazdy inny styl,kazdy x=t, f(x) = inna funkcja
# plt.show()  # T^2 nie działa, musi być T ** 2
#
# # 5TY WYKRES - ZAMIAST WSZYSTKO PODAWAC W JEDNYM PLOCIE, MOZNA DEFINIOWAC WYKRESY JEDEN PO DRUGIM
# x = np.linspace(0, 2, 100)
# plt.plot(x, x, label="liniowa")
# plt.plot(x, x ** 2, label="kwadratowa")
# plt.plot(x, x ** 3, label="szescienna")
# plt.xlabel('X')
# plt.ylabel('F(X)')
# # tytul
# plt.title("3 różne wykresy na jednej kanwie")
# # legenda ( stąd potrzebne było label="liniowa, kwadratowa, szescienna" )
# plt.legend()
# plt.show()

# # 6TY WYKRES - TRYGONOMETRYCZNY
# x = np.arange(0, 12, 0.1)
# plt.plot(x, np.sin(x), 'r', label="sin(x)")
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Wykres sin (x)')
# plt.legend()
# plt.show()
#
# # 7DMY WYKRES - NA PODSTAWIE SLOWNIKA ALBO DATAFRAME
# dane = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# dane['b'] = dane['a'] + 10 * np.random.randn(50)
# dane['d'] = np.abs(dane['d']) * 100  # wartosc bezwzgledna z losowych liczb, aby nie otrzymac ujemnych wartosci
# datafrejm = pd.DataFrame(dane)
# # teraz nalezy przekazacv nasze dane jako parametry wykresu, 'a' = datafrejm['a'] itd
# print(f"a={datafrejm['a'][0]}, b={datafrejm['b'][0]}, c={datafrejm['c'][0]}, d={datafrejm['d'][0]}")
# plt.scatter('a', 'b', c='c', s='d', data=datafrejm)  # c = color, parametr koloru, s = scale, rozmiar pkt dla wartosci
# plt.xlabel('wartosc a')
# plt.ylabel('wartosc b')
# plt.show()

# PODWYKRESY
# pozwalaja na umieszczenie na jednej kanwie wielu wykresow zoorganizowanych na gridzie
# podajemy wymiary gridu - liczba wierszy i liczba kolumn
# FUNKCJA SUBPLOT - 3 argumenty (nrows, ncols, index), ilosc wierszy, ilosc kolumn, indeks definiowanego wykresu
# (start od 1 i koniec na nrows*ncols)

# # 1WSZY PODWYKRES
# x1 = np.arange(0., 2., 0.02)
# x2 = np.arange(0., 2., 0.02)
#
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
#
# # tu grid 2x1 (2wiersze 1kolumny) - tzn tyle podwykresów moze byc na kanwie - definiujemy wykres o indeksie 1
# plt.subplot(2, 1, 1)
# plt.plot(x1, y1, '-')
# plt.title('Dwa podwykresy')
# plt.ylabel('sin(x)')
# plt.xlabel('x')
# # teraz definiujemy wykres o indeksie 2
# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, 'r', '-')
# plt.ylabel('cos(x)')
# plt.xlabel('x')
#
# plt.show()
#
# # 2GI PODWYKRES
# x1 = np.arange(0., 2., 0.02)
# x2 = np.arange(0., 2., 0.02)
#
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
# # teraz 3x2 GRID
# plt.subplot(3, 2, 1)
# plt.plot(x1, y1, 'g', '-')
# plt.title('Dwa podwykresy')
# plt.ylabel('sin(x)')
# plt.xlabel('x')
# # teraz definiujemy wykres o indeksie 2
# plt.subplot(3, 2, 2)
# plt.plot(x2, y2, 'brown', '-')
# plt.ylabel('cos(x)')
# plt.xlabel('x')
#
# plt.show()
#
# # 3CI PODWYKRES - JAK 2GI, ALE DRUGI WYKRES MA INDEKS 4 - TZN POMINELISMY 2,3
# x1 = np.arange(0., 2., 0.02)
# x2 = np.arange(0., 2., 0.02)
#
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
# # teraz 3x2 GRID
# plt.subplot(3, 2, 1)
# plt.plot(x1, y1, 'violet', '-')
# plt.title('Dwa podwykresy')
# plt.ylabel('sin(x)')
# plt.xlabel('x')
# # teraz definiujemy wykres o indeksie 2
# plt.subplot(3, 2, 4)
# plt.plot(x2, y2, 'red', '-')
# plt.ylabel('cos(x)')
# plt.xlabel('x')
#
# plt.show()
#
# # WYKRES SLUPKOWY
# etykiety = ['Kobiety', 'Mezczyzni']
# wartosci = [44, 43]
# # rozmiar wykresu = plt.figure(figsize=(8,10))
# plt.bar(etykiety, wartosci)
# # mozna zmienic kierunek tekstu etykiet (obrót) - plt.xticks(rotation=45)
# plt.ylabel('Srednie IQ')
# plt.xlabel('Plec')
# plt.title('Srednia iq ze wzgled na plec')
#
# plt.show()

# # HISTOGRAM
# x = np.random.randn(10000)
# # bins oznacza ilosc slupkow, do ktorych maja wpadac wartosci z wektora x
# # facekolor = kolor slupkow
# # alpha = stopien przezroczystoci calego wykresu
# # density = czy suma ilosci zostanie znormalizowana do rozkladu prawdopodobnienstwa ( przedzial 0 , 1 )
# plt.hist(x, bins=50, facecolor='green', alpha=0.75, density=True)
# plt.xlabel('Wartosci')
# plt.ylabel('Prawdopodobienstwo')
# plt.title('Histogram : )')
# plt.grid()  # siatka
# plt.show()
#
# # WYKRES KOLOWY
# zawodnicy = ['Benzema', 'CR7', 'Modric', 'Ramos']
# bramki = [23, 64, 7, 3]
# # 1wsza wersja wykresu kolowego
# wedges, texts, autotexts = plt.pie(bramki, labels=zawodnicy, autopct=lambda pct:
#                                    "{:.1f}%".format(pct), textprops=dict(color="black"))  # kolor tekstu = czarny
# plt.setp(autotexts, size=14, weight="bold")
# plt.title("PIERWSZA WERSJA WYKRESU KOLOWEGO")
# plt.legend(title='Zawodnicy')
#
# plt.show()
#
# # 2ga wersja wykresu kolowego
#
#
# def prepare_label(pct, br):
#     absolute = int(np.ceil(pct/100.*np.sum(br)))
#     return "{:.1f}% \n ({}/{})".format(pct, absolute, sum(bramki))
#
#
# wedges2, texts2, autotexts2 = plt.pie(bramki, labels=zawodnicy, autopct=lambda pct:
#                                    prepare_label(pct, bramki), textprops=dict(color="black"),
#                                    radius=1.2, labeldistance=1.02, startangle=70)
# plt.setp(autotexts, size=14, weight="bold")
# plt.title("DRUGA WERSJA WYKRESU KOLOWEGO")
# plt.legend(title='Zawodnicy', loc='lower left', bbox_to_anchor=(-0.2, -0.1))
#
# plt.show()

