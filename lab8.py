import pandas as pd
import numpy as np

#Zad 1
xlsx = pd.ExcelFile('imiona.xlsx')
imiona = pd.read_excel(xlsx,header=0)
print(imiona)

#Zad 2
print(imiona[imiona['Liczba'] > 1000])
print(imiona[imiona['Imie']=='PAWEL'])
print(imiona.agg({'Liczba':['sum']}))
print(imiona[(imiona['Rok'] >= 2000) & (imiona['Rok'] <= 2005)].agg({'Liczba':['sum']}))
print(imiona.groupby('Plec').agg({'Liczba':['sum']}))
print()

#Zad 3
file = pd.read_csv("zamowienia.csv",header=0,sep=";",decimal=".")

print(file)
a = file.groupby(['Sprzedawca'])
print(list(a.groups))
print(file.sort_values('Utarg',ascending=False).head(5))
print(file.groupby('Sprzedawca').agg({'Sprzedawca':['count']}))
print(file.groupby('Kraj').agg({'Utarg':['sum']}))
print(file[(file['Data zamowienia']>='2005-01-01') & (file['Data zamowienia']<='2005-12-31') & (file['Kraj']=='Polska')].agg({'Utarg':['sum']}))
#a = file[file['Data zamowienia'].between('2004-01-01','2004-12-31')].groupby(['Utarg'])

