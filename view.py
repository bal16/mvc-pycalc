import tkinter as tk
from tkinter import ttk
from typing import Literal


class View(tk.Tk):
    PADDING = 10

    MAX_BUTTONS_PER_ROW = 4

    BUTTON_CAPTIONS = [
        'C', '+/-', '%', '/',
        7,       8,   9, '*',
        4,       5,   6, '-',
        1,       2,   3, '+',
        0,     '.', '='
    ]

    def __init__(self, controller):
        self.controller = controller
        
        super().__init__()
        self.title("PyCalc")
        self.config(background='black')
        self.__config_btn_style()

        self.value_var = tk.StringVar(value='0')

        self.__init_main_frame()
        self.__init_label()
        self.__init_buttons()

        self.__center_window()

    def main(self):
        self.mainloop()

    def __init_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(
            padx=self.PADDING,
            pady=self.PADDING
        )

    def __init_label(self):
        entry = tk.Label(
            self.main_frame,
            anchor='e',
            textvariable=self.value_var,
            bg='black',
            fg='white',
            font=('Arial', 30)
        )
        entry.pack(fill='x')

    def __init_buttons(self):
        outer_frame = ttk.Frame(self.main_frame)
        outer_frame.pack()

        is_first_row = True
        frame = ttk.Frame(outer_frame)
        frame.pack(fill='x')

        btn_in_row = 0

        for caption in self.BUTTON_CAPTIONS:
            if isinstance(caption, int):
                style_prefix = 'N'
            elif self.__is_operator(caption):
                style_prefix = 'O'
            else:
                style_prefix = 'M'

            style_name = f'{style_prefix}.TButton'
            if is_first_row or btn_in_row == self.MAX_BUTTONS_PER_ROW:
                is_first_row = False

                frame = ttk.Frame(outer_frame)
                frame.pack(
                    fill='x'
                )

                btn_in_row = 0


            btn = ttk.Button(
                frame,
                text=caption,
                command=(lambda button=caption: self.controller.click_btn(button)),
                style=style_name,
                width=7
            )

            fill: Literal["none", "x", "y", "both"] = 'none'
            expand: Literal[0,1] = 0

            if caption == 0:
                fill= 'x'
                expand= 1

            btn.pack(
                side='left',
                expand=expand,
                fill=fill
            )

            btn_in_row += 1

    def __center_window(self):
        self.update()

        width = self.winfo_width()
        height = self.winfo_height()

        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2

        self.geometry(
            f'{width}x{height}+{x_offset}+{y_offset}'
        )

    @staticmethod
    def __config_btn_style():
        style = ttk.Style()
        font = ('Arial', 12)

        style.theme_use('alt')

        # number button
        style.configure(
            'N.TButton',
            background='gray',
            foreground='white',
            font=font
        )

        # operator button
        style.configure(
            'O.TButton',
            background='orange',
            foreground='black',
            font=font
        )

        # misc button
        style.configure(
            'M.TButton',
            background='white',
            font=font
        )

    @staticmethod
    def __is_operator(caption):
        return caption in ['+', '-', '*', '/', '=']
