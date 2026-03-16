import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f7f6") 
        
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
        
        tk.Label(
            self.button_frame, 
            text="Button Grid", 
            bg="#f4f7f6", 
            fg="#8c96b0",
            font=("Segoe UI", 12)
        ).pack(pady=100)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()