import pandas as pd
import matplotlib.pyplot as plt

# 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

df['Rok'] = df['Rok'].astype(str)
grupa = df.groupby(['Rok']).agg({'Liczba': ['sum']})
wykres = grupa.plot()
wykres.set_ylabel("Liczba urodzeń")
wykres.set_xlabel("Rok")
wykres.legend()
plt.title("Liczba urodzonych dzieci w poszczególnych latach")
plt.show()

# 2
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

grupa2 = df.groupby(['Plec']).agg({'Liczba': ['sum']})
wykres2 = grupa2.plot.bar()
wykres2.set_ylabel("Liczba urodzeń")
wykres2.set_xlabel("Płeć")
wykres2.legend()
plt.title("Liczba urodzonych dzieci ze względu na płeć")
plt.xticks(rotation=0)
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.show()

# 3
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
df = df[(df['Rok'] >= 2013) & (df['Rok'] <= 2017)]
print(df)
grupa3 = df.groupby(['Plec']).agg({'Liczba': ['sum']})
wykres3 = grupa3.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6), legend=(0, 0))
plt.legend(loc="lower right")
plt.title("Stosunek urodzeń ze względu na płeć ( Ostatnie 5 lat )")
plt.show()

# 4
df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal=',')
grupa4 = df.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']})
wykres4 = grupa4.plot.bar()
wykres4.set_ylabel("Ilość zamówień")
wykres4.set_xlabel("Sprzedawcy")
wykres4.legend()
plt.title("Ilość zamówień na poszczególną firmę")
plt.xticks(rotation=0)
plt.show()


# # NOTATKI
#
# # szereg czasowy danych, random + data_range
# ts = pd.Series(np.random.randn(2300), index=pd.date_range('1/1/2015', periods=2300))
# print(ts)
#
# # funkcja generujaca suma kolejnych elementow - wykres
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()
#
# # Wykres kolumnowy
#
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Pd', 'Europa'],
#         'Populacja': [11904265, 1246950324, 267695324, 37124245]}
# df = pd.DataFrame(data)
# print(df)
#
# grupa = df.groupby(['Kontynent']).agg({'Populacja': ['sum']})
# print(grupa)
# wykres = grupa.plot.bar()
# wykres.set_ylabel("Mld")
# wykres.set_xlabel("Kontynent")
# wykres.legend()
# plt.title("Populacja z podzialem na kontynenty")
# # zmiana kierunku tekstu etykiet słupkow
# plt.xticks(rotation=0)
# plt.savefig('wykres.png')
# plt.show()
#
# # wczytanie danych z plikow i wyswietlenie zgrupowanych rzeczy
# df = pd.read_csv('dane.csv', header=0, sep=";", decimal=".")
# print(df)
# grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia': ['sum']})
# # wykres kolowy z wartosciami procentowymi sformatowanymi z dokladoscia do 2 miejsc po przecinku
# # figsize ustawia wielkosc wykresu w calach, domyslnie 6,4 i 4,8
# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6), legend=(0, 0))
# plt.legend(loc="lower right")
# plt.title('Suma zamowienia dla przedawcy')
# plt.show()
#
# # wykres sredniej kroczacej
# ts = pd.Series(np.random.randn(2300), index=pd.date_range('1/1/2015', periods=2300))
# print(ts)
#
# ts = ts.cumsum()
# df = pd.DataFrame(ts)
# # dodanie nowej kolumny i wykorzystanie funkcji rolling do stworzenia kolejnych wartosci sredniej kroczacej
# df['MA'] = df.rolling(window=50).mean()
# df.plot()
# plt.show()
