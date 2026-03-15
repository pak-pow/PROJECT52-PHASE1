import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f7f6") 
        
        self.placeholder = tk.Label(
            self.root, 
            text="GUI Initialized", 
            font=("Segoe UI", 16), 
            bg="#f4f7f6", 
            fg="#2c3e50"
        )
        self.placeholder.pack(pady=200) 
        
    
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()