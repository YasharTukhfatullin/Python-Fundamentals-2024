import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)

    player = None
    while player not in choices:
        player = input(f"rock, paper, or scissors? ").lower()

    if player == computer:
        print(f"Computer: {computer}")
        print(f"Player: {player}")
        print(f"Tie")
    elif player == "rock":
        if computer == "paper":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print(f"You lose")
        if computer == "scissors":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print(f"You Win")
    elif player == "scissors":
        if computer == "rock":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print(f"You lose")
        if computer == "paper":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print(f"You Win")
    elif player == "paper":
        if computer == "scissors":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print(f"You lose")
        if computer == "rock":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print(f"You Win")

    play_again = input("Play again? (Yes/No): ").lower()

    if play_again != "yes":
        break

print("Bye")
