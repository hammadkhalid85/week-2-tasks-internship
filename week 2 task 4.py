# Data Type Tester
value = input("Enter any value: ")

# Python reads input as string, try to guess type
try:
    if "." in value:
        val = float(value)
        print("You entered a float!")
    else:
        val = int(value)
        print("You entered an integer!")
except ValueError:
    print("You entered a string!")
