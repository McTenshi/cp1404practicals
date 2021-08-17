"""CP1404 Practical 2 - Files"""

# 1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
name = input("What is your name: ")
out_file = open('name.txt', 'w')
print(name, file=out_file)
out_file.close()

# 2. Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).

in_file = open('name.txt', 'r')
name = in_file.read().strip()
in_file.close()
print(f"Your name is {name}")

# 3. Write code that opens "numbers.txt", reads only the first two numbers and
# adds them together then prints the result, which should be... 59.

in_file = open('numbers.txt', 'r')
first_number = int(in_file.readline())
second_number = int(in_file.readline())
in_file.close()
print(first_number + second_number)

# Now write a fourth block of code that prints the total for all lines in
# numbers.txt or a file with any number of numbers.

in_file = open('numbers.txt', 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(f"The total value for the numbers in {in_file.name} is {total}.")
