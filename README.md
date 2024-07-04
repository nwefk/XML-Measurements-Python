# XML Data Processing and Visualization

This project contains scripts for processing XML data and visualizing it in various formats.

## Prerequisites

- Python 3.10.x

## Installation

1. **Download the Project Files**

    Download the project files to your local machine.

2. **Set Up a Virtual Environment**

    It's recommended to use a virtual environment to manage dependencies. Run the following commands to create and activate a virtual environment:

    ```bash
    python -m venv venv
    ```

    - On Windows:
        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

3. **Install the Required Libraries**

    Install the required Python libraries using `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Scripts

### 1. xml_parser.py

This script creates text files from the data in the chosen XML file.

#### Usage

1. Run the script:
    ```bash
    python xml_parser.py
    ```
2. In the first file browser pop-up, choose the XML file to use.
3. In the second file browser pop-up, choose the directory where the text files should be written.

### 2. graph_plotting.py

This script displays a graph from the values in the chosen text file.

#### Usage

1. Run the script:
    ```bash
    python graph_plotting.py
    ```
2. In the file browser pop-up, choose the text file containing the data to plot.

### 3. xml_plotter.py

This script displays graphs of the data from the chosen XML file.

#### Usage

1. Run the script:
    ```bash
    python xml_plotter.py
    ```
2. In the file browser pop-up, choose the XML file containing the data to plot.

