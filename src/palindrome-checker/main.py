import sys


def isPalindrom(text):
    text = text.lower()
    return text == text[::-1]


print("===========================================")
print("|           PALINDROME CHECKER            |")
print("===========================================")

while True:
    text = input("Input Text \t\t: ")
    if isPalindrom(text):
        print(f"'{text}' is a palindrome")
    else:
        print(f"'{text}' is not a palindrome")

    print("===========================================")

    restart = ""
    while restart.lower() not in ["y", "n"]:
        restart = input("Do you want to restart the program? (y/n) : ")
        if restart.lower() == "y":
            print("Alright, let's restart.")
            print("===========================================")
            break
        elif restart.lower() == "n":
            print("Okay, I will exit now.")
            print("===========================================")
            sys.exit(0)
        else:
            print("Sorry, I didn't understand. Could you please try again?")
            print("===========================================")
