import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# Create database and table
conn = sqlite3.connect('bmi.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS BMI (
             id INTEGER PRIMARY KEY,
             weight REAL,
             height REAL,
             bmi REAL
             )''')
conn.commit()

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def add_data_to_db(weight, height, bmi, category):
    c.execute("INSERT INTO BMI (weight, height, bmi) VALUES (?, ?, ?)", (weight, height, bmi))
    conn.commit()

def plot_bmi_trends():
    c.execute("SELECT weight, height, bmi FROM BMI ORDER BY id ASC")
    data = c.fetchall()
    weights, heights, bmis = zip(*data)
    
    fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 6))
    fig.suptitle('BMI Trends Over Time')
    ax1.plot(weights, label='Weight (kg)')
    ax1.set_ylabel('Weight (kg)')
    ax2.plot(bmis, label='BMI')
    ax2.set_ylabel('BMI')
    ax2.set_xlabel('Data Points')
    ax1.legend()
    ax2.legend()
    plt.show()

def calculate_and_store():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        bmi_label.config(text=f"BMI: {bmi}")
        category_label.config(text=f"Category: {category}")

        add_data_to_db(weight, height, bmi, category)

        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi}\nYou are classified as: {category}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter valid numbers.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def view_historical_data():
    plot_bmi_trends()

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("800x600")

weight_label = tk.Label(root, text="Weight (kg):", width=20, height=2)
weight_label.grid(row=0, column=0, padx=10, pady=10)

weight_entry = tk.Entry(root, width=20, bd=5)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

height_label = tk.Label(root, text="Height (m):", width=20, height=2)
height_label.grid(row=1, column=0, padx=10, pady=10)

height_entry = tk.Entry(root, width=20, bd=5)
height_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_and_store, width=20, height=2)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

bmi_label = tk.Label(root, text="BMI: ", width=20, height=2)
bmi_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

category_label = tk.Label(root, text="Category: ", width=20,height=2)
category_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

view_historical_button = tk.Button(root, text="View Historical Data", command=view_historical_data)
view_historical_button.grid(row=5, column=0, columnspan=2)

root.mainloop()
