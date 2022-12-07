# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import math
import random

myList = []

for i in range(5):
    myList.append(round(random.uniform(0, 5), 2))
print(myList)

for j in range(len(myList)):
    myList[j] -= math.floor(myList[j])
    myList[j] = round(myList[j], 2)

print(max(myList) - min(myList))
