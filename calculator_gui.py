import tkinter as tk

# Function to update the input field whenever a button is pressed
def button_click(value):
    current = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(0, current + str(value))

# Function to clear the input field (AC button)
def button_clear():
    input_field.delete(0, tk.END)

# Function to calculate the result (Equal button)
def button_equal():
    try:
        result = eval(input_field.get())
        input_field.delete(0, tk.END)
        input_field.insert(0, str(result))
    except:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Error")

# Initialize the root window
root = tk.Tk()
root.title("Calc App")
root.configure(bg="black")

# Input field
input_field = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=5, relief=tk.FLAT, justify=tk.RIGHT)
input_field.grid(row=0, column=0, columnspan=4)

# Button settings (colors, font, etc.)
button_font = ('Arial', 18)
button_color = "#ff9500"
button_bg = "#333"
special_button_bg = "#a5a5a5"

# Creating the buttons (AC, +/- , %, /, etc.)
buttons = [
    ('AC', 1, 0, button_clear, special_button_bg),
    ('+/-', 1, 1, lambda: button_click('-'), special_button_bg),
    ('%', 1, 2, lambda: button_click('%'), special_button_bg),
    ('/', 1, 3, lambda: button_click('/'), button_color),
    ('7', 2, 0, lambda: button_click(7), button_bg),
    ('8', 2, 1, lambda: button_click(8), button_bg),
    ('9', 2, 2, lambda: button_click(9), button_bg),
    ('*', 2, 3, lambda: button_click('*'), button_color),
    ('4', 3, 0, lambda: button_click(4), button_bg),
    ('5', 3, 1, lambda: button_click(5), button_bg),
    ('6', 3, 2, lambda: button_click(6), button_bg),
    ('-', 3, 3, lambda: button_click('-'), button_color),
    ('1', 4, 0, lambda: button_click(1), button_bg),
    ('2', 4, 1, lambda: button_click(2), button_bg),
    ('3', 4, 2, lambda: button_click(3), button_bg),
    ('+', 4, 3, lambda: button_click('+'), button_color),
    ('0', 5, 0, lambda: button_click(0), button_bg),
    ('.', 5, 1, lambda: button_click('.'), button_bg),
    ('=', 5, 2, button_equal, button_color),
]

# Adding buttons to the grid
for (text, row, col, command, color) in buttons:
    tk.Button(root, text=text, padx=20, pady=20, font=button_font, bg=color, fg="white", command=command).grid(row=row, column=col, columnspan=(2 if text == '0' else 1))

# Start the Tkinter event loop
root.mainloop()
