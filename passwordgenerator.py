import random as r
x = r.randint(1,20)
i = input("Guess Number")

i = print('Try '+ 1)
if i == x:
    print('You WON!')
elif i != x:
    print("You LOSE")
