"""
1402 - Practical Joshua Quidlat
Hex Colours
"""

HEX_COLOURS = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine" : "#7fffd4", "azure": "#f0ffff",
               "beige": "#f5f5dc", "black": "#000000", "blue": "#0000ff", "brown": "#a52a2a", "cyan": "#00ffff",
               "green": "#00ff00"}

choice = input("Colour: ").lower()
while choice != "":
    if choice not in HEX_COLOURS:
        print("Invalid choice.")
    else:
        print(f"{choice} is {HEX_COLOURS[choice]}")
    choice = input("Colour: ").lower()