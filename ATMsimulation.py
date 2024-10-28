from random import choice

balance_amt=1000
while True:
    print("\n1.\tCheck balance")
    print("2.\tDeposite money")
    print("3.\tWithdraw money")
    print("4.\tExit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print(f"The current balance ${balance_amt}")
    elif choice==2:
        deposit_amt=float(input("Enter the amount"))
        balance_amt=balance_amt+deposit_amt
        print(f"The deposited amount :${deposit_amt} and the current balance ${balance_amt}")
    elif choice==3:
        withdraw_amt=float(input("Enter the amount:"))
        if withdraw_amt>balance_amt:
            print("Insufficient amount")
        else:
            balance_amt = balance_amt - withdraw_amt
            print(f"The withdrawed amount :${withdraw_amt} and the current balance ${balance_amt}")
    elif choice==4:
        break
    else:
        print("Invalid entry")