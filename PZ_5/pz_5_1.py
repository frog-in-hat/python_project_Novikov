'''
 Найти сумму чисел ряда 1,2,3,...,60 с использованием функции нахождения суммы.
Использовать локальные переменные.
'''

while True:
    try:
        x = 0
        for i in range(1, 61):
            print(i)
            x +=i
        print(x)
        break
    except ValueError: print('error')