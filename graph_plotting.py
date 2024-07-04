import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# Ask the user to select which file to use
file_path = filedialog.askopenfilename(
    title="Select a file", 
    filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )

if file_path:
    lines_list = []

    with open(file_path, "r") as file:
        for line in file:
            lines_list.append(float(line.strip()))

    ypoints = np.array(lines_list)

    plt.plot(ypoints, linestyle = 'solid')
    plt.show()