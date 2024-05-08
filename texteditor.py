import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def new_file():
    text_editor.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            content = text_editor.get(1.0, tk.END)
            file.write(content)

def about():
    messagebox.showinfo("About", "Simple Text Editor\nCreated using Tkinter")

root = tk.Tk()
root.title("Simple Text Editor")

# Create Menu
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

# Create Text Area
text_editor = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
text_editor.pack(expand=True, fill='both')

root.mainloop()
