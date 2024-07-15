import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import os


def plot():
    root = tk.Tk()
    root.withdraw()

    # Ask the user to select which file to use
    file_path = filedialog.askopenfilename(
        title="Select a file", 
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )

    if file_path:
        file_name_with_ext = os.path.basename(file_path)
        file_name, _ = os.path.splitext(file_name_with_ext)
        lines_list = []

        with open(file_path, "r") as file:
            for line in file:
                lines_list.append(float(line.strip()))

        fig = plt.gcf()
        fig.canvas.manager.set_window_title(file_name)

        ypoints = lines_list

        plt.plot(ypoints, linestyle = 'solid')
        plt.show()


if __name__ == "__main__":
    plot()
