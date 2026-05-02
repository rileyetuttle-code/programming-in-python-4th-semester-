import tkinter as tk


class Color: 
    """Color class to store color values used in the program."""

    background: str = "#000F6E"
    widget: str = "#1600DD"
    text: str = "#FFFFFF"


class CommandCenter: 
    """Class for handling button commands."""

    def __init__(
        self,
        entry: tk.Entry,
        input_base: tk.Spinbox,
        output_base: tk.Spinbox,
        output: tk.Label,
    ) -> None: 
        """Passes needed widgets into the object."""

        self.entry: tk.Entry = entry
        self.input_base: tk.Spinbox = input_base
        self.output_base: tk.Spinbox = output_base
        self.output: tk.Label = output

    def convert(self) -> None: 
        """Convert number from input base to output base."""

        # Number
        number_input: str = self.entry.get()
        input_base: str = self.input_base.get()
        output_base: str = self.output_base.get()
        
        # convert to decimal
        try: 
            number_dec: int = 0
            if input_base == "Binary":
                number_dec = int(number_input, 2)
            elif input_base == "Octal":
                number_dec = int(number_input, 8)
            elif input_base == "Decimal":
                number_dec = int(number_input, 10)
            elif input_base == "Hexadecimal":
                number_dec = int(number_input, 16)
        except ValueError:
            self.output.config(text="Invalid Number")
            return
    

        # convert output base
        number_output: str = ""
        if output_base == "Binary":
            number_output = bin(number_dec)[2:]
        elif output_base == "Octal":
            number_output = oct(number_dec)
        elif output_base == "Decimal":
            number_output = str(number_dec)
        elif output_base == "Hexadecimal":
            number_output = hex(number_dec)[2:].upper()

        # update label
        self.output.config(text=number_output)