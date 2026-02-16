import tkinter as tk
from tkinter.font import Font


def main():
    """Calculator application by Riley Tuttle"""

    # Setting up a window
    wn: tk.Tk = tk.Tk()
    wn.title("Calculator")
    basic_font: Font = Font(family = "Consolas", size = 20)
    large_font: Font = Font(family = "Consolas", size = 40)

    # Adding widgets
    exp_entry: tk.Entry = tk.Entry(wn, font=basic_font)
    eq_label: tk.Label = tk.Label(wn, text=" = ", font=basic_font)
    result_label: tk.Label = tk.Label(wn, text="0", font=large_font)
    calc_button: tk.Button = tk.Button(
        wn, 
        text="Calculate", 
        font=basic_font,
        command=lambda : calculate(exp_entry, result_label),
    )

    # Add widgets to layout
    # Get the result_label under the entry and =, but above the button
    # All i did was change the row value to 1 for result_label.grid and take away the 
    # column to be able to center it with columnspan right above the calc button
    # I also made a new font variable called "large_font" that kept the same font but 
    # increased the size to get the acquired bigger size for the result I was after
    
    exp_entry.grid(row=0, column=0)
    eq_label.grid(row=0, column=1)
    result_label.grid(row=1, columnspan=3)
    calc_button.grid(row=2, columnspan=3)

    # Keep program going

    wn.mainloop()


def calculate(exp_entry: tk.Entry, results_label: tk.Label) -> None:
        """Evaluate the expression and update the result."""

        expression: str = exp_entry.get()
        result: str = str(eval(expression)) # Not safe...
        results_label["text"] = result


main()