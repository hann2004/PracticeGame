import random 

# Rock, Paper, Scissor game
def get_choices():
    option = ["Rock", "Paper", "Scissor"]
    p_choice = input("Enter your choice(Rock, Paper, Scissor) ").capitalize()
    while p_choice not in option:
        p_choice = input("Invalid choice try again!").capitalize()
    c_choice = random.choice(option)
    return {"player": p_choice, "computer": c_choice}

def check_win(player, computer):
    print(f"\nYou chose {player}, The computer chose {computer}")
    if player == computer:
        return "it's a tie"
    elif player == "Rock":
        if computer == "Scissor":
            return ("Rock smash a scissor, U Win!")
        else:
            return("Paper covers a rock, U lose!")  
    elif player == "Paper":
        if computer == "Rock":
            return ("Paper covers a rock, U Win!")
        else:
            return("Scissor cuts a paper, U lose!")
    elif player == "Scissor":
        if computer == "Paper":
            return ("Scissor cuts a paper, U Win!")
        else:
            return("Rock smash a scissor, U lose!")
    
def play_game():
    while True:
        choices = get_choices()
        result = check_win(choices["player"], choices["computer"])
        print(result)
        play_again = input("Do you want to play again?? y/n: ").lower()
        if play_again != 'y':
            break

play_game()