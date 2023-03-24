#Written by Shiven Desai
def WriteSales():
    outfile = open('sales.txt','a')

    # Get the salary and number of sales days from the user
    salary = float(input('Enter the salary: '))
    days = int(input('Enter the number of sales days: '))

    # Initialize the total sales to 0
    total_sales = 0

    # Get the sales for each day from the user and add them to the total sales
    for i in range(days):
        sale = float(input(f'Enter the sales for day {i+1}: '))
        total_sales += sale

    # If the total sales are greater than 1000, add 10% commission to the salary
    if total_sales > 1000:
        commission = 0.1 * salary
        salary += commission

    # Write the data to the file
    outfile.write(f"Salary: {salary}\n")
    outfile.write(f"Total Sales: {total_sales}\n")

    print('Data recorded')

    # Close the file
    outfile.close()


def ReadSales():
    infile = open('sales.txt', 'r')

    # Read the contents of the file and store them in a variable
    contents = infile.read()

    # Print the contents of the file to the console
    print(contents)

    # Close the file
    infile.close()


# Call the WriteSales function to write to the file
WriteSales()

# Call the ReadSales function to read from the file and print to the console
ReadSales()
