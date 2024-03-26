import tkinter as tk

# Function to update the display when buttons are clicked
def button_click(char):
    global display_text
    if char == 'C':
        display_text.set('')
    elif char == '=':
        try:
            result = eval(display_text.get())
            display_text.set(str(result))
        except:
            display_text.set("Error")
    else:
        display_text.set(display_text.get() + str(char))

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Variable to store the display text
display_text = tk.StringVar()

# Entry widget to display the input and output
display = tk.Entry(root, textvariable=display_text, font=('Arial', 20), bd=10, insertwidth=4, width=14, justify='right')
display.grid(row=0, column=0, columnspan=4)

# List of buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Loop to create and place buttons
row_num = 1
col_num = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda char=button: button_click(char)).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Start the main event loop
root.mainloop()



