import tkinter as tk

# Initialize list to store tasks
tasks = []

# Function to add a task
def add_task(event):
  task = task_input.get()
  tasks.append(task)
  update_list()

# Function to delete a task
def delete_task(event):
  try:
    task = task_listbox.get(tk.ANCHOR)
    tasks.remove(task)
  except ValueError:
    # Task is not in list, so do nothing
    pass
  update_list()

# Function to update the listbox
def update_list():
  task_listbox.delete(0, "end")
  for task in tasks:
    task_listbox.insert("end", task)

# Create main window
window = tk.Tk()
window.title("To-Do List")

# Create widgets
task_label = tk.Label(window, text="Task:")
task_input = tk.Entry(window)
add_button = tk.Button(window, text="Add")
delete_button = tk.Button(window, text="Delete")
task_listbox = tk.Listbox(window)

# Add button click events
add_button.bind("<Button-1>", add_task)
delete_button.bind("<Button-1>", delete_task)

# Add widgets to window
task_label.pack()
task_input.pack()
add_button.pack()
delete_button.pack()
task_listbox.pack()

# Run the main loop
window.mainloop()
