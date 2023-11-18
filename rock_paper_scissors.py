# create a rock, paper, scissors game
# take input selection from the user
# generate random selection
# compare the users selection and random selection
# print winner

import random
import sys

player_score = 0
opponent_score = 0

def main():

    while True: # this loop lets the user repeatedly play they game until they chose to exit
        player_choice = user_choice() # set return of user_choice func to player_choice variable for later use
        op = rand_choice() # set return of rand_choice fund to op variable for later use
        compare(player_choice, op) # passes player_choice and op variable into compare func
    while True:
        player_choice = user_choice()
        op = rand_choice()
        compare(player_choice, op)

def user_choice():
    print("Choose 1, 2 or 3, or select 4 to exit:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")
    player_choice = int(input(">")) # get user input
    # todo handle exceptions
    player_choice = int(input(">"))
    if player_choice == 4:
        print("You quit the game")
        sys.exit()
    else:
        return player_choice

def rand_choice():
    op = random.choice([1, 2, 3])
    return op

def display_choices(player_choice, op):
    choice_dict = {
        1:"Rock",
        2:"Paper",
        3:"Scissors"
    }

# print each player's selection
    print(f">> You chose: {choice_dict[player_choice]}<<")
    print(f">>Opponent chose: {choice_dict[op]}<<\n")



def compare(player_choice, op):
    global player_score, opponent_score

    display_choices(player_choice, op)

    if player_choice == op:
        print("**It's a draw!**\n")
    elif player_choice == 1 and op == 3:
        player_score += 1
        print("**Rock beats Scissors, you win!**\n")
    elif player_choice == 2 and op == 1:
        player_score += 1
        print("**Paper beats Rock, you win!**\n")
    elif player_choice == 3 and op == 2:
        player_score += 1
        print("**Scissors beat paper, you win!**\n")
    else:
        opponent_score += 1
        print("**You Lose!**\n")

    print(f"#######################################")
    print(f"## Your Score: {player_score} | Opponent Score: {opponent_score} ##")
    print(f"#######################################\n")


main()




