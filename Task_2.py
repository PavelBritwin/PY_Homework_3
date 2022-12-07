# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random

myList = []
prodList = []

for i in range(random.randrange(5, 10)):
    myList.append(random.randrange(1, 9))

for j in range(round(len(myList)/2)):
    prodList.append(myList[j] * myList[len(myList) - j - 1])

print(myList)
print(prodList)