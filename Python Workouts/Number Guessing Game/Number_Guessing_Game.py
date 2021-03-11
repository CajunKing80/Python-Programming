from random import randint

def guessing_game():
    answer = randint(0,1000)

    while True:
        user_guess = int(input('Pick a Number, 1 - 1000: '))

        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break 

        elif user_guess < answer: 
            print(f'Your guess of {user_guess} is too low!')

        else: 
            print(f'Your guess of {user_guess} is too high!')

guessing_game()