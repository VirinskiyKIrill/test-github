width = 17
height = 12.0
print (width//2)
print (width/2.0)
print (height/3)
print (1 + 2 * 5)
#print (int('123e'))
#print (int('91,4'))
#print (int('524.345 ** 435345345311145345'))
#print (int('7.1 + 4'))
#print (int('4' - 2))
#print (int('4 - 2'))
#print (int('42'))
#print (int(-12.12))
num3 = 1921000
mb = 0
kb = 0
while num3 > 1024:
    nom3 -= 1024
    kb += 1
while kb > 1024:
    kb -= 1024
    mb += 1
print(mb)
a = int(input())
b = int(input())
if 1 < (a or b) < 1000:
    result = [a, b][a <= b]
    print (result)
else:
    print ("The numbers are not included in the range")
if a % b == 0:
    print("YES")
else:
    print("NO")
s = int(input())
m = 0 
h = 0
while s >= 60:
    s -= 60
    m += 1
while m >= 60:
    m -= 60
    h += 1
while h >= 24:
    h == 0
print('{}:{:02}:{:02}'.format (h,m,s))
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if ((a % b == 0) and (c % b == 0)):
    print("YES")
    print("White")
elif ((a % b == 1) and (c % b == 1)):
    print("YES")
    print("Black")
else:
    print("NO")

    
