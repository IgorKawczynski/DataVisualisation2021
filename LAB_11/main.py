import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data
from itertools import cycle
from cycler import cycler


# # Zad 1
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# t = np.linspace(0, 2 * np.pi, 100)
# z = t
# x = np.sin(t)
# y = 2 * np.cos(t)
#
# ax.plot(x, y, z, label='zadanie 1')
# ax.legend()
#
# plt.show()

# # Zad 2
# np.random.seed(19680801)  # ustawiamy sobie domyślny seed
#
#
# def randrange(n, vmin, vmax):
#     '''
#     Funkcja tworzy macierz losowych liczb o kształcie (n, )
#     '''
#     return (vmax - vmin) * np.random.rand(n) + vmin
#
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')  # utworzenie subplotu dla kilkunastu wykresów
#
# # utworzenie losowych kolorów
# colour = cycle('bgrycmk')
# # utworzenie losowych markerów
# markers = cycle(['o', '+', 'x', '*', '.', 'X', 'D', 'p', '|'])
# # utworzenie danych
# n = 15
# x1 = randrange(n, 23, 32)
# y1 = randrange(n, 16, 100)
# z1 = randrange(n, 44, 55)
# x2 = randrange(n, 60, 70)
# y2 = randrange(n, 24, 28)
# z2 = randrange(n, 77, 99)
# x3 = randrange(n, 24, 27)
# y3 = randrange(n, 51, 64)
# z3 = randrange(n, 22, 46)
# x4 = randrange(n, 67, 7)
# y4 = randrange(n, 41, 59)
# z4 = randrange(n, 96, 109)
# x5 = randrange(n, 101, 151)
# y5 = randrange(n, 94, 106)
# z5 = randrange(n, 19, 41)
#
# ax.scatter(x1, y1, z1, c=next(colour), marker=next(markers), label='first')
# ax.scatter(x2, y2, z2, c=next(colour), marker=next(markers), label='second')
# ax.scatter(x3, y3, z3, c=next(colour), marker=next(markers), label='third')
# ax.scatter(x4, y4, z4, c=next(colour), marker=next(markers), label='four')
# ax.scatter(x5, y5, z5, c=next(colour), marker=next(markers), label='five')
#
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
#
# plt.title('Zadanie 2')
# plt.legend(loc='upper right')
# plt.show()

# # Zad 3
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# # rysowanie powierzchni
# surface = ax.plot_surface(X, Y, Z, cmap=plt.get_cmap(), linewidth=0, antialiased=True)
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# # dodanie paska kolrów
# fig.colorbar(surface, shrink=1, aspect=5)
#
# plt.show()

# # Zad 4
# fig = plt.figure(figsize=(12, 10))
# ax1 = fig.add_subplot(1, 5, 1, projection='3d')
# ax2 = fig.add_subplot(1, 5, 2, projection='3d')
# ax3 = fig.add_subplot(1, 5, 3, projection='3d')
# ax4 = fig.add_subplot(1, 5, 4, projection='3d')
# ax5 = fig.add_subplot(1, 5, 5, projection='3d')
# _x = np.arange(4)
# _y = np.arange(5)
# _xx, _yy = np.meshgrid(_x, _y)
# x, y = _xx.ravel(), _yy.ravel()
# top = x + y
# bottom = np.zeros_like(top)
# width = depth = 1
# ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
# ax1.set_title('Wykres niebieski zacieniony')
# ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
# ax2.set_title('Wykres niebieski bez zacienienia')
# ax3.bar3d(x, y, bottom, width, depth, top, color='r', shade=True)
# ax3.set_title('Wykres czerwony zacieniony')
# ax4.bar3d(x, y, bottom, width, depth, top, color='r', shade=False)
# ax4.set_title('Wykres czarwony bez zacienienia')
# ax5.bar3d(x, y, bottom, width, depth, top, color='green', shade=True)
# ax5.set_title('Wykres zielony zacieniony')
#
# plt.show()

