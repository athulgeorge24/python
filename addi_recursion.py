num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))

def addition(num1,num2):
    if num2==0:
        return num1
    else:
        return addition(num1+1,num2-1)

if num1>0 and num2>0:
    y=addition(num1,num2)
    print("sum=",y)
else:
    print("enter valid positive numbers")
