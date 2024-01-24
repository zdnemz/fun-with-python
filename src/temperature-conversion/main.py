print(60 * "=")
print(f"\n{20 * '-'}Temperature Converter{19 * '-'}\n")
print(60 * "=")

while True:
    print("1. Celsius\n2. Fahrenheit\n3. Reamur\n4. Kelvin")
    print(60 * "=")

    scale_choice = input(
        "Choose the temperature scale to convert (1-4),\nType 'exit' to exit the program\t\t\t: "
    )

    if scale_choice.lower() == "exit":
        print("Exiting the program.")
        break

    elif scale_choice.isdigit() and 1 <= int(scale_choice) <= 4:
        try:
            temperature_input = input("Enter the temperature to convert\t\t: ")
            print(60 * "=")

            temperature_value = float(temperature_input)

            if int(scale_choice) == 1:
                celsius = temperature_value
                fahrenheit = (celsius * 9 / 5) + 32
                reamur = celsius * 4 / 5
                kelvin = celsius + 273.15
            elif int(scale_choice) == 2:
                fahrenheit = temperature_value
                celsius = (fahrenheit - 32) * 5 / 9
                reamur = celsius * 4 / 5
                kelvin = celsius + 273.15
            elif int(scale_choice) == 3:
                reamur = temperature_value
                celsius = reamur * 5 / 4
                fahrenheit = (celsius * 9 / 5) + 32
                kelvin = celsius + 273.15
            elif int(scale_choice) == 4:
                kelvin = temperature_value
                celsius = kelvin - 273.15
                fahrenheit = (celsius * 9 / 5) + 32
                reamur = celsius * 4 / 5

            print(f"If {temperature_value} is converted:")
            print(f"1. Celsius\t: {celsius:.2f} °C")
            print(f"2. Fahrenheit\t: {fahrenheit:.2f} °F")
            print(f"3. Reamur\t: {reamur:.2f} °R")
            print(f"4. Kelvin\t: {kelvin:.2f} K")
            print(60 * "=")

        except ValueError:
            print("Please enter a valid temperature.")
            print(60 * "=")

    else:
        print("Please choose a valid temperature scale.")
        print(60 * "=")
