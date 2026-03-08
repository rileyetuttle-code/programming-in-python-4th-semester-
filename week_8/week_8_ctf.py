import tkinter as tk
from tkinter import filedialog
import re


def main() -> None: 
    """CTF program by Riley Tuttle"""

    colors: dict[str, str] = {
        "background": "gray",
        "text": "black",
        "flag": "blue",
    }
    font_style: tuple = ("Consolas", 30)

    window: tk.Tk = tk.Tk()
    window.title("Capture the Flag")
    window.geometry("1000x150") # made wider for my computer screen
    window.configure(bg = colors["background"])

    # Top Frame
    top_frm: tk.Frame = tk.Frame(
        window,
    )
    top_frm.pack(
        anchor = tk.W,
        padx = 10,
        pady = 10,
    )

    flag_lbl: tk.Label = tk.Label(
        top_frm,
        text = "Flag:",
        font = font_style,
        fg = colors["text"],
        bg = colors["background"],
    )
    flag_lbl.pack(side = tk.LEFT)

    flag_value_lbl: tk.Label = tk.Label(
        top_frm,
        text = "",
        font = font_style,
        fg = colors["flag"],
        bg = colors["background"],
    )
    flag_value_lbl.pack(side = tk.LEFT)

    # Bottom Frame
    bottom_frm: tk.Frame = tk.Frame(
        window,
    )
    bottom_frm.pack(
        fill=tk.BOTH,
        padx = 10,
        pady = 10,
    )

    search_btn: tk.Button = tk.Button(
        bottom_frm,
        text = "SEARCH",
        font = font_style,
        command = lambda : search_for_flag(flag_value_lbl),
    )
    search_btn.pack(fill=tk.BOTH)

    window.mainloop()


def search_for_flag(flag_value_lbl: tk.Label) -> None:
    """Find flag in file and update label with result"""

    filename: str = filedialog.askopenfilename()

    # Open the file and search for the flag
    with open(filename, "r") as f:
        text: str = f.read()

    pattern: str = r"FLAG((-{1,3})(\w+)(-{1,3})|(>{1,2})(\w+)(<{1,2}))" # this pattern works by mainly testing the two separate main cases that are said to be used: 1. a range of 1-3 hyphens followed by any word characaters then another 1-3 hyphens, OR (|) 2. 1-2 greater than symbols followed by any word characters followed by 1-2 less than symbols. Either of these types of flags are inside of a bigger group of parenthesis that go after the FLAG to find the actual flag in the text
    results = re.search(pattern, text)

    if results:
        flag_value_lbl.config(text = results.group())
    else:
        flag_value_lbl.config(text = "None")


main()