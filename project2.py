#Written by Shiven Desai
def WriteNumbers():
    outfile = open('numbers.txt','a')

    num1 = int(input('enter #1 '))
    num2 = int(input('enter #2 '))
    num3 = int(input('enter #3 '))

    sum = num1 + num2 + num3
    avg = sum/3

    outfile.write("the 1st number is " + str(num1) + '\n')
    outfile.write("the 2nd number is " + str(num2) + '\n')
    outfile.write("the 3rd number is " + str(num3) + '\n')
    outfile.write("the avg number is " + str(avg) + '\n')
    outfile.write("the total number is " + str(sum) + '\n')

    print('data recorded')

    # Close the file
    outfile.close()

def ReadNumbers():
    infile = open('numbers.txt', 'r')

    # Read the contents of the file and store them in a variable
    contents = infile.read()

    # Print the contents of the file to the console
    print(contents)

    # Close the file
    infile.close()

# Call the WriteNumbers function to write to the file
WriteNumbers()

# Call the ReadNumbers function to read from the file and print to the console
ReadNumbers()
