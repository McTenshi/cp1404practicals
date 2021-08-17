"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """Get user score and determine grade using it"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    grade = determine_grade(score)
    print(f"Your grade is {grade}.")
    random_score = random.randint(0, 100)
    grade = determine_grade(random_score)
    print(f"Random score is {random_score}. Grade is {grade}.")


def determine_grade(score):
    """Determine grade from a score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
