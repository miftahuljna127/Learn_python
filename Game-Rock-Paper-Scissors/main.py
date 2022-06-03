from random import random
import random

print("Game Rock(R), Paper(P), Scissors(S)")

while True:
    # Choice input user
    choice_user = input("Enter your option (R, P or S) : ")

    # Choice random computer
    # actions = ["R, P, S"]
    choice_comp = random.choice(("R", "P", "S"))

    # Logic win lose
    result = ' '
    if choice_user == choice_comp:
        result = 'TIE!'
    elif choice_user == 'R':
        if choice_comp == 'S':
            result = 'WIN'
        else:
            result = 'LOSE'
    elif choice_user == 'P':
        if choice_comp == 'R':
            result = 'WIN'
        else:
            result = 'LOSE'
    elif choice_user == 'S':
        if choice_comp == 'P':
            result = 'WIN'
        else:
            result = 'LOSE'
    else:
        result = "enter wrong choice, please check you spelling"

    # Message output frPom choice
    print(
        f"You choose {choice_user}, computer choose {choice_comp}. \nYou {result}"
    )

    # Question for play again
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
