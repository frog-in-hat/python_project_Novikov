'''
Вариант22
1. Дан список размера N и целые числа K и L (1 < K ≤ L ≤ N). Найти среднее
арифметическое всех элементов списка, кроме элементов с номерами от K до L
включительно.
'''
import random
while True:
    n = int(input('Введите число N'))
    k = int(input('Введите число K'))
    l = int(input('Введите число L'))
    spisok = []
    zxc = 0
    for i in range(1, n+1):
     a= random.randint(1,11)
     spisok.append(a)
     if a != k or l:
      zxc +=a
    print(spisok)
    print(zxc/n)
    break
