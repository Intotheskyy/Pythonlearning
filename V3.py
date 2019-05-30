import random
player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
    print(f"Player score {player_wins} Computer score {computer_wins}")
    print("...rock...paper..scissors...")

    player_1 = input("Player 1 choice is: ").lower()
    if player_1 == "quit" or player_1 == "q":
        print("Closing game")
        break
    choices = ["rock", "paper", "scissors"]
    player_2 = random.choice(choices)
    # player_2 = input("Player 2 choice is: ")
    print(f"!!Computer rolled {player_2} !")
    if player_1 == player_2:
        print("IT'S A DRAW")
    elif player_1 == "rock":
        if player_2 == "paper":
            print("Compukter WON")
            computer_wins += 1
        elif player_2 == "scissors":
            print("Player 1 WON")
            player_wins += 1
    elif player_1 == "scissors":
        if player_2 == "paper":
            print("Player 1 WON")
            player_wins += 1
        elif player_2 == "rock":
            print("Compukter WON")
            computer_wins += 1
    elif player_1 == "paper":
        if player_2 == "rock":
            print("Player 1 WON")
            player_wins += 1
        elif player_2 == "scissors":
            print("Compukter WON")
            computer_wins += 1
    else:
        print("something is not right")
