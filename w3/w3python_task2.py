

def addition(list):
    sum=0
    for i in list:
        sum=sum+i
    return sum


summ=[]
x=int(input("Enter the limit:"))
for i in range(x):
    number=int(input("Enter the number"))
    summ.append(number)
summ=addition(summ)
print(summ)
