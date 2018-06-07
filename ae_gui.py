from tkinter import N, S, E, W, Tk
from tkinter.ttk import Button, Entry, Frame, Label
from tkinter.filedialog import askopenfilename, INSERT, StringVar

import settings
from AE import fetch, update

# Set up window
root = Tk()
root.title("Alma Enumerator")

# Select file to use
def get_file_path(btn, file):
    setattr(settings, file, askopenfilename())
    btn.configure(text=getattr(settings, file))

# Make sure to get the latest mms_id and api_key    
def update_settings():
    settings.mms_id = mms_id.get().strip()
    settings.api_key = api_key.get().strip()

# Fetch item info and save to file    
def fetch_it():
    update_settings()
    fetch(settings.mms_id, settings.output_file, settings.error_file, settings.api_key, settings.base_url)

# Update item info from file
def update_it():
    update_settings()
    update(settings.mms_id, settings.input_file, settings.api_key, settings.base_url)

# Set up content area in window
mainframe = Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Set up input for MMS ID 
mms_id = StringVar()
mms_entry = Entry(mainframe, width=14, textvariable=mms_id)
mms_entry.insert(INSERT, settings.mms_id)
mms_entry.grid(column=2, row=1, sticky=(W, E))
Label(mainframe, text="MMS ID").grid(column=3, row=1, sticky=W)

# Set up input for output file
output_btn = Button(mainframe, text=settings.output_file, command=lambda: get_file_path(output_btn, 'output_file'))
output_btn.grid(column=2, row=2  , sticky=(W, E))
Label(mainframe, text="Output File").grid(column=3, row=2, sticky=W)

# Set up input for input file
input_btn = Button(mainframe, text=settings.input_file, command=lambda: get_file_path(input_btn, 'input_file'))
input_btn.grid(column=2, row=3, sticky=(W, E))
Label(mainframe, text="Input File").grid(column=3, row=3, sticky=W)

# Set up input for error file
error_btn = Button(mainframe, text=settings.error_file, command=lambda: get_file_path(error_btn, 'error_file'))
error_btn.grid(column=2, row=4, sticky=(W, E))
Label(mainframe, text="Error File").grid(column=3, row=4, sticky=W)

# Set up input for API key
api_key = StringVar()
api_entry = Entry(mainframe, width=14, textvariable=api_key)
api_entry.insert(INSERT, settings.api_key)
api_entry.grid(column=2, row=5, sticky=(W, E))
Label(mainframe, text="API Key").grid(column=3, row=5, sticky=W)

# Add 'Fetch' and 'Update' buttons
Button(mainframe, text="Fetch", command=fetch_it).grid(column=2, row=6, sticky=W)
Button(mainframe, text="Update", command=update_it).grid(column=3, row=6, sticky=E)

# Set padding for widgets
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# Set focus on input for MMS ID
mms_entry.focus()

# Begin main loop
root.mainloop()