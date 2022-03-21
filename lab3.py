import random
from ciagi import *

# Zadanie 1
a = [1 - x for x in range(1, 11)]
print(a)
b = [4 ** x for x in range(0, 8)]
print(b)
c = [x for x in b if (x % 2 == 0)]
print(c)

# Zadanie 2
lista1 = [random.randint(0, 100) for i in range(0, 10)]
print(lista1)
lista2 = [x for x in lista1 if (x % 2 == 0)]
print(lista2)

# Zadanie 3
produkty = {'Coca-cola': 'l',
            'Jabłka': 'kg',
            'Banany': 'szt',
            'Woda': 'l',
            'Bochenek chleba': 'szt',
            'Jogurt': 'szt'}
produktyWszt = {key: val for key, val in produkty.items() if (val == 'szt')}
print(produktyWszt)


# Zadanie 4
def czyProstokatny(a, b, c):
    if (a ** 2 + b ** 2 == c ** 2) | (a ** 2 + c ** 2 == b ** 2) | (b ** 2 + c ** 2 == a ** 2):
        return 'Trojkat jest prostokatny'
    else:
        return 'To nie jest trojkat prostokatny'


print(czyProstokatny(5, 3, 4))


# Zadanie 5
def poleTrapezu(a=1, b=2, h=2):
    return 'Pole wynosi: ' + str((a + b) / 2 * h)


print(poleTrapezu())
print(poleTrapezu(2, 3, 2.5))


# Zadanie 6
def iloczynCiagu(a=1, b=4, ile=10):
    if (a == 0): return 0
    if (b == 0): return 0
    iloczyn = a
    for x in range(0, ile):
        iloczyn *= a
        a *= b
    return iloczyn


print(iloczynCiagu(2, 2, 2))
print(iloczynCiagu(ile=3))


# Zadanie 7


# Zadanie 8
def productCountAndPrize(**products):
    prize = 0
    for key in products:
        prize += float(products[key])
    return len(products), prize


produkty = {'Coca-cola': 3.50,
            'Woda': 2.50,
            'Czekloada Milka': 4.99,
            'Sushi': 14.99}
print(productCountAndPrize(Woda=2.50,
                           Czekolada=4.99,
                           Sushi=14.99))

# Zadanie 9
a2 = ciag_geometryczny.nty_wyraz(1, 2, 4)
print('Wartosc:', a2)
s4 = ciag_geometryczny.suma_n_wyrazow(1, 2, 4)
print('Suma:', s4)
a3 = ciag_arytmetyczny.nty_wyraz(1,2,2)
print('Wartosc:',a3)
