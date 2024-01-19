import tkinter as tk
from tkinter import simpledialog

def calculate_sla_credit(total_minutes, minutes_unavailable):
    # Calculate availability and SLA credit
    availability = (total_minutes - minutes_unavailable) / total_minutes
    sla_credit = minutes_unavailable / total_minutes
    return sla_credit * 100, availability * 100

def on_submit():
    total_minutes = int(total_minutes_entry.get())
    minutes_unavailable = int(minutes_unavailable_entry.get())
    sla_credit, availability = calculate_sla_credit(total_minutes, minutes_unavailable)
    result_label.config(text=f"SLA Credit Percentage: {sla_credit}\nAvailability Percentage: {availability}")

# Create the main window
root = tk.Tk()
root.title("SLA Calculator")

# Create and pack widgets
total_minutes_label = tk.Label(root, text="Enter total minutes in the month:")
total_minutes_label.pack()

total_minutes_entry = tk.Entry(root)
total_minutes_entry.pack()

minutes_unavailable_label = tk.Label(root, text="Enter total minutes the server was unavailable:")
minutes_unavailable_label.pack()

minutes_unavailable_entry = tk.Entry(root)
minutes_unavailable_entry.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
