import numpy as np
import pandas as pd
import xlrd
import openpyxl

# 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

# 2.1
print(df[(df['Liczba'] < 1000)])
print('\n')     # LUB
print(df[(df.Liczba < 1000)])

# 2.2
print(df[(df['Imie'] == "IGOR")])
print('\n')     # LUB
print(df[(df.Imie == "IGOR")])

# 2.3
print('\n')
print(sum(df.Liczba))
print(np.sum(df.Liczba))

# 2.4
print(sum(df.Liczba[((df.Rok >= 2005) & (df.Rok <= 2010))]))

# 2.5
print(sum(df.Liczba[((df.Rok == 2000) & (df.Plec == 'M'))]))

# 2.6
# print(max(df.Liczba[((df.Rok == 2000) & (df.Plec == 'K'))]))
for x in range(2000, 2018, 1):
    print('Rok ' + str(x))
    print(df.Imie[df['Liczba'] == max(df.Liczba[((df.Rok == x) & (df.Plec == 'K'))])])
    print(df.Imie[df['Liczba'] == max(df.Liczba[((df.Rok == x) & (df.Plec == 'M'))])])


# 2.7
print('\n')
print(df.Imie[df.Liczba == max(df.Liczba[(df.Plec == 'K')])])
print(df.Imie[df.Liczba == max(df.Liczba[(df.Plec == 'M')])])

# 3.1
print('\n')
df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
print(pd.unique(df.Sprzedawca))

# 3.2
print('\n')
df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
a = df.Utarg.sort_values(ascending=False)
print(a[0:5])

# 3.3
print('\n')
print(pd.value_counts(df.Sprzedawca))

# 3.4
print('\n')
print(df.groupby('Kraj').Utarg.sum())
print(df.groupby(['Kraj']).agg({'Utarg': ['sum']}))

# 3.5
# df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
# df['year'] = pd.DatetimeIndex(df['Data zamowienia']).year
# print(df.groupby(df['Data zamowienia'].dt.year).agg({'Utarg': ['sum']}))
# print(df['year'])
# print(sum(df.Utarg[df['year'] == 2005]))
print('\n')
df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
start_date = pd.to_datetime('1/1/2005')
end_date = pd.to_datetime('12/31/2005')
print(sum(df.Utarg[(df['Data zamowienia'] >= start_date) & (df['Data zamowienia'] <= end_date) & (df['Kraj'] == 'Polska')]))

# 3.6
print('\n')
df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
start_date = pd.to_datetime('1/1/2004')
end_date = pd.to_datetime('12/31/2004')
print(np.average(df.Utarg[(df['Data zamowienia'] >= start_date) & (df['Data zamowienia'] <= end_date)]))

# 3.7
print('\n')
df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
start_date2004 = pd.to_datetime('1/1/2004')
end_date2004 = pd.to_datetime('12/31/2004')
start_date2005 = pd.to_datetime('1/1/2005')
end_date2005 = pd.to_datetime('12/31/2005')
df2004 = df.loc[(df['Data zamowienia'] >= start_date2004) & (df['Data zamowienia'] <= end_date2004)]
df2005 = df.loc[(df['Data zamowienia'] >= start_date2005) & (df['Data zamowienia'] <= end_date2005)]
print(df2004)
df2004.to_csv('zamowienia_2004.csv', sep=';')
print(df2005)
df2005.to_csv('zamowienia_2005.csv', sep=';')

# NOTATKI

# # SERIES (1-dim)
# seria = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(seria)
# seria = pd.Series([10, 12, 8, 14], index=['Ala', 'Kazik', 'Włodzimierz', 'Matylda'])
# print(seria)
#

# # DATA FRAMES (2-dim)
# data = {'Kraj': ['Belgia', 'Indie', 'Polska', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Warszawa', 'Brasilia'],
#         'Populacja': [11190846, 1403171035, 39678093, 207847528]}
# df = pd.DataFrame(data)
# print(data)
# print(df)
# # dataFrame zapisuje typ dla każdej kolumny, co widać poniżej ;
# print(df.dtypes)
#

# # MOZNA UTWORZYC OKRES CZASOWY POPRZEZ PODANIE DATY PIERWSZEJ I SKOKU
# daty = pd.date_range('20210422', periods=5)
# print(daty)
# # MOZNA UTWORZYC DATAFRAME DLA LOSOWYCH LICZB, indeksami są wcześniej wyinkrementowane daty a kolumny A B C D
# df = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))
# print(df)
#

