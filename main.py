import tkinter as tk
import random
import string

def generate_easy_password():
    length = password_length.get()

    if length.isdigit():
        length = int(length)
        if length > 0:
            password = ''.join(random.choices(string.digits, k=length))
            display_generated_password(password, "Easy")
        else:
            display_error("Please enter a valid password length (greater than 0) for Easy.")
    else:
        display_error("Please enter a valid number for password length in Easy.")

def generate_medium_password():
    length = password_length.get()

    if length.isdigit():
        length = int(length)
        if length > 0:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            display_generated_password(password, "Medium")
        else:
            display_error("Please enter a valid password length (greater than 0) for Medium.")
    else:
        display_error("Please enter a valid number for password length in Medium.")

def generate_hard_password():
    length = password_length.get()

    if length.isdigit():
        length = int(length)
        if length > 0:
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
            display_generated_password(password, "Hard")
        else:
            display_error("Please enter a valid password length (greater than 0) for Hard.")
    else:
        display_error("Please enter a valid number for password length in Hard.")

def display_generated_password(password, complexity):
    password_display.config(state=tk.NORMAL)
    password_display.delete(1.0, tk.END)
    password_display.insert(tk.END, f"Generated Password ({complexity}): {password}")
    password_display.config(state=tk.DISABLED)

def display_error(error_message):
    password_display.config(state=tk.NORMAL)
    password_display.delete(1.0, tk.END)
    password_display.insert(tk.END, error_message)
    password_display.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a label and entry for password length input
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

password_length = tk.Entry(root)
password_length.pack()

# Create buttons for different complexity levels
easy_button = tk.Button(root, text="Generate Easy Password", command=generate_easy_password)
easy_button.pack()

medium_button = tk.Button(root, text="Generate Medium Password", command=generate_medium_password)
medium_button.pack()

hard_button = tk.Button(root, text="Generate Hard Password", command=generate_hard_password)
hard_button.pack()

# Create a text widget to display the generated password
password_display = tk.Text(root, height=10, width=40)
password_display.config(state=tk.DISABLED)
password_display.pack()

# Start the main loop
root.mainloop()
