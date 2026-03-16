import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f7f6") 
        
        self.display = tk.Entry(
            self.root, 
            font=("Segeo UI", 32, "bold"),
            bg="#ffffff",
            fg="#2c3e50",
            borderwidth=0,
            justify="right"
        )
        
        self.display.pack(
            expand=False, 
            fill="both", 
            ipady=20,
            pady=20,
            padx=20
        )
        
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

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()