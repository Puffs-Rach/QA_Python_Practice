import random

class RPS_Game:
    def __init__(self, rock, paper, scissors)

def play_round():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    player_choice = input("Enter your choice (rock, paper or scissors): ")
    print(f"computer chose {computer_choice}")
    if player_choice.lower() == computer_choice:
        return "tie"
    elif player_choice.lower() == "rock":
        if computer_choice == "scissors":
            return "user"
        else:
            return "computer"
    elif player_choice.lower() == "paper":
        if computer_choice == "rock":
            return "user"
        else: 
            return "computer"
    elif player_choice.lower() == "scissors":
        if computer_choice == "paper":
            return "user"
        else:
            return "computer"
    else:
        print("invalid choice try again")
        return play_round()
    
    

num_rounds = 0
user_wins = 0
computer_wins = 0
play_again = "y" - needs to go into the init method. dont want a seperate while loop and everything should eb in a class. Object needs to be made and then an obect needs to be called to play the game. 


while play_again.lower() == "y":
    num_rounds += 1
    result = play_round()
    if result == "user":
        user_wins += 1
        print("You win!")
    elif result == "computer":
        computer_wins += 1
        print("computer wins")
    else:
        print("tie game")
    print(f"Rounds played: {num_rounds}")
    print(f"User wins: {user_wins}")
    print(f"Computer wins: {computer_wins}")
    play_again = input("Do you want to play again? y/n: ")


import random

class RockPaperScissors:
    def __init__(self, num_rounds, user_wins, computer_wins):
        self.num_rounds = 0
        self.user_wins = 0
        self.computer_wins = 0

    def play_round(self):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        player_choice = input("Enter your choice (rock, paper, or scissors): ")
        print(f"Computer chose {computer_choice}")
        if player_choice.lower() == computer_choice:
            return "tie"
        elif player_choice.lower() == "rock":
            if computer_choice == "scissors":
                return "user"
            else:
                return "computer"
        elif player_choice.lower() == "paper":
            if computer_choice == "rock":
                return "user"
            else:
                return "computer"
        elif player_choice.lower() == "scissors":
            if computer_choice == "paper":
                return "user"
            else:
                return "computer"
        else:
            print("Invalid choice. Please try again.")
            return self.play_round()

    def start_game(self):
        play_again = "y"
        while play_again.lower() == "y":
            self.num_rounds += 1
            result = self.play_round()
            if result == "user":
                self.user_wins += 1
                print("You win!")
            elif result == "computer":
                self.computer_wins += 1
                print("Computer wins")
            else:
                print("It's a tie!")
            print(f"Rounds played: {self.num_rounds}")
            print(f"User wins: {self.user_wins}")
            print(f"Computer wins: {self.computer_wins}")
            play_again = input("Do you want to play again? (y/n): ")

# Create an instance of the game and start playing
game = RockPaperScissors()
game.start_game()


# every mutiple objects will keep their own object otherwise it would start on high numbers.
class RPS

    def __init__(self):
    #no parameters needed. 
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0

    def play_game(self):
        while True:
            player_choice = input("choose rock, paper or scissors ")
            computer_choice = random.choice(self.choices)

            print(f"player choice: {player_choice}")
            print(f"Computer choice: {computer_choice}")

            if player choice not in self.choices
                print("invalid choice try again")
            elif player choice == computer_choice
                print("its a tie")
            elif player choice == "rock" and computer choice == "scissor" win
                + 1
            elif player 