'''Starting point for program. tkinter menu to prompt user to generate a new maze or exit program'''
import tkinter
from tkinter import *
from tkinter import ttk
import threading
from maze_algorithm_analysis import maze_algorithm_analysis

# Create window
root = tkinter.Tk()

# Set size of tkinter frame
root.geometry(("700x300"))

Label(root, text='Click to Generate New Maze').pack(pady=15)

ttk.Button(root, text="Generate New Maze", command=maze_algorithm_analysis).pack()


root.mainloop()

