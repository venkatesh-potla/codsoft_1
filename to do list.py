import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def clear_tasks():
    if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
        task_listbox.delete(0, tk.END)

# Set up the main application window
root = tk.Tk()
root.title("To-Do List")

# Create and place the heading
heading = tk.Label(root, text="To Do List", font=("Helvetica", 24))
heading.pack(pady=10)

# Create and place widgets
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Add Task", width=48, command=add_task)
add_task_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

delete_task_button = tk.Button(root, text="Delete Selected Task", width=48, command=delete_task)
delete_task_button.pack(pady=5)

clear_tasks_button = tk.Button(root, text="Clear All Tasks", width=48, command=clear_tasks)
clear_tasks_button.pack(pady=5)

# Run the application
root.mainloop()
