# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

petr=0
serg=0
katya=0
s= int(input('Введите число журавликов  S='))
if s%4==0:
    print ("Петр сделал =", s/6)
    print ("Сергей сделал =", s/6)
    print ("Катя сделала =", s*2/3 )
else:
    print ("количество не корректное  ") 