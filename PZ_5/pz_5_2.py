'''
Описать функцию Mean(X, Y, AMean, GMean), вычисляющую среднее
арифметическое AMean = (X+Y)/2 и среднее геометрическое GMean = y/X Y двух
положительных чисел X и Y (X и Y — входные, AMean и GMean — выходные
параметры вещественного типа). С помощью этой функции найти среднее
арифметическое и среднее геометрическое для пар (A, B), (A, C), (A, D), если даны
A, B, C, D.
'''
while True:
    try:
        def Mean(X, Y):
            AMean = (X+Y)/2
            GMean = Y/X
            print(str(AMean) + '   ' + str(GMean))
        Mean(10, 5)
        Mean(10, 88)
        Mean(10, 90)
        break

    except ValueError: print('Error')
