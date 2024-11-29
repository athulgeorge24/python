'''
Author:Athul George
Discription:Program to find the factorial of a number using Recursion.
'''


def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)


x=int(input("Enter the number:"))
y=factorial(x)

print("Factorial of the given number is:",y)
