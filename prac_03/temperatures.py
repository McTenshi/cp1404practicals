"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Convert temperatures between celsius and fahrenheit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = calculate_fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_fahrenheit_to_celsius(fahrenheit):
    """Calculate fahrenheit using celsius"""
    return 5 / 9 * (fahrenheit - 32)


def calculate_celsius_to_fahrenheit(celsius):
    """Calculate celsius using fahrenheit"""
    return celsius * 9.0 / 5 + 32


main()
