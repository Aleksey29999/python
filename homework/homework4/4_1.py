# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n= int(input("Введите количество чисел первого множества="))
nombers1 = set()
[nombers1.add(int(input("Введите числа первого множества="))) for i in range(n)]
m= int(input("Введите количество чисел второго множества="))
nombers2 = set()
[nombers2.add(int(input("Введите числа второго множества="))) for i in range(m)]
print(nombers1, nombers2, sorted(nombers1.intersection(nombers2)))


# n= int(input("Введите количество чисел первого множества="))
# nombers1 = set()
# for i in range(n):
#     nombers1.add(int(input("Введите числа первого множества=")))
#     print(nombers1)
# m= int(input("Введите количество чисел второго множества="))
# nombers2 = set()
# for i in range(m):
#     nombers2.add(int(input("Введите числа второго множества=")))
#     print(nombers2)
# nombers3 = set()
# nombers3 = nombers1.intersection(nombers2) 
# print(nombers3)
# print(sorted(nombers3))