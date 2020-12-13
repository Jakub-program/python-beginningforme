from math import pi

def obsah_elipsy(a, b):
    return pi * a * b

x=int(input('Zadej číslo: '))
y=int(input('Zadej číslo: '))
print('Obsah je', obsah_elipsy (x, y))