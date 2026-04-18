import tkinter as tk
from tkinter.font import Font

from week_11_mod import Stack, Queue


class Boxes: 
    """A container for objects of type Box."""

    def __init__(
            self, 
            struct: Stack | Queue,
            frame: tk.Frame,
            font: Font,           
            output: tk.Label,
            entry: tk.Entry,
            ) -> None: 
        """Class to manage the boxes."""

        self.struct: Stack | Queue = struct
        self.frame: tk.Frame = frame
        self.font: Font = font
        self.output: tk.Label = output
        self.entry: tk.Entry = entry

    def add_box(self) -> None:
        """Add a box to the structure with a value."""

        value: str = self.entry.get()
        box: Box = Box(self.frame, value, self.font)
        self.struct.enter_item(box)
        self.output.config(text=" ")
        self.entry.delete(0, tk.END)

        self.update_window()

    def get_box(self) -> None:
        """Remove a box from the structure."""

        if self.struct.is_empty():
            self.output.config(text="Empty")
            return
        
        box: Box = self.struct.get_value()
        box.label.pack_forget()
        self.output.config(text=box.text)
        self.update_window()

    def peek_box(self) -> None:
        """Show next box"""

        if self.struct.is_empty():
            self.output.config(text="Empty")
            return
        
        box: Box = self.struct.view_next()
        self.output.config(text=box.text)

    def update_window(self) -> None:
        """Update the canvas with the boxes."""

        for box in self.struct.items:
            box.label.pack_forget()
        for box in self.struct.items:
            box.label.pack()


class Box: 
    """A class that represents a box."""

    def __init__(self, parent: tk.Frame, text: str, font: Font) -> None: 
        """Create a box."""

        self.text: str = text
        self.label: tk.Label = tk.Label(parent, text=self.text, font=font)


if __name__ =="__main__":
    print("This is a module...")