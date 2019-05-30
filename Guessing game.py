from random import randint
random = randint(1, 10)
x = 0

while x != random:
    x = int(input("Guess a number from 1 to 10: "))
    if x > random:
        print("Number is too high, try again!")
    elif x < random:
        print("Number is too low, try again!")
    else:
        print("You found it!")
        rep = input("Do you want to play again? (y/n) ")
        if rep == "y":
            random = randint(1, 10)
            x = 0
        else:
            print("Game is finished")
            break

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
total_donations += for v in donations.values()
print(total_donations)