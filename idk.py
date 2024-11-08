
n=int(input("Enter list:"))
num=int(input("Enter number:"))
small=num
big=num
second_small=int(0)
second_big=int(0)
while n>1:
    num=int(input("Enter number:"))
    if num>big:
        second_big=big
        big=num
    elif num>second_big:
        second_big=num
    if num<small:
        second_small=small
        small=num
    elif num<second_small:
        second_small=num
    n=n-1
print("The biggest number is",big)
print("the second biggest is", second_big)
print("the second smallest is", second_small)
print("The smallest number is",small)
