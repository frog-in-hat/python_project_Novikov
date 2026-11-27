'''
 Дано множество A из N точек (точки заданы своими координатами х, у). Среди всех
точек этого множества, лежащих во второй четверти, найти точку, наиболее
удаленную от начала координат. Если таких точек нет, то вывести точку с нулевыми
координатами.
Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
R = √(x2 – x1)2 + (у2 – y1)2
.
Для хранения данных о каждом наборе точек следует использовать по два списка: первый
список для хранения абсцисс, второй — для хранения ординат.
'''
import math, random

while True:
    try:
     abc =[] # x
     ordi =[] # y
     n = int(input('Введите N: '))
#присваивание x y координат 
     for i in range(1, n+1):
        a = random.randint(-10,10)
        abc.append(a)
     for i in range(1, n+1):
        a = random.randint(-10,10)
        ordi.append(a)
#проверка положения точек        
     abc2 = []
     ordi2 =[]    
     for i in range(0, n):
       if abc[i]< 0 and ordi[i]>0:
        abc2.append(abc[i])
        ordi2.append(ordi[i])     
#Начальные координаты x y         
     nach = [0,0] 
     otvr = [] #
     for i in range(0, len(abc2)):
      r = math.sqrt((abc2[i]-nach[1])**2 +(ordi2[i]-nach[0])**2)
      print(r)
      otvr.append(r)
#порядковый номер числа, которое дальше всех
     numotvr = otvr.index(max(otvr))

     print(f'x{abc2[numotvr]}, y{ordi2[numotvr]}' ) 
     print(abc2, ordi2, nach)
    except ValueError: print(nach)
    break
           