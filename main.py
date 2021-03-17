# # Zad 1
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# zbior_1 = [1-x for x in A]
# print(zbior_1)
# zbior_2 = [4**y for y in range(8)]
# print(zbior_2)
# zbior_3 = [z for z in zbior_2 if z % 2 == 0]
# print(zbior_3)

# # Zad 2
# import random
# losowo = []
# for x in range(10):
#     losowo.append(random.randint(0, 100))
# print(losowo)
# parzyste = [x for x in losowo if x % 2 == 0]
# print(parzyste)

# # Zad 3
# produkty = {"woda": "sztuki", "orzechy": "kg", "pomidory": "kg", "konserwa": "sztuki", "chleb": "sztuki"}
# sztuki = [keys for keys, values in produkty.items() if values == "sztuki"]
# print(produkty)
# print(sztuki)

# # Zad 5
# def trapez(a=3, b=9, h=5):
#     p = ((a+b)*h)/2
#     print("Pole trapezu wynosi: ")
#     return p
# print(trapez())

# # Zad 6
# def ciag(a1=2, b=2, ile=2):
#     for i in range(ile):
#         a1 *= b
#     return a1
# print(ciag())

# # Zad 7
# def ciag(a1=2, b=2, ile=2):
#     a1 = (a1**ile)*b
#     return a1
# print(ciag())

# # Zad 8
# koszyk = {"Bułki": 5, "Banany": 8, "Napoje": 15, "Wędliny": 5, "Alkohol": 69.99}
# def lista(a):
#     b = 0
#     c = 0
#     for x in a.values():
#         b = b + x
#         c += 1
#     print('Za zakupy zapłacisz', b, "zł.")
#     print("Ilosc rzeczy w koszyku", c)
#     return c
# print(lista(koszyk))

# # Zad 9
# import Ciagi
# from Ciagi import *