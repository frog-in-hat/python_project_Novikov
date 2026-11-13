def sym(a):
 total = 0
 while a > 0:
     total += a %10
     a = a //10
     return total
 print(total)
z = int(input())
x = int(input())
c = int(input())
z = sym(z)
x = sym(x)
c = sym(c)
print(z,x,c)
max_sym= max(z, x)
print(max_sym)

