#Guess the number game

import random
small=int(input("Enter smallest number:"))
big=int(input("Enter largest number:"))
mynum=random.randint(small,big)
nooftry=0
while True:
    Guess=int(input("Guess the number:"))
    nooftry += 1
    if Guess<mynum:
        print("Your guess is too low,try again!")
    elif Guess>mynum:
        print("Your guess is too high,try again!")
    else:
        print("Congratulations...!Your guess is correct")
        break
print("Total tries:",nooftry)