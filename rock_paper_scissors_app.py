def play_round():
    computer_choice
    player_choice
    game_logic
    output_result

while loop:
    update score
    update rounds played

    show wins + rounds played 
    play_again ?


import random

def play_round():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    player_choice = input("Eneter your choice (rock, paper or scissors): ")
    print(f"computer chose {computer_choice}")
    if player_choice.lower() == computer_choice
        return "tie"
    elif player_choice.lower() == "rock":
        if computer_choice == "sissors":
            return "user"
            else:
                return "computer"
        elif player_choice.lower() == "paper":
            return "user"
            else:
                return "computer"
        if computer

        return play_round()

num_rounds = 0
user_wins = 0
computer_wins = 0
play_again = "y"

while play_again.lower() == "y":
    num_round += 1
    result = play_round()
    if result == user:
        user_wins += 1
        print("You win!")
    elif result == "computer":
        computer_wins += 1
        print("computer wins")
    else:
        print("tie game")
    print(f"rounds played: {num_rounds}")
    print(f"User wins: {user_wins}")
    print(f"Computer wins: {computer_wins}")
    play_again = input("Do you want to play again? y/n")

    show wins + rounds played 
    play_again ?