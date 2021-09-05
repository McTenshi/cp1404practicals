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
        if confirmation != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} {email}")


def get_name_from_email(email):
    first_part = email.split("@")[0]
    name_parts = first_part.split(".")
    name = " ".join(name_parts).title()
    return name

main()
