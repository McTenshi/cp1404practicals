"""
CP1404 - Practical
Joshua Quidlat
Guitar test
"""
from guitar import Guitar


guitar_01 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar_02 = Guitar("Another Guitar", 2020, 12345.67)

print("guitar_01 get_age() - expect 99. got {}".format(guitar_01.get_age()))
print("guitar_02 get_age() - expect 1. got {}".format(guitar_02.get_age()))
print("guitar_01 is_vintage() - expect True. got {}".format(guitar_01.is_vintage()))
print("guitar_02 is_vintage() - expect False. got {}".format(guitar_02.is_vintage()))
print(guitar_01)
print(guitar_02)