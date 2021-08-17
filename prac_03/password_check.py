"""
Password Check Program
"""

MINIMUM_LENGTH = 6


def main():
    password = get_password()
    while len(password) < MINIMUM_LENGTH:
        print(f"Error. Password not longer than {MINIMUM_LENGTH} characters.")
        password = get_password()
    display_stars(password)


def display_stars(password):
    print("*" * len(password))


def get_password():
    return input("Enter a password: ")


main()
