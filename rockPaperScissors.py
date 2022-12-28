#!/bin/python3
import random

#function to receive user input band determine computer choice
def get_choices():
    player_choice = input("Enter a choice (rock,paper,scissors): ")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {'player': player_choice.upper().strip(
    ), 'computer': computer_choice.upper().strip()}
    return choices

#function to valid the user and computer choices
def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!!"
        else:
            return "Paper covers rock! You lose!!!"
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cuts paper! You lose!!!"
        else:
            return "Paper covers rock! You win!!!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! you win!!!"
        else:
            return "Rock smashes scissors! You lose!!!"

#calls the get_choices function
choices = get_choices()
#stores the outcome of the game in the result variable
result = check_win(choices["player"], choices["computer"])
#outputs the final outcome
print(result)