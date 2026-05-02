import tkinter as tk
from tkinter.font import Font

from week_14_mod import Color, CommandCenter


def main() -> None: 
    """Base Converter app by Riley Tuttle."""

    wn: tk.Tk = tk.Tk()
    wn.title("Base Converter")
    wn.configure(bg=Color.background)
    font_style: Font = Font(wn, family="Consolas", size=20)
    output_font_style: Font = Font(wn, family="Consolas", size=40)

    number_entry: tk.Entry = tk.Entry(
        wn,
        font=font_style,
        bg=Color.widget,
        fg=Color.text,
        insertbackground=Color.text,
    )

    choices: tuple = ("Binary", "Octal", "Decimal", "Hexadecimal")
    base_input_sbox: tk.Spinbox = tk.Spinbox(
        wn,
        font=font_style,
        values=choices,
        fg=Color.text,
        state="readonly",
        readonlybackground=Color.widget,
        buttonbackground=Color.widget,
    )
    base_output_sbox: tk.Spinbox = tk.Spinbox(
        wn,
        font=font_style,
        values=choices,
        fg=Color.text,
        state="readonly",
        readonlybackground=Color.widget,
        buttonbackground=Color.widget,
    )

    result_label: tk.Label = tk.Label(
        wn,
        text="-",
        font=output_font_style,
        bg=Color.background,
        fg=Color.text,
    )

    command_center: CommandCenter = CommandCenter(
        number_entry,
        base_input_sbox,
        base_output_sbox,
        result_label,
    )

    convert_button: tk.Button = tk.Button(
        wn,
        command=command_center.convert,
        text="Convert",
        font=font_style,
        bg=Color.widget,
        fg=Color.text,
        activebackground=Color.text,
        activeforeground=Color.widget,
    )

    logo: tk.PhotoImage = tk.PhotoImage(master=wn, file="logo.png")
    logo = logo.subsample(2)
    logo_label: tk.Label = tk.Label(wn, image=logo, bg=Color.background)

    padx: int = 10
    pady: int = 5
    number_entry.pack(fill=tk.X, padx=padx, pady=pady)
    base_input_sbox.pack(fill=tk.X, padx=padx, pady=pady)
    base_output_sbox.pack(fill=tk.X, padx=padx, pady=pady)
    convert_button.pack(fill=tk.X, padx=padx, pady=pady)
    result_label.pack(fill=tk.X, padx=padx, pady=pady)
    logo_label.pack(fill=tk.X, padx=padx, pady=pady)

    wn.mainloop()
    

if __name__ == "__main__":
    main()