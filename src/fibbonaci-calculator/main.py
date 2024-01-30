import sys

while True:
    print("=======================================================")
    total = 0

    def fibonacci(n):
        global total
        if n <= 1:
            total += n
            return n
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
            total += result
            return result
    
    n = int(input('Enter a number \t\t\t\t\t: '))
    result = fibonacci(n)

    print("=======================================================")
    print(f'The {n}th Fibonacci number is\t\t\t: {result}')
    print(f'The sum of Fibonacci numbers up to {n} is\t: {total}')
    print("=======================================================")

    restart = ''
    while restart.lower() not in ['y', 'n']:
        restart = input('Do you want to restart the program? (y/n): ')
        if restart.lower() == 'y':
            print('Alright, let\'s restart.')
            break
        elif restart.lower() == 'n':
            print('Okay, I will exit now.')
            print("=======================================================")
            sys.exit(0)
        else:
            print('Sorry, I didn\'t understand. Could you please try again?')