import random

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?', '<', '>', '.', ',', '/', '~']
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'

try:
    password_length = int(input("Enter password length (8-16)\t: "))

    while not (8 <= password_length <= 16):
        print('Please enter a number between 8 and 16')
        password_length = int(input("Enter password length (8-16)\t: "))

    all_characters = symbols + list(lowercase) + list(uppercase) + list(numbers)

    password = ''.join(random.choice(all_characters) for _ in range(password_length))

    print("Generated password\t\t:", password)

except ValueError:
    print('Invalid input')
