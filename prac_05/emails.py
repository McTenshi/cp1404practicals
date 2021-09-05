"""
1404 - Practical Joshua Quidlat
emails program

"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/N) ").upper()
        if confirmation != "Y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")


def get_name_from_email(email):
    first_part = email.split("@")
    name_parts = first_part.split(".")
    name = " ".join(name_parts).title()
    return name