# # Zad 5
# fig = plt.figure(figsize=(12, 10))
# ax1 = fig.add_subplot(1, 2, 1, projection='3d')
# ax2 = fig.add_subplot(1, 2, 2, projection='3d')
# # dane wykres nr.1
# X1 = np.arange(-5, 5, 0.25)
# Y1 = np.arange(-5, 5, 0.25)
# X1, Y1 = np.meshgrid(X1, Y1)
# R1 = np.sqrt(X1**2 + Y1**2)
# Z1 = np.sin(R1)
# # dane wykres nr.2
# X2 = np.arange(-5, 5, 0.1)
# Y2 = np.arange(-5, 5, 0.1)
# X2, Y2 = np.meshgrid(X2, Y2)
# R2 = np.sqrt(X2**2 + Y2**2)
# Z2 = np.sin(R2)
# # rysuj powierzchnie
# surface = ax1.plot_surface(X1, Y1, Z1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# ax1.set_zlim(-1.01, 1.01)
# ax1.zaxis.set_major_locator(LinearLocator(10))
# ax1.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# ax1.set_title('Wykres nr.1')
# surface2 = ax2.plot_surface(X2, Y2, Z2, cmap=cm.coolwarm, linewidth=0, antialiased=True)
# ax2.set_zlim(-1.01, 1.01)
# ax2.zaxis.set_major_locator(LinearLocator(10))
# ax2.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# ax2.set_title('Wykres nr.2')
# # dodanie paska kolrów
# fig.colorbar(surface, shrink=0.5, aspect=5)
# plt.show()

# # # # # NOTATKI

# # wykres liniowy 3D
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# t = np.linspace(0, 2 * np.pi, 100)
# z = t
# x = np.sin(t) * np.cos(t)
# y = np.tan(t)
#
# ax.plot(x, y, z, label='zadanie 1')
# ax.legend()
# plt.show()
#
# # wykres punktowy 3D
# np.random.seed(19680801)  # ustawiamy sobie domyślny seed
#
# def randrange(n, vmin, vmax):
#     '''
#     Funkcja wspomagajaca może tworzyć macierz losowych liczb o kształcie (n, )
#     '''
#     return (vmax - vmin) * np.random.rand(n) + vmin
#
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# n = 100
# # dla kazdego zbioru styli oraz zakresow wygeneruje n losowych punktow
# # zdefiniowane przez x   z   [23, 32],  y     z [0, 100],    z     z [zlow, zhigh].
#
# for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)
#
#
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
#
# plt.title('Zadanie 2')
# plt.show()
#
# # wykres powierzchniowy
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# # generuj dane
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# # rysuj powierzchnie
# surface = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=True)
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# # dodanie paska kolrów
# fig.colorbar(surface, shrink=0.5, aspect=5)
#
# plt.show()
#
# # konfiguracja wielkosci wykresu, figsize okresla wielkosc wykresu w calach
# fig = plt.figure(figsize=(8, 3))
# ax1 = fig.add_subplot(1, 2, 1, projection='3d')
# ax2 = fig.add_subplot(1, 2, 2, projection='3d')
# # fikcyjne dane :
# _x = np.arange(4)
# _y = np.arange(5)
# _xx, _yy = np.meshgrid(_x, _y)
# x, y = _xx.ravel(), _yy.ravel()
# top = x + y
# bottom = np.zeros_like(top)
# width = depth = 1
# ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
# ax1.set_title('Wykres zacieniony')
# ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
# ax2.set_title('Wykres bez zacienienia')
#
# plt.show()
#
# # wiele wykresow w jednym wwwolaniu
#
# # szerokosc 2x wieksza niz wysokosc
# fig = plt.figure(figsize=plt.figaspect(0.5))
#
# # Pierwszy wykres
# ax = fig.add_subplot(1, 2, 1, projection='3d')
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# surface = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=1, antialiased=True)
# ax.set_zlim(-1.01, 1.01)
# fig.colorbar(surface, shrink=0.5, aspect=10)
#
# # Drugi wykres
# ax = fig.add_subplot(1, 2, 2, projection='3d')
# X, Y, Z = get_test_data()
# ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
#
# plt.show()
#
#
# # Wiele typow wykresow w jednej przestrzeni
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# x = np.linspace(0, 1, 100)
# y = np.sin(x * 2 * np.pi) / 2 + 0.5
# ax.plot(x, y, zs=0, zdir='z', label='curve in (x, y)')
# colors = ('r', 'g', 'b', 'k')
# np.random.seed(19680801)
# x = np.random.sample(20 * len(colors))
# y = np.random.sample(20 * len(colors))
# c_list = []
# for c in colors:
#     c_list.extend([c] * 20)
#
# # przez uzycie zdir='y', wartosc y dla tych punktow jest rowne zs czyli 0,  punkty (x, y) są nakładane na osiach x i z
# ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='points in (x,z)')
#
# # limity dla legendy
# ax.legend()
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# ax.set_zlim(0, 1)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# # ustawienie kąta nachylania przy generowaniu wykresu,    oś y=0
# ax.view_init(elev=20., azim=-35)
#
# plt.show()
