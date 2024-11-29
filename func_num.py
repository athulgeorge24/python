'''
Author: Athul George
task:Program to check whether the given number is a
valid mobile number or not using function
'''

def phn_num(num):
    if len(num)==10 and num[0] in '987':
        print( "It's a valid number")
    else:
         print("It's not a valid number")


x=str(input("Enter the number:"))
phn_num(x)

