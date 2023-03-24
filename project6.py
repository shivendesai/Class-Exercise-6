#Written by Shiven Desai
import tkinter as tk

def write_numbers():
    num1 = int(num1_entry.get())
    num2 = int(num2_entry.get())
    num3 = int(num3_entry.get())

    sum = num1 + num2 + num3
    avg = sum/3

    with open('numbers.txt','a') as outfile:
        outfile.write("The 1st number is " + str(num1) + '\n')
        outfile.write("The 2nd number is " + str(num2) + '\n')
        outfile.write("The 3rd number is " + str(num3) + '\n')
        outfile.write("The average of the numbers is " + str(avg) + '\n')
        outfile.write("The total sum of the numbers is " + str(sum) + '\n')

    status_label.config(text='Data recorded!')

window = tk.Tk()
window.title('Enter 3 Numbers')

num1_label = tk.Label(window, text='Enter Number 1:')
num1_label.grid(row=0, column=0)

num1_entry = tk.Entry(window)
num1_entry.grid(row=0, column=1)

num2_label = tk.Label(window, text='Enter Number 2:')
num2_label.grid(row=1, column=0)

num2_entry = tk.Entry(window)
num2_entry.grid(row=1, column=1)

num3_label = tk.Label(window, text='Enter Number 3:')
num3_label.grid(row=2, column=0)

num3_entry = tk.Entry(window)
num3_entry.grid(row=2, column=1)

submit_button = tk.Button(window, text='Submit', command=write_numbers)
submit_button.grid(row=3, column=0)

status_label = tk.Label(window, text='')
status_label.grid(row=3, column=1)

window.mainloop()
