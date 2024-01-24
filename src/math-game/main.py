import sys

def display_game_title():
    # Display the game title
    game_title = "MATH GAME".center(35, "=")
    print("'" + game_title + "'")

def preprocess_input(input_str):
    # Preprocess the user input for math operations
    input_str = input_str.replace(" ", "")
    input_str = input_str.replace("x", "*") 
    input_str = input_str.replace("^", "**") 
    return input_str

def evaluate_math_operation(input_str):
    # Evaluate the math operation and return the result.
    try:
        result = float(eval(input_str))
        return result
    except:
        return None

def play_math_game():
    # Play the math game.
    while True:
        display_game_title()

        user_input = input("(example: 2 + 3 * 5)\nEnter a math operation\t: ")
        processed_input = preprocess_input(user_input)

        result = evaluate_math_operation(processed_input)

        if result is not None:
            user_answer = float(input('What is Your Answer\t: '))
            print('=========================================')
            if user_answer == result:
                print('Correct Answer!')
            else:
                print(f'Wrong Answer, the correct answer is {result}')
        else:
            print("Invalid math operation.")

        restart = ''
        while restart.lower() not in ['y', 'n']:
            print('=========================================')
            restart = input('Do you want to play again? (y/n): ')
            if restart.lower() == 'y':
                print('Alright then.')
                break
            elif restart.lower() == 'n':
                print('Okay, I will stop.')
                sys.exit(0)
            else:
                print('Sorry, I don\'t understand. Can you please repeat?')

if __name__ == "__main__":
    play_math_game()
