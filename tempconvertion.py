temp=int(input("Enter the temperature:"))
while True:
    print("\n1.\tConvert Fahrenheit to Celcius")
    print("2.\tConvert Celcius to Fahrenheit")
    print("3.\tExit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        c=(temp-32)*(9/5)
        print("Temperature in celcius:",c)
    elif choice==2:
        f=temp*(9/5)+32
        print("Temperature in Fahrenheit:",f)
    elif choice==3:
        break
    else:
        print("Invalid choice")

