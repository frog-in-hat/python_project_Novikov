'''

'''

while True:
    try:
        a = float(input('Введите 1 число модуль числа <1'))
        s = int(input('Введите 2 чсло >0'))
        if a < 0:
            a = a * -1
        if a > 1:
            print('Error')
            continue
        if s < 0:
            print('Error')
            continue
        print(a,s)

    except ValueError: print('Error')
    for i in range(3)
    s = a - (a**3)/3 + (a**5)/5 -