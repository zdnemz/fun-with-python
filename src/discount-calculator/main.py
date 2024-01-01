import sys

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

while True:
    discount_price = input('Enter the discounted price: ')
    initial_price = input('Enter the original price: ')

    if is_float(discount_price) and is_float(initial_price):
        initial_price = float(initial_price)
        discount_price = float(discount_price)
        discount_amount = initial_price - discount_price
        discount_percentage = (discount_amount / initial_price) * 100

        print(f'The total discount is: {discount_percentage:.2f}%')

    else:
        print('Please enter valid numbers!')

    restart = ''
    while restart.lower() not in ['y', 'n']:
        restart = input('Do you want to restart the program? (y/n): ')
        if restart.lower() == 'y':
            print('Alright, let\'s restart.')
            break
        elif restart.lower() == 'n':
            print('Okay, I will exit now.')
            sys.exit(0)
        else:
            print('Sorry, I didn\'t understand. Could you please try again?')
