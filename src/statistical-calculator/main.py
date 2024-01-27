import statistics as st
import sys

def user():
    print("==========================================")
    data = input("Enter Data, (example: 2,4,5,1) \t: ")

    # Convert the input string into a list of integers
    data_list = [int(x) for x in data.split(",")]

    print("==========================================")
    print(data_list)
    print("")

    while True:
        print("What would you like to calculate?")
        print("1. Mean")
        print("2. Median")
        print("3. Mode")
        print("4. Variance")
        print("5. Standard Deviation")
        inp = input("Enter Number \t\t\t: ")
        print("==========================================")

        if inp == "1":
            mean = sum(data_list) / len(data_list)
            print(f"Mean of the Data Above is \t: {mean:.2f}")

        elif inp == "2":
            median = st.median(data_list)
            print(f"Median of the Data Above is \t: {median:.2f}")

        elif inp == "3":
            try:
                mode = st.mode(data_list)
                print(f"Mode of the Data Above is \t: {mode:.2f}")
            except st.StatisticsError:
                print("No Mode in the Data")

        elif inp == "4":
            variance = st.variance(data_list)
            print(f"Variance of the Data Above is \t: {variance:.2f}")

        elif inp == "5":
            std_dev = st.stdev(data_list)
            print(f"Standard Deviation of the Data Above is \t: {std_dev:.2f}")

        elif inp == "exit":
            sys.exit()
        else:
            print("Invalid Choice, Please Enter Again")

        print("==========================================")

user()
