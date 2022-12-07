# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def dectobin(x):
    result = ''
    while (x >= 2):
        result += str(x % 2)
        x = x // 2
    return '1' + result[::-1]
print(dectobin(45))