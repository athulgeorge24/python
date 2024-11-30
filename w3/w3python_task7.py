from curses.ascii import isupper, islower


def count(string):
    up=0
    low=0
    for i in string:
        if i.isupper():
            up=up+1
        if i.islower():
            low=low+1
        return (up,low)

x=input("Enter the string:")
y=count(x)
print(y)
