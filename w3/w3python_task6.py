r1=int(input("Enter lower range:"))
r2=int(input("Enter upper range"))
num=int(input("Enter a number:"))
def raan(r1,r2,num):
    if num>r1 and num<r2:
        return "The given value exist in the given range"
    else:
        return "The given value not exist in the given range"
x=raan(r1,r2,num)
print(x)