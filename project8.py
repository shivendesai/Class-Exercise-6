#Written by Shiven Desai
import random

# Generate a list of 10 random numbers between 1 and 10
random_numbers = [random.randint(1, 10) for _ in range(10)]

# Write the random numbers to a file named 'random_numbers.txt'
with open('random_numbers.txt', 'w') as outfile:
    for number in random_numbers:
        outfile.write(str(number) + '\n')

# Read the contents of the 'random_numbers.txt' file and print them to the console
with open('random_numbers.txt', 'r') as infile:
    contents = infile.read()
    print(contents)
