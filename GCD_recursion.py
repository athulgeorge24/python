'''
Author:Athul George
Discriptiom:Recursive function to find the greatest common divisor
of two positive numbers.Euclidean Algorithm for Greatest Common Divisor (GCD)
'''
num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
def gcd(num1,num2):
    if num1>0 and num2>0:
        if num1%num2==0:
            return num2
        else:
            return gcd(num2,num1%num2)
    else:
        print("The given numbers are not positive")

y=gcd(num1,num2)
print("GCD of given numbers is:",y)