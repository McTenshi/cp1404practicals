"""
Password Check Program
"""

MINIMUM_LENGTH = 6

password = input("Enter a password: ")
while len(password) < MINIMUM_LENGTH:
    print(f"Error. Password not longer than {MINIMUM_LENGTH} characters.")
    password = input("Enter a password: ")
print("*"*len(password))
