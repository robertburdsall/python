import random


game = ["rock", "paper", "scissors"]


computer = random.choice(game)
player = None

while player not in game:
    player = input("Please select rock, paper, or scissors!: ").lower()

if player == computer:
    print("computer: "+computer)
    print("player: "+player)
    print("Tie!")
elif player == "rock":
    if computer == "paper":
        print("computer: " + computer)
        print("player: " + player)
        print("The computer wins!")
    elif computer == "scissors":
        print("computer: " + computer)
        print("player: " + player)
        print("You win!")
elif player == "paper":
    if computer == "rock":
        print("computer: " + computer)
        print("player: " + player)
        print("You win!")
    elif computer == "scissors":
        print("computer: " + computer)
        print("player: " + player)
        print("The computer wins!")
elif player == "scissors":
    if computer == "rock":
        print("computer: " + computer)
        print("player: " + player)
        print("The computer wins!")
    elif computer == "paper":
        print("computer: " + computer)
        print("player: " + player)
        print("You win!")