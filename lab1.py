import math # aby korzystac z funkcji matemaatycznych potrzebny import biblioteki math

#Zad1 Napisz pierwszy skrypt w ktorym zadeklarujesz po dwie zmienne kazdego typu
# a nastepnie wyswietl te zmienne
s1 = 'Ala ma kota 1'
s2 = "Ala ma kota 2"
s3 = """Ala 
ma 
kota 3"""
print(s1)
print(s2)
print(s3)
i1 = 13
i2 = -20
print('Wartosc i1= %(zm1)d oraz wartosc zmiennej i2 = %(zm2)d'%{'zm1':i1,'zm2':i2})
f1 = 3.14
f2 = -0.32
print(f1)
print(f2)
c1,c2 = 2+3j,-3-0.5j
print('Zmienna c1= ' + str(c1) + ' zmienna c2= '+str(c2))


#Zadanie2
znak = input("Podaj znak: /,+,%,^,-,*")
a = input("Podaj liczbe: ")
b = input("Podaj liczbe: ")
a=float(a)
b=float(b)
if znak=='+':
    print("Suma: ",a+b)
elif znak=='-':
    print("Roznica = ",a-b)
elif znak=='^':
    if(a==0 & b==0):
        print("symbol nieoznaczony")
    else:
        print("Potega: ",a**b)
elif znak=='*':
    print("Iloczyn: ",a*b)
elif znak=='/':
    if(b==0):
        print("Nie dzielimy przez 0!")
    else:
        print("Dzielenie",a/b)
else:
    print("Nieprawidlowy znak")

#Zadanie3
a = input("Podaj pierwsza wartosc: ")
b = input("Podaj pierwsza wartosc: ")
a = float(a)
b = float(b)
a+=3
print(a)
b-=4+2
print(b)
a*=b
print(a)
b/=2
a**=3
print(a)
a%=15
print(a)

#Zadanie4
e= math.e**6
print(e)
log = (math.log(5+math.sin(8)**2))**(1/6)
print(log)
print(math.ceil(3.55))
print(math.floor(4.80))

#Zadanie5
imie = "PAWEL"
nazwisko = "RACIBORSKI"
print(imie.capitalize() + ' ' + nazwisko.capitalize())

#Zadanie6
tekst = """La la, la la la la la na na na na na
La la na na, la la la la la na na na na na
La la, la la la la la na na na na na
La la na na, la la la la la na na na na na
Hush, don't speak
When you spit your venom, keep it shut I hate it
When you hiss and preach
About your new messiah 'cause your theories catch fire"""
print(tekst.count("na"))

#Zadanie7
slowo = "Ala ma kota"
print(slowo[1])
print(slowo[len(slowo)-2])

#Zadanie8
print(tekst.split())
