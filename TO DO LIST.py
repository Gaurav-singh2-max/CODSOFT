#!/usr/bin/env python
# coding: utf-8

# In[2]:


#to do list
import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("My To-Do List")
root.geometry("400x500")
root.resizable(False,False)

tasks=[]

def update_listbox():
    listbox.delete(0, tk.END)
    for idx,task in enumerate(tasks, 1):
        status= "GOT" if task['done'] else "NOT"
        listbox.insert(tk.END, f"{idx}. [{status}] {task['task']}")

def add_task():
    task_text=entry.get().strip()
    if task_text=="":
        messagebox.showwarning("Input Error", "Please enetr a task!")
        return
    tasks.append({"task": task_text, "done": False})
    entry.delete(0, tk.END)
    update_listbox()

def mark_done():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")
        return
    index = selected[0]
    tasks[index]['done']=True
    update_listbox()

def delete_task():
    selected=listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")
        return
    index=selected[0]
    tasks.pop(index)
    update_listbox()

def clear_all():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        tasks.clear()
        update_listbox()

entry=tk.Entry(root, width=30)
entry.pack(pady=10)

add_button=tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

listbox=tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

button_frame=tk.Frame(root)
button_frame.pack(pady=5)

done_button=tk.Button(button_frame, text="Mark Done", command=mark_done)
done_button.grid(row=0, column=0 , padx=5)

delete_button=tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=1 , padx=5)

clear_button=tk.Button(button_frame, text="Clear All", command=clear_all)
clear_button.grid(row=0, column=2 , padx=5)

root.mainloop()
        
    


# In[ ]:




