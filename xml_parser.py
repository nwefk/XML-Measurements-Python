import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import struct
import base64
import tkinter as tk
from tkinter import filedialog
import os


# In the case of reoccuring names
def labels(root):
    label_count = {}
    label_list = []
    for names in root.iter("Ydata"):
        ylabel = names.attrib["ylabel"]
        
        if ylabel in label_count:
            label_count[ylabel] += 1
            label_list.append(f"{ylabel}_{label_count[ylabel]}")
            
        else:
            label_count[ylabel] = 0
            label_list.append(ylabel)

    return label_list


def xml_parse():
    root = tk.Tk()
    root.withdraw()

    # Ask the user to select which file to use
    file_path_get = filedialog.askopenfilename(
        title="Select an XML file", 
        filetypes=(("XML files", "*.xml"), ("All files", "*.*"))
        )
    
    # Ask the user to select the directory to save the files
    if file_path_get:
        save_directory = filedialog.askdirectory(
            title="Select directory to save files"
        )

        if save_directory:
            tree = ET.parse(file_path_get)
            root = tree.getroot()

            name_list = labels(root)

            for index, values in enumerate(root.iter("values")):
                encoded_data = values.text.strip()
                binary_data = base64.b64decode(encoded_data)
                num_values = int(values.attrib['numvalues'])
                float_values = struct.unpack('<' + 'f' * num_values, binary_data)

                file_path_write = os.path.join(save_directory, f"{name_list[index]}.txt")

                with open(file_path_write, "w") as file:
                    file.write("\n".join(str(value) for value in float_values[:num_values]))


if __name__ == "__main__":
    xml_parse()
