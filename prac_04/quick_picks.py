"""
1404 practical
Quick Picks Program
"""
import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6

number_of_quick_picks = int(input("How many quick picks? "))
while number_of_quick_picks < 0:
    print("Invalid number")
    number_of_quick_picks = int(input("How many quick picks? "))

for i in range(0, number_of_quick_picks):
    quick_pick = []
    for j in range(0, NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in quick_pick:
            number = random.randint(MINIMUM, MAXIMUM)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join("{:2}".format(number) for number in quick_pick))
