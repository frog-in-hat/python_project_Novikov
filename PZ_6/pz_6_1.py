'''
Вариант22
1. Дан список размера N и целые числа K и L (1 < K ≤ L ≤ N). Найти среднее
арифметическое всех элементов списка, кроме элементов с номерами от K до L
включительно.
'''
import random
while True:
    n = int(input('Введите число N(Кол-во в списке):'))
    k = int(input('Введите число K(1 число которое надо исключить):'))
    l = int(input('Введите число L(2 число котоое надо исключить):'))
    spisok = []
    zxc = 0
    cv = 0
    for i in range(1, n+1):
     a= random.randint(1,11)
     spisok.append(a)
     if a != k and a !=l:
      zxc +=a
      cv +=1
    print(spisok)
    print(zxc/cv)
    break
