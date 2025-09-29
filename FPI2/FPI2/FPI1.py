a = int(input())
if 1 <= a <= 9:
    for i in range(a):
        print ("       _ ~_     ", end="")
    print()                
    for i in range(a):
        print ("      (o  o)    ", end="")
    print()                
    for i in range(a):
        print ("     /  \\/  \\   ", end="")
    print()                
    for i in range(a):
        print ("    /(   _  )\\  ", end="")
    print()                
    for i in range(a):
        print ("      ^^  ^^    ", end="")
    print() 
else:
    print("The number should be from 1 to 9")