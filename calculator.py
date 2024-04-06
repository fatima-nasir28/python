import tkinter as tk
import math

def button_click(char):
    current = display_var.get()
    if char == "C":
        display_var.set("")
    elif char == "=":
        try:
            result = eval(current)
            display_var.set(str(result))
        except:
            display_var.set("Error")
    elif char == "sqrt":
        try:
            result = math.sqrt(float(current))
            display_var.set(str(result))
        except:
            display_var.set("Error")
    elif char == "^2":
        try:
            result = float(current) ** 2
            display_var.set(str(result))
        except:
            display_var.set("Error")
    elif char == "^3":
        try:
            result = float(current) ** 3
            display_var.set(str(result))
        except:
            display_var.set("Error")
    elif char == "%":
        try:
            result = float(current) / 100
            display_var.set(str(result))
        except:
            display_var.set("Error")
    else:
        display_var.set(current + char)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a variable to store the current display text
display_var = tk.StringVar()
display_var.set("")

# Create the display label
display_label = tk.Label(root, textvariable=display_var, font=("Arial", 20), anchor="e", padx=10)
display_label.grid(row=0, column=0, columnspan=4)

# Define buttons with their colors
button_configurations = [
    ("7", "#7f8c8d"), ("8", "#7f8c8d"), ("9", "#7f8c8d"), ("/", "#2ecc71"),
    ("4", "#7f8c8d"), ("5", "#7f8c8d"), ("6", "#7f8c8d"), ("*", "#2ecc71"),
    ("1", "#7f8c8d"), ("2", "#7f8c8d"), ("3", "#7f8c8d"), ("-", "#2ecc71"),
    ("0", "#7f8c8d"), (".", "#7f8c8d"), ("=", "#3498db"), ("+", "#2ecc71"),
    ("C", "#e74c3c"), ("sqrt", "#7f8c8d"), ("^2", "#7f8c8d"), ("^3", "#7f8c8d"),
    ("%", "#7f8c8d")
]

# Create and position buttons
for i, (char, color) in enumerate(button_configurations):
    row = i // 4 + 1
    col = i % 4
    button = tk.Button(root, text=char, font=("Arial", 16), width=5, height=2, bg=color, fg="white", command=lambda c=char: button_click(c))
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
