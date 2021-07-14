import random


def play():
    user_choice = input(
        "What is your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    comp_choice = random.choice(['r', 'p', 's'])

    if user_choice == comp_choice:
        return 'It\'s a tie!'

    if is_win(user_choice, comp_choice):
        return 'You won!'

    return 'You lost!'


def is_win(player, oponent):
    # r > s, p > r, s > p
    if (player == 'r' and oponent == 's') or (player == 'p' and oponent == 'r') or (player == 's' or player == 'p'):
        return True


print(play())
