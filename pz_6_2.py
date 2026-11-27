'''
2. Даны списки A и B одинакового размера N. Поменять местами их содержимое и
вывести вначале элементы преобразованного списка A, а затем — элементы
преобразованного списка B
'''
import random

while True:
    spi1 = []
    spi2 = []
    n = int(input('Введите N'))
    for i in range(1, n+1):
        a= random.randint(1,11)
        spi1.append(a)
    for i in range(1, n+1):
        a= random.randint(1,11)
        spi2.append(a) 
    print(spi1, spi2)
      
    for i in range(len(spi1)):
        spi2.append(spi1[i])
        spi1.append(spi2[i])  
    for i in range(0, n):
        spi1.pop(0)
        spi2.pop(0)         
    print(spi1, spi2)

    break       
