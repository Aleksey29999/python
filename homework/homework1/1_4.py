# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
#  отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no
m= int(input('Введите размер долек m= '))
n= int(input('Введите размер долек n= '))
k= int(input('Введите число долек k= '))
if ((m%k==0 or n%k==0) and (k>=m or k>=n) and k<m*n) or ((k%n==0 or k%m==0) and (k>=m or k>=n) and k<m*n):
    print("да")
else:
    print("нет")