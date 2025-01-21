import os
import subprocess
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyperclip

def run_script(script_path):
    """Runs a Python script in a separate thread."""
    def target():
        try:
            subprocess.run(["python", script_path], check=True)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run script: {e}")

    thread = threading.Thread(target=target)
    thread.daemon = True  # Ensure it closes with the GUI
    thread.start()

def create_tab_content(tab, buttons):
    """Adds buttons and explanatory text to a tab."""
    for button_text, description, script_path in buttons:
        frame = ttk.Frame(tab)
        frame.pack(fill="x", pady=5)

        btn = ttk.Button(frame, text=button_text, command=lambda path=script_path: run_script(path))
        btn.pack(side="left", padx=5)

        label = ttk.Label(frame, text=description)
        label.pack(side="left", padx=5)

# Define the scripts and explanations for each tab
tab1_buttons = [
    ("Script 1", "Runs script 1.", "path/to/script1.py"),
    ("Script 2", "Runs script 2.", "path/to/script2.py"),
    ("Script 3", "Runs script 3.", "path/to/script3.py"),
    ("Script 4", "Runs script 4.", "path/to/script4.py"),
    ("Script 5", "Runs script 5.", "path/to/script5.py"),
]

tab2_buttons = [
    ("Script A", "Runs script A.", "path/to/scriptA.py"),
    ("Script B", "Runs script B.", "path/to/scriptB.py"),
    ("Script C", "Runs script C.", "path/to/scriptC.py"),
    ("Script D", "Runs script D.", "path/to/scriptD.py"),
    ("Script E", "Runs script E.", "path/to/scriptE.py"),
]

tab3_buttons = [
    ("Script X", "Runs script X.", "path/to/scriptX.py"),
    ("Script Y", "Runs script Y.", "path/to/scriptY.py"),
    ("Script Z", "Runs script Z.", "path/to/scriptZ.py"),
    ("Script W", "Runs script W.", "path/to/scriptW.py"),
    ("Script V", "Runs script V.", "path/to/scriptV.py"),
]

# Initialize the GUI
root = tk.Tk()
root.title("Python Script Launcher")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Create tabs and add content
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab_info = ttk.Frame(notebook)

notebook.add(tab1, text="Tab A")
notebook.add(tab2, text="Tab B")
notebook.add(tab3, text="Tab C")
notebook.add(tab_info, text="Info")

create_tab_content(tab1, tab1_buttons)
create_tab_content(tab2, tab2_buttons)
create_tab_content(tab3, tab3_buttons)

# Add explanation to Info tab
info_frame = ttk.Frame(tab_info)
info_frame.pack(expand=True)

explanation_label = ttk.Label(info_frame, text="This application launches Python scripts given their paths.\nIt ensures the GUI remains responsive.", wraplength=400, justify="center")
explanation_label.pack(pady=10)

root.mainloop()
