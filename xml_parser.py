import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import struct
import base64
import tkinter as tk
from tkinter import filedialog
import os


file_name = "test_data_"

root = tk.Tk()
root.withdraw()

file_path_get = filedialog.askopenfilename(
    # Ask the user to select which file to use
    title="Select an XML file", 
    filetypes=(("XML files", "*.xml"), ("All files", "*.*"))
    )

if file_path_get:
    # Ask the user to select the directory to save the files
    save_directory = filedialog.askdirectory(
        title="Select directory to save files"
    )

    if save_directory:
        tree = ET.parse(file_path_get)
        root = tree.getroot()

        name_list = []
        name_count = {}

        # In the case of reoccuring names
        for names in root.iter("Ydata"):
            ylabel = names.attrib["ylabel"]
            
            if ylabel in name_count:
                name_count[ylabel] += 1
                name_list.append(f"{ylabel}_{name_count[ylabel]}")
                
            else:
                name_count[ylabel] = 0
                name_list.append(ylabel)


        for index, values in enumerate(root.iter("values")):
            encoded_data = values.text.strip()
            binary_data = base64.b64decode(encoded_data)
            num_values = int(values.attrib['numvalues'])
            float_values = struct.unpack('<' + 'f' * num_values, binary_data)

            file_path_write = os.path.join(save_directory, f"{file_name}{name_list[index]}.txt")

            with open(file_path_write, "w") as file:
                file.write("\n".join(str(value) for value in float_values[:num_values]))
