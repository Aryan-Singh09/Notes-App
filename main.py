'''NOTES APP'''

#import tkinter for creating GUI apps
import tkinter as tk

#import filedialog and messagebox from tkinter for file handling and displaying messages
from tkinter import filedialog, messagebox

#Main application window
root=tk.Tk() # Create the main application window
root.title("Notes App - Untitled") # Set the title of the window
root.geometry("800x600") # Set the size of the window

#create a text widget for writing notes
scrollbar = tk.Scrollbar(root)

text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 13),
    yscrollcommand=scrollbar.set,
    bg="#1e1e1e",
    fg="white",
    insertbackground="white"
)

scrollbar.config(command=text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text.pack(expand=True, fill=tk.BOTH) # Pack the text widget to fill the window

#Main event loop to run the application

#function1 - to create a new text file
def new_file():
    root.title("Notes App - Untitled")
    text.delete(1.0, tk.END) # Clear the texts already in the text widget to create a new file

#function2 - to open a new text file
def open_file():
    #open file dialogue
    file_path=filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        root.title(f"Notes App - {file_path}")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text.delete(1.0, tk.END)
                text.insert(tk.END, file.read())
        except Exception as e:
            messagebox.showerror("Error", str(e))

#Function3 - to save the text file

def save_file():
    #open file dialogue
    file_path=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        root.title(f"Notes App - {file_path}")
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text.get(1.0, tk.END))

            messagebox.showinfo(
                "Info",
                "File saved successfully!"
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))

#Function4 - to exit the application
def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()
#End of functions


#Menu bar
menu_bar=tk.Menu(root) # Create a menu bar
root.config(menu=menu_bar) # Set the menu bar for the root window
file_menu=tk.Menu(menu_bar) # Create a file menu


menu_bar.add_cascade(label="File", menu=file_menu) # Add the file menu to the menu bar
#New, Open, Save, Exit options in the file menu
file_menu.add_command(label="New", command=new_file) # Add a "New" option to the file menu that calls the new_file function
file_menu.add_command(label="Open", command=open_file) # Add an "Open" option to the file menu that calls the open_file function
file_menu.add_command(label="Save", command=save_file) # Add a "Save" option to the file menu that calls the save_file function
file_menu.add_separator() # Add a separator in the file menu
file_menu.add_command(label="Exit", command=exit_app) # Add an "Exit" option to the file menu that calls the exit_app function


#Adding keyboard shortcuts for the text widget
root.bind("<Control-n>", lambda event: new_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<Control-q>", lambda event: exit_app())
root.protocol("WM_DELETE_WINDOW", exit_app)
root.mainloop() # Start the main event loop to run the application
