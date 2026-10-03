while True:
 try:
  chislo = int(input('Введите число больше 999: '))
  print((chislo//100)%10)
 except: print('Error')
