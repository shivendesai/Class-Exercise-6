#Written by Shiven Desai
def main():
    num_emps = int(input('Enter the number of employee records: '))

    emp_file = open('employees.txt', 'w')

    for count in range(1, num_emps+1):
        print('Enter data for employee #', count)

        name = input('Name: ')
        id_num = input('ID NUMBER: ')
        dept = input('DEPARTMENT: ')

        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

        print()

    emp_file.close()
    print('Recorded')

    # Open the employees.txt file for reading
    emp_file = open('employees.txt', 'r')

    # Read the contents of the file
    contents = emp_file.read()

    # Print the contents to the console
    print('Contents of employees.txt:')
    print(contents)

    # Close the file
    emp_file.close()


main()
