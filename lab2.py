import sys as system
import math

# Zadanie 1
listaSportow = ['Skoki narciarskie', 'Pilka nozna', 'Biegi']
listaSportow.reverse()
listaSportow.append('Siatkowka')
listaSportow.insert(0, "Pilka reczna")
print(listaSportow)

# Zadanie 2
skrotySlow = {"HTML": "HyperText Markup Language", "JS": "JavaScript", "JVM": "Java Virtual Machine",
              "JRE": "Java Runtime Environment"}
skrotySlow['JDK'] = 'Java Development Kit'
print(skrotySlow)

# Zadanie 3
slownikGier = {1: 'PayDay 2', 2: "Dying Light 1/2", 3: "Red Dead Redemption 2", 4: "League of Legends",
               5: "Don’t Starve Together"}
print(slownikGier)
print("Dlugosc slownika: ", len(slownikGier))

# Zadanie 4
word = input("Wpisz zdanie: ")
length = word.lower().count('a')
print("Dlugosc slowa: ", length)

# Zadanie 5
system.stdout.write('Podaj pierwsza liczbe: ')
a = system.stdin.readline()
a = int(a)
system.stdout.write('Podaj druga liczbe: ')
b = system.stdin.readline()
b = int(b)
system.stdout.write('Podaj trzecia liczbe: ')
c = system.stdin.readline()
c = int(c)
system.stdout.write("Wartosc = " + str(a ** b + c))

# Zadanie 6
a = input("Podaj pierwsza wartosc: ")
b = input("Podaj druga wartosc: ")
c = input("Podaj trzecia wartosc: ")
a = int(a)
b = int(b)
c = int(c)
if (a > b) & (a > c):
    print("Wartosc: ", a, " jest najwieksza")
else:
    if (b > c):
        print("Wartosc najwieksza: ", b)
    else:
        print("Wartosc najwieksza: ", c)

# Zadanie 7
lista = [2, 1, 0, 5, 2.5, 10, -0.753, -2.8]
for i in range(0, len(lista), 1):
    lista[i] = lista[i] ** 2
print(lista)

# Zadanie 8
evenNumbers = []
i = 0
while i < 10:
    a = input("Podaj liczbe: ")
    a = float(a)
    if (a % 2 == 0):
        evenNumbers.append(a)
    i+=1
else:
    print("Lista: ",evenNumbers)

# Zadanie 9
value = input("Podaj wartosc: ")
try:
    value = float(value)
    print("Pierwiastek ",value," = ",math.sqrt(value))
except ValueError:
    if not value:
        print("Wartosc jest pusta!")
    elif isinstance(value,str):
        print("Nie jest to liczba rzeczywista!")
    else:
        print("To wartosc ujemna!")