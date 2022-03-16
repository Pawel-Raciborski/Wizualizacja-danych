import math

# lista = []
# for counter in range(0, 30):
#     if counter % 2 == 0:
#         lista.append(counter)
#
# print(lista)
#
# # mozna to zapisac w postaci jednolinijkowej:
# # Cw 1  (za pomoca petli for)
# print('\nCw1')
# a = []
# for x in range(0, 10):
#     a.append(x ** 2)
# print(a)
#
# # lista = [#coDodajemy for x in ...]
# a = [element ** 2
#     for element in range(0, 10)]
# print(a)
# # -------------------------------------------------
# print('\nCw2')
# # Cw 2 potegi liczby 3
# b = []
# for x in range(0, 6):
#     b.append(3 ** x)
# print('Za pomoca petli for: ',b)
#
# #za pomoca skroconej formy
# b = [3**x for x in range(0,6)]
# print('Skrocona forma: ',b)
# print('\nCw3')
# #---------------------------------------------------
#
# #Cw 3 indeksy nieparzyste
# c = []
# for x in a:
#     if x%2!=0:
#         c.append(x)
# print('Za pomoca petli for: ',c)
# #skrocona forma
# c = [x
#      for x in a
#      if x%2!=0]
# print('Skrocona forma: ',c)


# Cw 4
lista = []
for a in [1, 2, 3]:
    for b in [4, 5, 6]:
        lista.append((a, b))
print(lista)

lista2 = [(a, b) for a in [1, 2, 3] for b in [4, 5, 6]]
print(lista2)

# Cw 5 przyklad ze slownikiem
slownik = {'PZU': 'Państwowy Zakład Ubezpieczeń',
           'ZUS': 'Zakład ubezpieczeń społecznych',
           'PKO': 'Państwowa Kasa oszczędności'}
print('slownik przed odwrocoeniem: ', slownik)
slownik_odwrocony = {}
for key, value in slownik.items():
    slownik_odwrocony[value] = key
print('slownik_odwrocony po odwroceniu: ', slownik_odwrocony)

slownik2 = {value: key for key, value in slownik.items()}
print('Slownik2 : ', slownik2)


# tworzenie funkcji
# def nazwa_funkcji(argumenty)
# argumenty funkcji moga byc: pozycyjne,argumenty domyslne,*arg (dowolna ilosc krotki),**arg (dowolna ilosc argumentow z kluczem)

# Przyklad 1 (argumenty pozycyjne)
def row_kwadratowe(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Brak rozwiązan")
        return -1
    if delta == 0:
        print("Jedno rozwiązanie")
        x = (-b) / (2 * a)
        return x
    else:
        print("Dwa rozwiazania")
        x1 = ((-b) - math.sqrt(delta)) / (2 * a)
        x2 = ((-b) + math.sqrt(delta)) / (2 * a)
        return x1, x2


print(row_kwadratowe(6, -1, 3))
print(row_kwadratowe(1, 2, 1))
print(row_kwadratowe(1, 4, 1))


# Przyklad 2 Napisac funkcje ktora przyjmuje wartosc typu int
def isEven(a):
    if a % 2 == 0:
        print('Liczba ' + str(a) + ' jest parzysta')
    else:
        print('Liczba ' + str(a) + ' jest nieparzysta')


isEven(2)
isEven(5)


def dlugosc_odcinka(x1=0, y1=0, x2=0, y2=0):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


print('Dlugosc odcinka:', dlugosc_odcinka())
print('Dlugosc odcinka:', dlugosc_odcinka(1, 2, 3, 4))
print('Dlugosc:',
      dlugosc_odcinka(2, 2, x2=2, y2=1))  # nie moze byc np. print('Dlugosc:', dlugosc_odcinka(x2=2, y2=1,2, 2))
# mozna zmieniac kolejnosc podawanych argumentow
print('Dlugosc:', dlugosc_odcinka(x2=3, x1=2, y2=5, y1=-1))
print('Dlugosc:', dlugosc_odcinka(x2=2, y2=3))


# Funkcje z dowolna iloscia argumentow w krotce
def ciag(*liczby):  # konstrukcja do krotki
    if len(liczby) == 0:
        return 0
    else:
        suma = 0
        for i in liczby:
            suma += i
        return suma


print(ciag())
print(ciag(1, 3, 5, 3, 2, 5, 6))


# Funkcja z dwoma symbolami **
def co_lubie(**rzeczy):  # **cos - konstrukcja do slownika
    for cos in rzeczy:
        print("To jest")
        print(cos)
        print("Co lubie")
        print(rzeczy[cos])


co_lubie(slodycze='czekolada', gry=['lol', 'cs'])
