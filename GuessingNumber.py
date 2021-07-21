print('Number Guessing Game')
print('Guess a Number (between 1 and 9):')

import random
number = random.randint(1,9)
print(number)

for i in range(0,5,1):
    userInput = int(input('Enter your Guess :- '))
    if userInput < 3:
        print('Your guess was too low: Guess a number higher than 3')
    elif userInput < 5:
        print('Your guess was too low: Guess a number higher than 5')
    elif userInput < 7:
        print('Your guess was too low: Guess a number higher than 7')
    if userInput == number:
        print('Congratulations !\nYou Won !!')
