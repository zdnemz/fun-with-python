<<<<<<< HEAD
import random

print('=' * 30)
print('   Rock Paper Scissors')
print('=' * 30 + '\n')

choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)

try:
    user_input = int(input('1. Rock\n2. Paper\n3. Scissors\nEnter your choice (as a number): '))

    if 1 <= user_input <= 3:
        user_choice = choices[user_input - 1]

        if computer_choice == user_choice:
            result = 'It\'s a tie!'
        elif (computer_choice == 'rock' and user_choice == 'paper') or (computer_choice == 'paper' and user_choice == 'scissors') or (computer_choice == 'scissors' and user_choice == 'rock'):
            result = 'You win!'
        else:
            result = 'You lose!'

        print(f'The computer chose {computer_choice}, so: {result}')
    else:
        print('Invalid input. Please enter a number between 1 and 3.')
except ValueError:
    print('Please enter only numbers.')
=======
import random

print('=' * 30)
print('   Rock Paper Scissors')
print('=' * 30 + '\n')

choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)

try:
    user_input = int(input('1. Rock\n2. Paper\n3. Scissors\nEnter your choice (as a number): '))

    if 1 <= user_input <= 3:
        user_choice = choices[user_input - 1]

        if computer_choice == user_choice:
            result = 'It\'s a tie!'
        elif (computer_choice == 'rock' and user_choice == 'paper') or (computer_choice == 'paper' and user_choice == 'scissors') or (computer_choice == 'scissors' and user_choice == 'rock'):
            result = 'You win!'
        else:
            result = 'You lose!'

        print(f'The computer chose {computer_choice}, so: {result}')
    else:
        print('Invalid input. Please enter a number between 1 and 3.')
except ValueError:
    print('Please enter only numbers.')
>>>>>>> a8d7b99dbb3481e966498f29ecda8eb9c74633d5
