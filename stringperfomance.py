'''
Author:Athul George
Date:19/10/24
Python program that performs create, concatenate, and print a string and access a sub-string from a given string.
'''

name1=input("Enter your first name:")
name2=input("Enter your last name:")
name=name1+" "+name2
print("Your name is ",name)
lenghtof_name1 =len(name1)
extracted_name=name[:lenghtof_name1]
print("sub-string that consists of the last name only:",extracted_name)