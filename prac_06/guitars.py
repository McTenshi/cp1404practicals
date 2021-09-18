"""
CP1404 - Practical
Joshua Quidlat
Guitars
"""
from guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    name = input("Name: ")

print(guitars)
print(guitars[0])
