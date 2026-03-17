import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f7f6") 
        
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]
        
        """
        `self.display = tk.Entry(` is creating an Entry widget in the tkinter GUI application. An
        Entry widget is used to display a single-line text field where the user can enter or display
        text. In this case, it is being used as a display for the calculator where the user can see
        the input and output of the calculations.
        """
        self.display = tk.Entry(
            self.root, 
            font=("Segeo UI", 32, "bold"),
            bg="#ffffff",
            fg="#2c3e50",
            borderwidth=0,
            justify="right"
        )
        
        """
        `self.display.pack(` is configuring the layout of the Entry widget (`self.display`) within
        the tkinter GUI application. The `pack` method is used to organize widgets in blocks before
        placing them in the parent widget.
        """
        self.display.pack(
            expand=False, 
            fill="both", 
            ipady=20,
            pady=20,
            padx=20
        )
        
        """
        `self.button_frame = tk.Frame(` is creating a Frame widget in the tkinter GUI application. A
        Frame widget is a container that holds other widgets and helps in organizing the layout of
        the GUI components. In this case, `self.button_frame` is being used to group and organize
        the buttons that will be part of the calculator interface.
        """
        self.button_frame = tk.Frame(
            self.root,
            bg="#f4f7f6"
        )
        
        self.button_frame.pack(
            expand=True,
            fill="both",
            padx=20,
            pady=(0,20)
        )
        
        for (text, row, col) in buttons:
            btn = tk.Button(
                self.button_frame,
                text=text,
                font=("Segoe UI", 18, "bold"),
                bg="#ffffff",
                fg="#2c3e50",
                borderwidth=0,
                cursor="hand2"
            )

            btn.grid(
                row=row, 
                column=col, 
                sticky="nsew", 
                padx=5, 
                pady=5
            )
            
        for i in range(4):
            self.button_frame.grid_rowconfigure(i, weight=1)
            self.button_frame.grid_columnconfigure(i, weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()