def check_password_strength(password):
    symbols = "!@#$%^&*()?<>.,/~"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"

    conditions = [
        any(char in symbols for char in password),
        any(char in lowercase for char in password),
        any(char in uppercase for char in password),
        any(char in numbers for char in password),
    ]

    if len(password) < 8 or len(password) > 16:
        return "Password must have a length between 8 and 16 characters."

    if all(conditions) and 8 <= len(password) <= 16:
        return "Strong"
    elif any(conditions):
        return "Medium"
    else:
        return "Weak"


def main():
    password_user = input("Enter your password\t: ")
    result = check_password_strength(password_user)
    print(result)


if __name__ == "__main__":
    main()
