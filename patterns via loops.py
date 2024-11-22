#Incresasing triangle
rows1=int(input("enter the no.of rows:"))
for i in range(0,rows1):
    for j in range(0,i+1):
        print("*",end="")
    print('')

#Decreasing triangle
rows2=int(input("enter the no.of rows:"))
for a in range (rows2,0,-1):
    for b in range(a,0,-1):
        print("*",end="")
    print('')

#Hill pattern
rows3=int(input("enter the no.of rows:"))
for l in range(1,rows3+1):
    for j in range(rows3-l):
        print(" ",end="")
    for k in range(2*l-1):
        print("*", end="")
    print('')

#Reverse hill pattern
rows3=int(input("enter the no.of rows:"))
for l in range(rows3+1,0,-1):
    for j in range(rows3-l):
        print(" ",end="")
    for k in range(2*l-1):
        print("*", end="")
    print('')



