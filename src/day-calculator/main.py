import datetime as dt
import sys

def date_converter(days):
    years = abs(days // 365.25)
    months = abs((days % 365.25) // 30)
    remaining_days = abs((days % 365.25) % 30)
    return f"{int(years)} years, {int(months)} months, {int(remaining_days)} days"

def get_user_input():
    try:
        day = int(input("Enter day\t: "))
        month = int(input("Enter month\t: "))
        year = int(input("Enter year\t: "))
        return dt.date(year, month, day)
    except ValueError:
        print("Input must be a number. Please try again.")
        return get_user_input()

def main():
    while True:
        print("\n" + "="*45 + " DAY CALCULATOR " + "="*45 + "\n")
        print("Enter Day, Month, and Year")

        target_date = get_user_input()
        today = dt.date.today()

        print("\n" + "="*45 + "\n")
        restart_input = input(f"Is {target_date} correct?\t: ")

        if restart_input.lower() in ["no", "n"]:
            print("You can input it again.")
            continue

        elif restart_input.lower() in ["yes", "y"]:
            days_difference = (today - target_date).days
            print("\n" + "="*45 + "\n")

            if days_difference < 0:
                print(f"Coming up\t\t\t: {-days_difference} days from now")
                print(f"If Converted, Approximately\t: {date_converter(-days_difference)} days from now")
            else:
                print(f"Already passed\t\t\t: {days_difference} days")
                print(f"If Converted, Approximately\t: {date_converter(days_difference)} days ago")

        else:
            print("Sorry, I did not understand. Can you please repeat?")
            continue

        restart_main_input = input("\nDo you want to calculate again?\t: ")

        if restart_main_input.lower() in ["no", "n"]:
            print("Okay, I will stop.")
            sys.exit(0)
        elif restart_main_input.lower() not in ["yes", "y"]:
            print("Sorry, I did not understand. Can you please repeat")

if __name__ == "__main__":
    main()
