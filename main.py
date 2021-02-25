# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import sys as system

print(system.version)

from math import *
a = 2
print (a)

b = 'tekst'
print (b)

c = 'tekst2'
print (b + ' ' + c) # ' ' its space

x = 5
y = 3.6
z = 3+6j
print(type(y)) #checker the datatype of variable
print(x+y+z)

x2 ='inzynieria \n systemow \n informatycznych \n'
print(x2)


#ctrl and slash is for commenting the lines

a2 = 10
b2 = 15

dodawanie = a2 + b2
odejmowanie = a2 - b2
mnozenie = a2 * b2
dzielenie = a2 / b2
dzielenie_calkowite = a2 // b2
potega = a2 ** b2
print(dodawanie,odejmowanie,mnozenie,dzielenie,dzielenie_calkowite,potega)

a2 = a2 + b2
print(a2)



print(pow(5,2))
print(sqrt(81))
print(pi)

print(u'inzynieria systemow informatycznych')
print('wynik dzialania jest rowny a = %(zm)d' % {'zm' : 15})


napis = 'isi'
grupa = 2
print('specjalizacja %s, grupa %d' %(napis,grupa))

a3 = 5
b3 = 3
c3 = 5 - 3
print('wynik dzialania %(zmienna1)d-%(zmienna2)d=%(zmienna3)d' % {'zmienna1' : a3, 'zmienna2' : b3, 'zmienna3' : c3})