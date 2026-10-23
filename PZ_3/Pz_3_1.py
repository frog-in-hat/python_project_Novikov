'''
В22

Дано трехзначное число. Провреить истинность
высказывания: Цифра жанного числа образует возрастаюую последовательность
'''

while True:
    try:
        a = int(input('Введите число: '))
        q,w,e= a//100, a//10%10, a%10
        if q<w<e:
            break
        else: continue
    except ValueError: print('Error')
print('good')