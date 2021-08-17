"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
        A ValueError will occur when a character other than a number is entered.
2. When will a ZeroDivisionError occur?
        A ZeroDivisionError will occur when you enter a zero for the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
        You could make it loop and re-prompt the user when they enter a zero into the denominator.
"""

valid_input = False
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        valid_input = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished.")
