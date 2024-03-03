import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    password_length = length_scale.get()
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    if not (use_lowercase or use_uppercase or use_digits or use_symbols):
        messagebox.showerror("Error", "Please select at least one option.")
        return

    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = "".join(random.choices(characters, k=password_length))

    pyperclip.copy(password)

    messagebox.showinfo("Generated Password", f"Password: {password}\n\nPassword copied to clipboard.")

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0)

length_scale = tk.Scale(root, from_=6, to=30, orient=tk.HORIZONTAL, length=200)
length_scale.set(12)
length_scale.grid(row=0, column=1)

lowercase_var = tk.BooleanVar()
lowercase_var.set(True)
lowercase_check = tk.Checkbutton(root, text="Include lowercase", variable=lowercase_var)
lowercase_check.grid(row=1, column=0, columnspan=2, sticky=tk.W)

uppercase_var = tk.BooleanVar()
uppercase_var.set(True)
uppercase_check = tk.Checkbutton(root, text="Include uppercase", variable=uppercase_var)
uppercase_check.grid(row=2, column=0, columnspan=2, sticky=tk.W)

digits_var = tk.BooleanVar()
digits_var.set(True)
digits_check = tk.Checkbutton(root, text="Include digits", variable=digits_var)
digits_check.grid(row=3, column=0, columnspan=2, sticky=tk.W)

symbols_var = tk.BooleanVar()
symbols_var.set(True)
symbols_check = tk.Checkbutton(root, text="Include symbols", variable=symbols_var)
symbols_check.grid(row=4, column=0, columnspan=2, sticky=tk.W)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2)

root.mainloop()
