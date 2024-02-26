# Frameworks
import tkinter as tk
from tkinter import ttk

# Functions
def button_func():
    entry_text = entry.get()
    label['text'] = entry_text
    entry['state'] = 'disable'

def button_rest_func():
    label['text'] = 'Some text'
    entry['state'] = 'enable'

# Window
window = tk.Tk()
window.title('Getting and setting widgets')
window.geometry('800x500')

# Widgets
label = ttk.Label(master=window, text= 'Some text')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='the button', command= button_func)
button.pack()

# button restart
button_rest = ttk.Button(master=window, text='restart', command= button_rest_func)
button_rest.pack()
# Run
window.mainloop()
