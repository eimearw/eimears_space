#!/usr/bin/python
try:
    import random

    computer_choice = random.choice(["scissors","rock","paper"])

    user_choice = input ("Do you want - rock, paper or scissors?\n")

    if computer_choice == user_choice:
        print("Tie")
    elif user_choice == "rock" and computer_choice == "scissors":
        print ("You win")
    elif user_choice == "paper" and computer_choice == "rock":
        print ("machine win")
    elif user_choice == "scissors" and computer_choice == "paper":
        print ("You win")
    else:
        print ("You are a loser :(")
except Exception as ex:
    print(ex)
    