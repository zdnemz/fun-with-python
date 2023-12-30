# Password Strength Checker

This Python script checks the strength of a user-provided password based on certain criteria, categorizing it as either "Strong," "Medium," or "Weak."

## Features

- Validates the password based on the following criteria:

  - Contains at least one symbol (!, @, #, $, %, ^, &, \*, (, ), ?, <, >, ., ,, /, ~)
  - Contains at least one lowercase letter
  - Contains at least one uppercase letter
  - Contains at least one number
  - Has a length between 8 and 16 characters

- The script provides feedback on the strength of the password.

## Example Usage

### Run the script:

```bash
python main.py
```

### Input and Output

```bash
Enter your password     : mypassword
Medium

Enter your password     : test
Password must have a length between 8 and 16 characters.
```

The script will output whether your password is "Strong," "Medium," or "Weak" based on the defined criteria.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests.

## License

This project is licensed under the [MIT License](/LICENSE).
