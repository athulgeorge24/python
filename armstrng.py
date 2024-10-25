"""
Author:Athul George
Date:25/10/2024
Discription:Program to find whether the given number is armstrng or not
"""
num=int(input("Enter a number:"))
sumdigit=0
while num>0:
    reminder=num%10
    sumdigit=sumdigit+(reminder**3)
    num=num//10

print("Sum of digit of the given number is",sumdigit)