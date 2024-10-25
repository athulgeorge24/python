"""
Author:Athul George
Date:25/10/2024
Discription:program to convert temperature values back and forth between
Celsius and Fahrenheit. The user should be able to input a temperature in Celsius
 or Fahrenheit, and the program should convert it to the other unit using formula
"""
temp=int(input("Enter temperature:"))
unit=input("Is this in (C)elsius or (F)ahrenheit:")
if unit=="C":
    f=(9/5)*temp+32
    print(temp,"Celsius is",f,"fahrenheit")
elif unit=="F":
    c=(9/5)*(temp-32)
    print(temp,"fahrenheit is",c,"celsius")
else:
    print("invalid character")


