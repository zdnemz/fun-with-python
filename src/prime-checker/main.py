while True:
    print('\nPrime Checker')
    print('================================')

    def prima(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    try:
        angka = int(input('Input Number \t: '))
        if angka >= 0:
            if prima(angka):
                print(f'\n{angka} is a prime number')
            else:
                print(f'\n{angka} is not a prime number')
        else:
            print(f'\n{angka} is not a valid number')
            continue

    except ValueError:
        print('\nInput must be a number')
    