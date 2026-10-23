'''
в22
Даны два числа. Вывести большее из них
'''
k = 0
while True:
    try:
        one = int(input('Введите 1 число'))
        two = int(input('Введите 2 число'))

        break
    except ValueError: print("Error")

if one>two:
    print(one)
else:
    print(two)
