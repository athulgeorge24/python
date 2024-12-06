print("Hello welcome to stick game...!")
print("Rules:")
print("Two players take turns to play the game.\n"
      "Each player picks one set of sticks (needn’t be adjacent) during his turn.\n"
      "A set contains 1, 2, or 3 sticks. The player who takes the last stick is the loser.")
name1=str(input("Enter the first player name:\n"))
name2=str(input("Enter the Second player name:\n"))
stickcount=int(input("Enter the no of sticks:\n"))
while True:

    print("Current number of sticks:",stickcount)
    a=int(input(f"It's {name1}'s chance,pick a set (1,2 or 3) sticks:\n"))
    if a==3:
        stickcount-=3
    elif a==2:
        stickcount-=2
    elif a==1:
        stickcount-=1
    else:
        print("Invalid Set\n")

    if stickcount==0:
        print(f"You choose the last stick...!You lose.\n{name2} wins")
        break

    print("Current number of sticks:", stickcount)
    b = int(input(f"It's { name2 }'s chance,pick a set (1,2 or 3) sticks:\n"))

    if b==3:
        stickcount-=3
    elif b==2:
        stickcount-=2
    elif b==1:
        stickcount-=1
    else:
        print("Invalid Set")

    if stickcount==0:
        print(f"You choose the last stick...!You lose.\n{name1} wins")
        break

