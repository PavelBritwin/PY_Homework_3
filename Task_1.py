# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import random

myList = []
sum = 0
for i in range(random.randrange(5, 7)):
    myList.append(random.randrange(-9, 9))
    if (i % 2 == 1):
        sum += myList[i]
print(myList)
print(sum)
