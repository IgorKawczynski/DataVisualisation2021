import math

def rownanie_kwadratowe(a,b,c):
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Nie ma rozwiazan")
    elif delta == 0:
        x = ((-1) * b) / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2
