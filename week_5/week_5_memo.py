import tkinter as tk
import os 


def main(): 
    """Hacker's memo by Riley Tuttle"""

    # variables
    width: int = 700
    height: int = 500 # had to change for my laptop resolution
    widgets_width: int = 40

    # colors - use your own
    colors: dict = {
        "app_bg": "light blue",
        "app_text": "green",
        "console_bg": "orange",
        "console_text": "green",
    }

    # Change font if you want
    app_font: tuple = ("Consolas", 20)
    button_font: tuple = ("Consolas", 20)

    # setting window up
    wn: tk.Tk = tk.Tk()
    wn.title("Hacker's Memo")
    wn.geometry(f"{width}x{height}")
    wn.minsize(width, height)
    wn.maxsize(width, height)
    wn.config(bg = colors["app_bg"])

    # creating and packing widgets
    label: tk.Label = tk.Label(
        wn,
        text = "Hacker's Memo",
        fg = colors["app_text"],
        bg = colors["app_bg"],
        font = app_font,
    )
    label.pack()

    entry_text: tk.Text = tk.Text(
        wn,
        width = widgets_width,
        height = 10,
    )
    entry_text.config(
        fg = colors["console_text"],
        bg = colors["console_bg"],
        insertbackground = colors["console_text"],
    )
    entry_text.pack()

    button_add: tk.Button = tk.Button(
        wn,
        text = "Add",
        font = button_font,
        fg = colors["app_text"], 
        bg = colors["app_bg"],
        width = widgets_width - 19, # had to change widget width for my laptops resolution to match the size 
        command = lambda : add_to_file(entry_text),
    )
    button_add.pack()

    button_burn_file: tk.Button = tk.Button(
        wn,
        text = "Burn File",
        font = button_font,
        fg = colors["app_text"], 
        bg = colors["app_bg"],
        width = widgets_width - 19, # had to change widget width for my laptops resolution to match the size
        command = lambda : burn_file(entry_text),
    )
    button_burn_file.pack()

    button_clear_screen: tk.Button = tk.Button(
        wn,
        text = "Clear Screen",
        font = button_font,
        fg = colors["app_text"], 
        bg = colors["app_bg"],
        width = widgets_width - 19, # had to change widget width for my laptops resolution to match the size
        command = lambda : clear_screen(entry_text),
    )
    button_clear_screen.pack()

    # keep window open
    wn.mainloop()


def add_to_file(entry: tk.Text) -> None:
    """Function that appends entered text into the memo.txt file and clears the screen"""

    with open("memo.txt", "a") as f:
        f.write(entry.get("1.0", "end"))
        entry.delete("1.0", "end")
    

def burn_file(entry: tk.Text) -> None:
    """function that deletes the memo.txt file if it exists or prints that it does not exist to the entry if it doesn't"""

    if os.path.exists("memo.txt"):
        os.remove("memo.txt")
        entry.delete("1.0", "end") # deleting entered text before outputting file notification to avoid cluster and confusion
        entry.insert("1.0", "File Burned!")
    else:
        entry.delete("1.0", "end") # deleting entered text before outputting file notification to avoid cluster and confusion
        entry.insert("1.0", "File does not exist.")
    

def clear_screen(entry: tk.Text) -> None:
    """function that clears the entry screen"""

    entry.delete("1.0", "end")


main()