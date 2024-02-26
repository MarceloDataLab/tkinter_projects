# Frameworks
import tkinter as tk
from tkinter import ttk

def button_func():
    print('A button was pressed')

def greetings():
    print('Hello')

# Window
window = tk.Tk()
window.title('Windows & Widgets')
window.geometry('800x500')

# ttk label
label = ttk.Label(master=window, text= 'This is a test')
label.pack()

# tk widgets
text = tk.Text(master=window)
text.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# label exercise
label_exercise = ttk.Label(master=window, text= 'my label')
label_exercise.pack()

# ttk button
button = ttk.Button(master=window, text= 'a button', command= button_func)
button.pack()

# button exercise
button_exercise = ttk.Button(master=window, text= 'greetings', command=greetings)
button_exercise.pack()

# Run
window.mainloop()
