#Written by Shiven Desai
def main():
    try:
        outfile = open('grades.txt', 'a')
        
        # Get user input
        name = input('Enter full name: ')
        midterm = float(input('Enter grade for midterm exam: '))
        final = float(input('Enter grade for final exam: '))
        
        # Calculate average grade
        avg = (midterm + final) / 2
        
        # Determine letter grade
        if avg >= 90:
            letter_grade = 'A'
        elif avg >= 80:
            letter_grade = 'B'
        elif avg >= 70:
            letter_grade = 'C'
        elif avg >= 60:
            letter_grade = 'D'
        else:
            letter_grade = 'F'
        
        # Write data to file
        outfile.write(f'{name}, {midterm}, {final}, {avg}, {letter_grade}\n')
        outfile.close()
        
        print('Data recorded.')
        
        # Read data from file and display to console
        infile = open('grades.txt', 'r')
        print('Grade report:')
        print(infile.read())
        infile.close()
    except ValueError:
        print('Invalid input. Please enter a valid number.')
    except:
        print('An error occurred.')
        
main()
