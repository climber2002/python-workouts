import random

def guessing_name():
    number = random.randint(0, 100)
    while user_input := input('Make your guess:'):
        user_number = int(user_input)
        if number == user_number:
            print('Congrats, you guessed right!')
            break
        elif number > user_number:
            print('Too low')
        else:
            print('Too high')

guessing_name()