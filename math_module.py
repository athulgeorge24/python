'''
Author:Athul George
Date:18/10/24
Discription:program that uses functions from the math module to perform the following operations on a number provided by the user
'''

import math
from math import factorial

num=int(input("Enter a number-"))
sqnum= math.sqrt(num)
print("square root of",num, "is",sqnum)
fac= math.factorial(num)
print("Factorial of",num, "is",fac)
powe=math.pow(num,2)
print(num, "raise to 2 is" ,powe)