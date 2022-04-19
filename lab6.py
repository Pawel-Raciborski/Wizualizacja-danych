import numpy as np

# Zad 1
# a = np.arange(0,80,4)
# print(a)

# Zad 2
# a = np.array([2.3,4.124,3.14,2,-4.3])
# b = a.astype('int32')
# print(b)
# print(b.dtype)

# Zad 3
# def foo(n):
#     matrix = 2**np.arange(n*n)
#     matrix = matrix.reshape((n,n))
#     return matrix
# print(foo(5))

# Zad 4
# def generuj(n,m):
#     tab = np.logspace(n,m+1,num=m,base=n)
#     return tab
# print(generuj(2,4))

# Zad 5
# def foo(length):
#     vector = np.arange(length,-1,-1)
#     diag = np.diag([x for x in vector],2)
#     return diag
# print(foo(5))

# Zad 6
# slowo1 = "zamek"
# slowo2 = "alfabet"
# slowo3 = "prawo"
# array = np.array(list(slowo1))

# Zad 7
# def funkcja(n):
#     tab = 2*np.ones((n,n))
#     for k in range(n):
#         tab_tmp = np.diag([2*k for x in range(n-k)],k)
#         tab_tmp2 = np.diag([2*k for x in range(n-k)],-k)
#         print(tab_tmp2)
#         tab+=tab_tmp
#         tab+=tab_tmp2
#     return tab
#
#
# print(funkcja(5))

#Zad 8
# def foo(tab,kierunek):
#     if kierunek == "pion":
#         if(tab.shape[1]%2!=0):
#             return "Nie mozna podzielic"
#         return a[:(int)(a.shape[0] / 2)]
#     elif kierunek == "poziom":
#         if (tab.shape[0] % 2 != 0):
#             return "Nie mozna podzielic"
#         return a[(int)(a.shape[0] / 2):]
#
# a = np.arange(4)
# a = a.reshape((2,2))
# print(a)
# print()
# print(foo(a,"pion"))

#Zad 9
# tab = np.arange(3,100,4)
# matrix = tab.reshape((5,5))
# print(matrix)
