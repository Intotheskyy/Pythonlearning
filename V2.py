print("...rock...paper..scissors...")
player_1 = input("Player 1 choice is: ")
player_2 = input("Player 2 choice is: ")
if player_1 == player_2:
    print("IT'S A DRAW")
elif player_1 == "rock":
    if player_2 == "paper":
        print("Player 2 WON")
    elif player_2 == "scissors":
        print("Player 1 WON")
elif player_1 == "scissors":
    if player_2 == "paper":
        print("Player 1 WON")
    elif player_2 == "rock":
        print("Player 2 WON")
elif player_1 == "paper":
    if player_2 == "rock":
        print("Player 1 WON")
    elif player_2 == "scissors":
        print("Player 2 WON")
else:
    print("something is not right")
