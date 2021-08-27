"""
List Exercises Programs

"""

# # 1. Basic list operations
# numbers = []
# for i in range(0, 5):
#     number = int(input("Number: "))
#     numbers.append(number)
# print(f"The first number is {numbers[0]}")
# print(f"The last number is {numbers[-1]}")
# numbers.sort()
# print(f"The smallest number is {numbers[0]}")
# print(f"The largest number is {numbers[-1]}")
# average = sum(numbers) / len(numbers)
# print(f"The average of the numbers is {average}")

# 2. Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username: ")
if username in usernames:
    print("Access Granted")
else:
    print("Access Denied")