# # Pandas umozliwia nam takze tworzenie DataFrame'ów na podstawie zewnętrznych danych ( CSV ) ;
# df = pd.read_csv('wyniki.csv', header=0, sep=';', decimal=',')
# print(df)
# df.to_csv('plik.csv', index=False)  # chcemy bez indeksow stworzyc nowy plik


# # TERAZ ZAPIS I ODCZYT NA XLSX ( PLIKI TYPU EXCEL )

# xlsx = pd.ExcelFile('wyniki.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
# df.to_excel('wyniki2.xlsx', sheet_name='Arkusz Pierwszy')


# # POBIERANIE POSZCZEGOLNYCH DANYCH ZE STRUKTUR, Z SERIES ALBO DATAFRAMES ITD //
# # POBIERANIE POSZCZEGOLNEGO ELEMENTU Z WIERSZA TUDZIEŻ KOLUMNY CZY INDEKSU ITD //
# # POBIERANIE POSZCZEGOLNEGO WIERSZA TUDZIEŻ KOLUMNY CZY INDEKSU CZY CZEGOKOLWIEK //
# seria = pd.Series([10, 12, 8, 14], index=['Ala', 'Kazik', 'Włodzimierz', 'Matylda'])
# print(seria)
# data = {'Kraj': ['Belgia', 'Indie', 'Polska', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Warszawa', 'Brasilia'],
#         'Populacja': [11190846, 1403171035, 39678093, 207847528]}
# df = pd.DataFrame(data)
# print(df)
# # SERIA : POJEDYNCZY ELEMENT - ODNOSIMY SIE DO INDKSU
# print(seria['Ala'])
# # MOZNA DO TEGO SIE DOSTAC TAKZE POPRZEZ ODWOLANIE DO OBIEKTU, BO NASZYMI INDEKSAMI SA OBIEKTY
# print(seria.Ala)
# # DATAFRAME : POJEDYNCZY ELEMENT - ODNOSIMY SIE JAK W TABLIACH POPRZEZ CIĘCIE - TUTAJ OD INDEKSU 0 do 1
# print(df[0:1])
# # CALA KOLUMNA (poprzez podanie nazwy etykiety)
# print(df['Populacja'])
# # WARTOSCI POPRZEZ PODANIE INDEKSU WIERSZA I INDEKSU KOLUMNY
# print(df.iloc[[0][0]])
# # WARTOSCI POPRZEZ PODANIE INDEKSU WIERSZA I ETYKIECIE KOLUMNY
# print(df.loc[[0], ["Kraj"]])
# print("\n")
# print(df.at[0, "Kraj"])
# # PODOBNIE JAK W SERIES - MOZNA ODWOLAC SIE DO OBIEKTU ZAMIAST PODAWAC CALA NAZWE W " "
# # DODATKOWO PRINT JEST WYWOLYWANY DLA KAZDEGO ELEMENTU DANEJ KOLUMNY ( PĘTLA )
# print('Kraj: ' + df.Kraj)
#
# # MOZNA TAKZE WYWOLAC FUNKCJE KTORA POBIERA LOSOWE ELEMENTY LUB ODNOSZACE SIE DO PROCENTOWEJ WIELKOSCI CALEGO ZBIORU
# # JEDEN LOSOWY ELEMENT :
# print(df.sample())
# # N-LOSOWYCH ELEMENTOW :
# print(df.sample(2))
# # ILOSC ELEMENTOW PROCENTOWO, UWAGA NA ZAOKRAGLENIE !!
# print(df.sample(frac=0.5))
# # MOZNA UZYC PARAMETRU REPLACE KTORY BEDZIE LOSOWAL Z POWTORZENIAMI JAK CHCEMY DUPLIKATY
# print(df.sample(n=10, replace=True))
# # ZAMIAST WYSWIETLAC CALA KOLEKCJE MOZNA WYSWIETLAC DANĄ ILOSC ELEMENTOW ( OD ZERA )
# print(df.head())
# print(df.head(1))
# print(df.head(2)) # head tzn te indeksy
# # MOZNA WYSWIETLIC TEZ STATYSTYKE DLA DANEJ KOLUMNY CZY WIERSZA O ILE SA NUMERYCZNE
# print(df.describe())
# # TRANSPOZYCJA KOLEKCJI
# print(df.T)
#
#
# # GRUPOWANIE - FILTROWANIE - AGREGOWANIE W PANDAS
# seria = pd.Series([10, 12, 8, 14], index=['Ala', 'Kazik', 'Włodzimierz', 'Matylda'])
# print(seria)
# data = {'Kraj': ['Belgia', 'Indie', 'Polska', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Warszawa', 'Brasilia'],
#         'Populacja': [11190846, 1403171035, 39678093, 207847528]}
# df = pd.DataFrame(data)
# print(df)
# # WYSWIETLA TYLKO DANE GDZIE WARTOSCI SA WIEKSZE NIZ 9
# print(seria[(seria > 9)])
# # MOZNA TEZ TO ZROBIC FUNKCJA WHERE,
# # KTORA ZWROCI KOLEKCJE W ORYGINALNEJ LICZEBNOSCI ELEMENTOW,
# # ALE ELEMENTY NIE SPELNIAJACE WARUNKU SA ZAPISYWANE JAKO NAN
# print(seria.where(seria > 10))
# # MOZNA TEZ PODSTAWIC WARTOSC KTORA BEDZIE ZAMIAST NAN ( DLA ELEMENTOW NIE SPELNIAJACYC?H WARUNKU )
# print(seria.where(seria > 10, 'Za Duze'))
# # WHERE POZWALA TEZ NA MODYFIKOWANIE KOLEKCJI ( DOMYSLNIE ZWRACANA JEST KOPIA )
# seria2 = seria.copy()
# seria2.where(seria2 > 10, 'Za Duze', inplace=True)
# print('########')
# print(seria2)
# # WYSWIETLA DANE Z SERII GDZIE WARTOSC NIE JEST WIEKSZA NIZ 10
# print(seria[~(seria > 10)])
# # WARUNKI MOZNA TEZ ŁACZYC
# print(seria[(seria < 13) & (seria > 8)])
# # WARUNKI DLA DATAFRAME TERAZ
# print(df[(df.Populacja > 100000000)])
# # SKOMPLIKOWANY PRZYKLAD TERAZ
# print(df[((df.Populacja > 100000000) & (df.index.isin([0, 2])))])
# # INNY PRZYKLAD Z ISIN ZWRACAJACA WARTOSCI BOOLOWSKIE // 0 --- 1
# print('########')
# szukaj = ['Belgia', 'Brasilia']
# print(df.isin(szukaj))
#
#
# # ZMIANA, USUWANIE, DODAWANIE DANYCH
# # W SERII MOZNA SIE ODWOLAC DO ELEMENTU PODAJAC KLUCZ(indeks)
# seria['Ala'] = 15
# seria['Alan'] = 21  # mozna dodawac nawet elementy
# print(seria)
# # W DATAFRAME POWYZSZA OPERACJA ZADZIALA INACZEJ
# df.loc[3] = 'dodane'
# print(df)
# # MOZNA DODAC WIERSZ W POSTACI LISTY
# df.loc[4] = ['Poland', 'Warsaw', 38675431]
# print(df)
# # USUWAMY DANE POPRZEZ FUNCKJE DROP, KTORA JEDNAK TWORZY KOPIE NASZEGO DATAFRAME Z USUNIETYMI WARTOSCIAMI
# new_df = df.drop([3])
# print(new_df)
# # JESLI JEDNAK CHCEMY ZMIENIC PIERWOTNA KOLEKCJE A NIE ROBIC KOPIE, TO :
# df.drop([3], inplace=True)
# print(df)
# # MOZNA ROWNIEZ USUWAC CALE KOLUMNY PO INDEKSIE, ALE WTEDY NIE MOZEMY NIC DALEJ ZROBIC, TAK TO WYGLADA :
# # df.drop('Kraj', axis=1, inplace=True)
#
# # DO DATAFRAME MOZEMY ROWNIEZ DODAWAC KOLUMNY ZAMIAST WIERSZY
# df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Pn', 'Ameryka Pd']
# print(df)
#
#
# # PANDAS MA FUNKCJE SORTOWANIA
# print(df.sort_values(by='Kraj')) # alfabetycznie
#
# # PANDAS MA FUNKCJE GRUPOWANIA
# grouped = df.groupby(['Kontynent'])
# print(grouped.get_group('Europa'))
# # MOZNA TEZ JAK W SQLU WYKONAC FUNKCJE AGREGUJACE NA DANEJ KOLUMNIE
# print(df.groupby(['Kontynent']).agg({'Populacja': ['sum']}))
#
#
# # MAMY TEZ SUMY CZESCIOWE ZNANE Z EXCELA I TABELE PRZESTAWNE
# print("____sumy częsciowe ____")
# tabela = pd.pivot_table(df, values=['Populacja'], index=['Kontynent'], columns=['Kraj'], aggfunc=np.sum, margins=True)
# print(tabela.stack('Kraj'))
