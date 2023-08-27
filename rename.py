import os
import tkinter as tk
from tkinter import filedialog

# Function to rename files
def rename_files():
    folder_path = entry_path.get()          # Get the folder path from the entry field
    begin_value = int(entry_begin.get())    # Get the starting number for renaming
    end_value = int(entry_end.get())        # Get the ending number for renaming
    prefix = entry_prefix.get()             # Get the prefix for renaming
    
    if not os.path.exists(folder_path):     # Check if the folder path exists
        status_label.config(text="Invalid path", fg="red")
        return
    
    file_list = os.listdir(folder_path)     # List all files in the folder
    
    for count, filename in enumerate(file_list, start=begin_value):
        if count > end_value:               # Stop renaming if the count exceeds the end value
            break
        
        file_extension = os.path.splitext(filename)[1]  # Get the file extension
        new_filename = f"{prefix}{count:03d}{file_extension}"  # Create the new filename
        
        # Rename the file
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        status_label.config(text=f"Renamed '{filename}' to '{new_filename}'", fg="green")
    
    status_label.config(text="File renaming complete", fg="blue")

# Function to browse for a folder
def browse_folder():
    folder_selected = filedialog.askdirectory()  # Open a folder selection dialog
    entry_path.delete(0, tk.END)                # Clear the entry field
    entry_path.insert(0, folder_selected)       # Insert the selected folder path

# Create the main window
root = tk.Tk()
root.title("File Renamer")

# Styling and window size
root.configure(bg="#f0f0f0")
root.geometry("220x290")

# Create and place widgets
label_path = tk.Label(root, text="Folder Path:", bg="#f0f0f0")
entry_path = tk.Entry(root, width=30)
button_browse = tk.Button(root, text="Browse", command=browse_folder)

label_begin = tk.Label(root, text="Begin Value:", bg="#f0f0f0")
entry_begin = tk.Entry(root, width=10)

label_end = tk.Label(root, text="End Value:", bg="#f0f0f0")
entry_end = tk.Entry(root, width=10)

label_prefix = tk.Label(root, text="Prefix:", bg="#f0f0f0")
entry_prefix = tk.Entry(root, width=20)

button_rename = tk.Button(root, text="Rename Files", command=rename_files, bg="#4CAF50", fg="white")
status_label = tk.Label(root, text="", bg="#f0f0f0")

# Arrange widgets with spacing
label_path.pack(pady=0.5)
entry_path.pack(pady=0.5)
button_browse.pack(pady=0.5)
label_begin.pack(pady=0.5)
entry_begin.pack(pady=0.5)
label_end.pack(pady=0.5)
entry_end.pack(pady=0.5)
label_prefix.pack(pady=0.5)
entry_prefix.pack(pady=0.5)
button_rename.pack(pady=20)
status_label.pack(pady=0.5)

root.mainloop()  # Start the GUI event loop
