import sys
import random

#Zadanie 1
lista = []
for i in range(10):
    lista.append(random.randint(0,30)*2)
plik = open("noweDane.txt",'w+')
plik.write(str(lista))
plik.close()

#Zadanie 2
plik = open("noweDane.txt","r")
dane = plik.readlines()
print(dane)
plik.close()

#Zadanie 3
with open("dane2.txt","a+") as plik:
    for i in range(5):
        wartosc = input('Napisz cos: ')
        plik.write(wartosc)
        plik.write('\n')
with open("dane2.txt","r") as plik:
    for linia in plik:
        print(linia,end="")

#Zadanie 4

class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednosta_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        print('Nazwa produktu:',self.nazwa_produktu,'\nIlosc:',self.ilosc,
              '\nJednostka miary:',self.jednosta_miary,'\nCena jednostka:',self.cena_jed)
    def ile_produktu(self):
        print(self.ilosc,self.jednosta_miary)
    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed
zakupy = NaZakupy('Woda',3,'szt',1.50)
zakupy.wyswietl_produkt()
print(zakupy.ile_kosztuje())
zakupy.ile_produktu()

#Zadanie 5

class Ciagi:
    wartosci = []
    def wyswietl_dane(self):
        print(self.wartosci)
    def pobierz_elementy(self,*val):
        for i in val:
            self.wartosci.append(i)
    def pobierz_parametry(self,a1,r,n):
        self.wartosci = []
        for i in range(n):
            self.wartosci.append(a1)
            a1+=r
    def policz_sume(self):
        suma = 0
        suma = sum(self.wartosci)
        return suma
ciag = Ciagi()
ciag.pobierz_elementy(2,6,4,6)
ciag.wyswietl_dane()
ciag.pobierz_parametry(1,2,5)
ciag.wyswietl_dane()
print(ciag.policz_sume())

#Zadanie 6

class Robaczek:
    def __init__(self,x,y,krok):
        self.x = x
        self.y = y
        self.krok = krok
    def idz_w_gore(self,ile_krokow):
        self.y = self.y+self.krok*ile_krokow
    def idz_w_dol(self,ile_krokow):
        self.y = self.y - self.krok * ile_krokow
    def idz_w_lewo(self,ile_krokow):
        self.x = self.x - self.krok * ile_krokow
    def idz_w_prawo(self,ile_krokow):
        self.x = self.x + self.krok * ile_krokow
    def pokaz_gdzie_jestes(self):
        print("Wspolrzedne: (",self.x,',',self.y,")")

robaczek = Robaczek(0,0,1)
robaczek.idz_w_dol(3)
robaczek.idz_w_lewo(5)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_prawo(12)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_gore(13)
robaczek.pokaz_gdzie_jestes()