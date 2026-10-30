'''
в22 Дано вещественное число X (|X|<1) и целое число N (>0). Найти значение выражения
X - X3/3 + X5/5 - ... + (-1)NX2N +1/(2N +1). Полученное число является приближенным
значением функции arctg в точке X.
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
        break

    except ValueError: print('Error')
i = 1
yr = a
o = 1
while i < s:
    if i+2 > s:
        break
    i+=2
    if o//2 == 0:
        yr -= (a**i)/i
    elif o//2 != 0:
        yr += (a**i)/i
print(yr)
