num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
def addition(num1,num2):
   if num2==1:
       return num1
   else:
       return num1+addition(num1,num2-1)
      if num1>0 and num2>0:      
   y=addition(num1,num2)
   print("product=",y)
else:
    print("enter valid positive numbers")
