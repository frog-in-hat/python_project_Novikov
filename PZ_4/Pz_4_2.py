'''
 Дано число A (>1). Вывести наибольшее из целых чисел K, для которых сумма 1 +
1/2 + ... + 1/K будет меньше A, и саму эту сумму.
'''
while True:
    try:

        a = float(input('Введите 1 чсло >0 '))
        K = int(input('K '))

        if a <= 1:
            print('Error')
            continue

        num = 0
        for i in range(1, K+1):

            if num + 1/i >= a:
                break
            num += 1/i
        print(num, i)

    except ValueError: print('Error')
