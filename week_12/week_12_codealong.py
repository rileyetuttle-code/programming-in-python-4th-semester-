import tkinter as tk
from tkinter.font import Font
# Your tkinter modules used
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import showerror, showinfo, askyesno
from tkinter.simpledialog import askstring
import shutil
from pathlib import Path
import os
from send2trash import send2trash


def main() -> None: 
    padding: int = 20
    btn_x_size: int = 40
    btn_y_size: int = 3

    root: tk.Tk = tk.Tk()
    root.title("File Automation")
    root.config(bg=Color.bg_color)

    label_font: Font = Font(family="Consolas", size=30)

    frame: tk.Frame = tk.Frame(
        root,
        bg = Color.bg_color,
        padx=padding,
        pady=padding,
    )
    label: tk.Label = tk.Label(
        frame,
        text="File Automation",
        font=label_font,
        bg=Color.bg_color,
        fg=Color.text_color,
    )

    copy_btn: HoverButton = HoverButton(
        master=frame,
        text="Copy File",
        command=copy_file,
        width=btn_x_size,
        height=btn_y_size,
    )
    move_btn: HoverButton = HoverButton(
        master=frame,
        text="Move File",
        command=move_file,
        width=btn_x_size,
        height=btn_y_size,
    )
    rename_btn: HoverButton = HoverButton(
        master=frame,
        text="Rename File",
        command=rename_file,
        width=btn_x_size,
        height=btn_y_size,
    )
    delete_btn: HoverButton = HoverButton(
        master=frame,
        text="Delete File",
        command=delete_file,
        width=btn_x_size,
        height=btn_y_size,
    )

    frame.pack()
    label.pack()

    copy_btn.pack()
    move_btn.pack()
    rename_btn.pack()
    delete_btn.pack()

    root.mainloop()


def copy_file() -> None:
    """Make a copy of a file."""

    # get base file path name and copy it to new variable using tkinter and pathlib libraries 
    file_path: str = askopenfilename(title="Select a file to copy")
    path = Path(file_path)
    file_name: str = path.name
    copy_file_name: str = f"copy_of_{file_name}"

    # get destination directory from tkinkter tools, then use path join to add the string copied file name to the dest directory as an actual usable path, then use shutil copy with original file path as the source and the the new dest full path as the destination
    dest_path: str = askdirectory(title= f"Select a destination directory for {copy_file_name}")
    dest_full_path: str = Path(dest_path) / copy_file_name
    shutil.copy(file_path, dest_full_path)

    # success message
    showinfo(title="Success!", message=f"{file_name} has been copied as {copy_file_name} and moved to {Path(dest_path)}")


def move_file() -> None:
    """Move a file to a new directory."""

    # get base file path name and parent name for comparison later
    file_path: str = askopenfilename(title="Select a file to move")
    path = Path(file_path)
    file_name: str = path.name
    file_path_parent: str = path.parent

    # get destination path from tkinter tools
    dest_path: str = askdirectory(title= f"Select a destination directory for {file_name}")

    # check if file is being moved to the same directory, if not, move it
    if(file_path_parent == Path(dest_path)):
        showerror(title="Error!", message="Destination directory is the same as the source destination")
    else:
        shutil.move(file_path, dest_path)
        # success message
        showinfo(title="Success!", message=f"{file_name} has been moved to {Path(dest_path)}")


def rename_file() -> None:
    """Rename a file."""

    file_path: str = askopenfilename(title="Select a file to rename")
    path = Path(file_path)
    file_name: str = path.name

    # get new file name from user through an input box and turn it into a new file path to be used in the os.rename later
    new_file_name: str = askstring(title="Rename File", prompt=f"Please enter a new name for {file_name}")
    new_file_path: str = path.parent / new_file_name

    # error checking for new file name equalling old fild name
    if (new_file_name == file_name):
        showerror(title="Error!", message="The entered new file name is the same as the old file name.")
    else: 
        # renaming using os and showing a success message box
        os.rename(file_path, new_file_path)
        showinfo(title="Success!", message=f"File has been renamed from {file_name} to {new_file_name}")
    

def delete_file() -> None: 
    """Delete a file and move to trash."""

    # get file path from user and file name from pathlib
    file_path: str = askopenfilename(title="Select a file to delete.")
    path = Path(file_path).resolve() # done to resolve forward slashes for send2trash to be able to process it
    file_name: str = path.name

    # ask user for confirmation on deletion
    delete_result: str = askyesno(title="Warning!", message="Are you sure you want to delete this file?")

    # if selection is no, return
    if(delete_result == False):
        return
    else: 
        # if selection is yes, send file to trash and show success messgae box
        send2trash(path)
        showinfo(title="Success!", message=f"{file_name} was successfully sent to trash.")
    

class HoverButton(tk.Button):
    """A class to create a button with hover effect."""

    def __init__(self, **kw_args) -> None: 
        """Set the HoverButton up."""

        super().__init__(**kw_args)
        self.config(bg=Color.base_color, fg=Color.btn_txt_base_color)

        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.off_hover)

    def on_hover(self, event: tk.Event) -> None: 
        """Change the color of the button when mouse is over it."""

        event.widget.config(bg=Color.hover_color, fg=Color.btn_txt_hover_color)

    def off_hover(self, event: tk.Event) -> None: 
        """Change the color of the button when mouse moves off of it."""

        event.widget.config(bg=Color.base_color, fg=Color.btn_txt_base_color)

class Color: 
    """A class to store colors for the GUI."""

    bg_color = "#0d0d0d"
    text_color = "#00ff00"
    base_color = "#1a3a1a"
    hover_color = "#00ff00"
    btn_txt_base_color = "#00ff00"
    btn_txt_hover_color = "#000000"


if __name__ == "__main__":
    main()