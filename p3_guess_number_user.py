import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} too high(h), too low(l), or correct(c)?")
        if feedback == 'h':
            high -= 1
        elif feedback == 'l':
            low += 1

    print(f"Yay, the computer guessed the number correctly! {guess}")


computer_guess(10)
