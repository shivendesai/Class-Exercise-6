#Written by Shiven Desai
# Ask the user for their first name, last name, and age
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

# Write the information to a file
with open("user_info.txt", "w") as file:
    file.write(f"First Name: {first_name}\n")
    file.write(f"Last Name: {last_name}\n")
    file.write(f"Age: {age}\n")

# Read the information from the file
with open("user_info.txt", "r") as file:
    contents = file.read()
    print(contents)
