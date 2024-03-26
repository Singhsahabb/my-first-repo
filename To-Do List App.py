import tkinter as tk
from tkinter import messagebox

# Function to add a new task to the list
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a selected task from the list
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List App")

# Create task entry widget
task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

# Create buttons
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.grid(row=0, column=2, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.grid(row=1, column=2, padx=5, pady=5)

# Create task listbox
task_listbox = tk.Listbox(root, width=50)
task_listbox.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

# Start the main event loop
root.mainloop()




