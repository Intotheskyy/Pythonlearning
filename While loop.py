from random import randint
number = randint(1, 10)  # store random number in here, each time through
i = 0
while number != 5:
    number = randint(1, 10)
    i += 1

print(i)
# i should be incremented by one each iteration

