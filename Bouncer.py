#ask for age
age = input("How old are you? ")
if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter, but you need a wristband!")
    elif age >= 21:
        print("You are good to go")
    else:
        print("You are too young, lad. Bye")
else:
    print("Please enter an age!") and return
