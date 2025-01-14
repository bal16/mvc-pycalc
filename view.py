import tkinter as tk
from tkinter import ttk
from tkinter.constants import DISABLED


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
        super().__init__()
        self.title("PyCalc")

        self.controller = controller

        self.value_var = tk.StringVar(value='0')

        self.__init_frame()
        self.__init_entry()
        self.__init_buttons()

        self.__center_window()

    def main(self):
        self.mainloop()

    def __init_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(
            padx=self.PADDING,
            pady=self.PADDING
        )

    def __init_entry(self):
        entry = ttk.Entry(
            self.main_frame,
            justify='right',
            textvariable=self.value_var,
            state=DISABLED
        )
        entry.pack(fill='x')

    def __init_buttons(self):
        outer_frame = ttk.Frame(self.main_frame)
        outer_frame.pack()

        frame = ttk.Frame(outer_frame)
        frame.pack()

        btn_in_row = 0

        for caption in self.BUTTON_CAPTIONS:
            if btn_in_row == self.MAX_BUTTONS_PER_ROW:
                frame = ttk.Frame(outer_frame)
                frame.pack()
                btn_in_row = 0

            btn = ttk.Button(
                frame,
                text=caption,
                command=(lambda button=caption: self.controller.click_btn(button)),
            )
            btn.pack(side='left')

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