import tkinter as tk

SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 40, "bold")

SAKURA_PINK = "#f3bad8"
SAKURA_PINK_BORDER = "#d48ea7"
LABEL_COLOR = "#f6d6e7"

class Calculator():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("300x500")

        self.total_expr = "0"
        self.current_expr = "0"

        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        self.button_frame = self.create_button_frame()

    def create_display_labels(self):
       total_label = tk.Label(self.display_frame,text=self.total_expr, anchor=tk.E, bg=SAKURA_PINK, fg=LABEL_COLOR, padx = 24, font=SMALL_FONT_STYLE)
       total_label.pack(expand=True, fill="both")

       label = tk.Label(self.display_frame,text=self.current_expr, anchor=tk.E, bg=SAKURA_PINK, fg=LABEL_COLOR, padx = 24, font=LARGE_FONT_STYLE)
       label.pack(expand=True, fill="both")
       return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=SAKURA_PINK)
        frame.pack(expand=True, fill="both")
        return frame


    def create_button_frame(self):
        frame = tk.Frame(self.window, bg=SAKURA_PINK_BORDER)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()

        
