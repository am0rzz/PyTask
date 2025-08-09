import tkinter as tk
from tkinter import messagebox
import Task_Manager


root = tk.Tk()
root.title("PyTask")
root.geometry("800x600")
root.iconbitmap("checklist.ico")
listbox = tk.Listbox(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=listbox.yview)
taskmanager = Task_Manager.TaskManager()
taskmanager.load_tasks()
filtered_tasks = taskmanager.tasks.copy()


for i in range(len(taskmanager.tasks)): # Put tasks in the listbox
    listbox.insert(i,str(taskmanager.tasks[i]))

def update_task_list():
    """
    Update listbox everytime we add/deleted/edit/complete a task.
    """
    global filtered_tasks
    listbox.delete(0, tk.END)
    for i in range(len(filtered_tasks)):
        listbox.insert(tk.END,str(filtered_tasks[i]))

title_var = tk.StringVar()
desc_var = tk.StringVar()
search_var = tk.StringVar()

def add():
    """
    the Add Task Button
    """
    global filtered_tasks
    title = title_var.get()
    if not title.strip(): # Checks if user didn't enter a task title
        messagebox.showwarning("Warning", "Please Enter a task name!")
        return
    description = desc_var.get()
    task = Task_Manager.Task(title,description)
    taskmanager.add_task(task)
    taskmanager.save_tasks()
    filtered_tasks = taskmanager.tasks.copy()
    update_task_list()
    title_var.set("")
    desc_var.set("")

def delete():
    """
    Delete task based on task index in listbox
    """
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task to delete.")
        return
    task_to_delete = filtered_tasks[listbox.curselection()[0]]
    if task_to_delete in taskmanager.tasks:
        taskmanager.tasks.remove(task_to_delete)
    filtered_tasks.remove(task_to_delete)
    update_task_list()
    taskmanager.save_tasks()
    

def mark_as_completed():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task.")
        return
    task = filtered_tasks[selected[0]]
    task.completed = not task.completed
    taskmanager.save_tasks()
    update_task_list()

def search():
    global filtered_tasks
    search = search_var.get().lower().strip()
    if not search.strip():
        messagebox.showwarning("Warning", "Please Enter a text.")
        return
    listbox.delete(0,tk.END)
    filtered_tasks.clear()
    for i in range(len(taskmanager.tasks)):
        if search in taskmanager.tasks[i].title.lower() or search in taskmanager.tasks[i].description.lower():
            filtered_tasks.append(taskmanager.tasks[i])
    update_task_list()

def show_all():
    global filtered_tasks
    listbox.delete(0, tk.END)
    filtered_tasks = taskmanager.tasks[:]
    for task in filtered_tasks:
        listbox.insert(tk.END,str(task))

def buttons_labels():
    """
    Buttons and labels lay here
    """
    title_label = tk.Label(root, text='Task', font=('calibre', 10, 'bold'))
    title_entry = tk.Entry(root, textvariable=title_var, font=('calibre', 10, 'normal'))
    desc_label = tk.Label(root, text='Description', font=('calibre', 10, 'bold'))
    desc_entry = tk.Entry(root, textvariable=desc_var, font=('calibre', 10, 'normal'))
    search_label = tk.Label(root, text='Search', font=('calibre', 10, 'bold'))
    search_entry = tk.Entry(root, textvariable=search_var, font=('calibre', 10, 'normal'))
    add_button = tk.Button(root, text="Add Task", command=add)
    delete_button = tk.Button(root,text="Delete Task", command= delete)
    mark_button = tk.Button(root,text="Toggle Complete", command= mark_as_completed)
    search_button = tk.Button(root,text="Search" , command= search)
    show = tk.Button(root,text="Show All tasks",command= show_all)
    title_label.place(relx= 0.1,rely=0.03)
    title_entry.place(relx = 0.2, rely=0.03, relwidth=0.6)

    desc_label.place(relx = 0.1 ,rely = 0.1)
    desc_entry.place(relx = 0.2, rely=0.1, relwidth=0.6)

    search_label.place(relx= 0.1,rely=0.24)
    search_entry.place(relx=0.2,rely=0.24,relwidth=0.6)

    add_button.place(relx=0.45, rely = 0.16, width=100, height=30)
    show.place(relx=0.85, rely = 0.20, width=100, height=30)

    delete_button.place(relx=0.35, rely=0.9, width=100, height=30)
    search_button.place(relx=0.45,rely = 0.29, width = 100, height = 30)
    mark_button.place(relx=0.65, rely=0.9, width=120, height=30)


buttons_labels()
listbox.config(yscrollcommand=scrollbar.set)
listbox.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
scrollbar.place(relx=0.88, rely=0.35, relwidth=0.03, relheight=0.5)
root.mainloop()