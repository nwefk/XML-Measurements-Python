import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import struct
import base64
import tkinter as tk
from tkinter import filedialog
from xml_parser import labels

def xml_plot():
    root = tk.Tk()
    root.withdraw()

    # Ask the user to select which file to use
    file_path = filedialog.askopenfilename(
        title="Select an XML file", 
        filetypes=(("XML files", "*.xml"), ("All files", "*.*"))
        )

    if file_path:
        tree = ET.parse(file_path)
        xml_root = tree.getroot()
        lines_list = []

        for values in xml_root.iter("values"):
            value_list = []
            encoded_data = values.text.strip()
            binary_data = base64.b64decode(encoded_data)
            num_values = int(values.attrib['numvalues'])
            float_values = struct.unpack('<' + 'f' * num_values, binary_data)

            for values in float_values[:num_values]:
                value_list.append(values)

            lines_list.append(value_list)
        
        ylabels = labels(xml_root)

        for ylabel, lines in zip(ylabels, lines_list):
            plt.plot(lines, label=ylabel)
        
        plt.legend()
        plt.show()


if __name__ == "__main__":
    xml_plot()
