# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))
fibList = [0, 1]
negfibList = []

x = 2
while (x <= n):
    fibList.append(fibList[x - 1] + fibList[x - 2])
    x += 1

x = 1
while (x <= n):
    negfibList = [(-1) ** (x + 1) * fibList[x]] + negfibList
    x += 1

print(negfibList + fibList)
