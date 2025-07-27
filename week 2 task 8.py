# Temperature Converter
try:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

    f_input = float(input("Enter temperature in Fahrenheit: "))
    c_output = (f_input - 32) * 5/9
    print(f"{f_input}°F = {c_output}°C")

except ValueError:
    print("Invalid input! Please enter a number.")
