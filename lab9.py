import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Zad 1
# xlsx= pd.ExcelFile('imiona.xlsx')
# dane = pd.read_excel(xlsx,header=0)
# print(dane)
# grupaRok = dane.groupby(['Rok']).agg({'Liczba':['sum']})
# grupaRok.plot(legend=True,figsize=(8,6))
# plt.show()

#Zad 2
# plec = dane.groupby(['Plec']).agg({'Liczba':['sum']})
# print(plec)
# plec.plot(kind='bar',xlabel='Płec',ylabel='Liczba',rot=0)
# plt.show()

#Zad 3
# data = dane.groupby(['Rok']).agg({'Liczba':['sum']}).tail(5)
# print(data)
# data.plot(kind='pie',subplots=True,autopct='%.2f%%',rot=0,legend=False,title='Ilość urodzonych chłopców i dziewczynek')
# plt.show()

#Zad 4
# dane = pd.read_csv('zamowienia.csv',header=0,sep=';',decimal='.')
# ileZamowien = dane.groupby(['Sprzedawca']).agg({'Sprzedawca':['count']})
# ileZamowien.plot(kind='bar',title='Ilość zamówionych zamówień',width=0.5,rot=0,ylabel='Ilosc zamówien',xlabel='Nazwa sprzedawcy',figsize=(9,6))
# plt.show()