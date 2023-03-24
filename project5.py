#Written by Shiven Desai
import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.geometry("300x180")
win.title("Customer Information")

lblLastname = tk.Label(win, text="Enter the Last Name:").grid(column=0, row=0)
lblFirstname = tk.Label(win, text="Enter the First Name:").grid(column=0, row=1)
lblAddress = tk.Label(win, text="Enter the Address:").grid(column=0, row=2)
lblCity = tk.Label(win, text="Enter the City:").grid(column=0, row=3)
lblState = tk.Label(win, text="Enter the State:").grid(column=0, row=4)
lblZip = tk.Label(win, text="Enter the Zip Code:").grid(column=0, row=5)

def write():
    text_file = open("Customers.txt", "a")
    content = LN.get() + ", " + FN.get() + ", " + Address.get() + ", " + City.get() + ", " + State.get() + ", " + Zip.get()
    text_file.write(content + "\n")
    text_file.close()
    messagebox.showinfo("Information", "Data Recorded")

def quit():
    messagebox.showinfo("Information", "Thank you...")
    win.destroy()

LN = tk.StringVar()
txtLastname = tk.Entry(win, width=12, textvariable=LN).grid(column=1, row=0)

FN = tk.StringVar()
txtFirstname = tk.Entry(win, width=12, textvariable=FN).grid(column=1, row=1)

Address = tk.StringVar()
txtAddress = tk.Entry(win, width=12, textvariable=Address).grid(column=1, row=2)

City = tk.StringVar()
txtCity = tk.Entry(win, width=12, textvariable=City).grid(column=1, row=3)

State = tk.StringVar()
txtState = tk.Entry(win, width=12, textvariable=State).grid(column=1, row=4)

Zip = tk.StringVar()
txtZip = tk.Entry(win, width=12, textvariable=Zip).grid(column=1, row=5)

btnSubmit = tk.Button(win, text="Submit", command=write).grid(column=0, row=6)
btnQuit = tk.Button(win, text="Quit", command=quit).grid(column=1, row=6)
btnTransfer = tk.Button(win, text="Transfer", command=write).grid(column=2, row=6)

win.mainloop()
