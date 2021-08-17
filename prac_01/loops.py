for i in range(1, 21, 2):
    print(i, end=' ')
print()

# loop a
for i in range(0, 101, 10):
    print(i, end=" ")
print()

# loop b
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# loop c
number_of_stars = int(input("Number of stars: "))
for i in range(0, number_of_stars):
    print("*",end="")
print()

# loop d
number_of_stars = int(input("Number of stars: "))
for i in range(0, number_of_stars):
    for j in range(0, i + 1):
        print("*", end="")
    print()
print()