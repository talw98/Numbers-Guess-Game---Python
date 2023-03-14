import random


def guess(y):
    random_number = random.randint(1, y)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {y}: '))
        if guess < random_number:
            print('Sorry, please guess again. Number is low')
        elif guess > random_number:
            print('Sorry, please guess again. Number is high')

    print(
        f'Yahoooo!, congratulations, you guessed the number {random_number} correctly')


guess(10)
