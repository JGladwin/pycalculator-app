import tkinter as tk

SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 40, "bold")
DIGIT_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20, "bold")

SAKURA_PINK = "#f3bad8"
SAKURA_PINK_BORDER = "#f6d6e7"
LABEL_COLOR = "#d48ea7"

class Calculator():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("300x500")

        self.total_expr = "0"
        self.current_expr = "0"

        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        self.digits = {
                7:(1,1),8:(1,2),9:(1,3),
                4:(2,1),5:(2,2),6:(2,3),
                1:(3,1),2:(3,2),3:(3,3),
                ".":(4,1),0:(4,2)
        }

        self.operations = {"/" : "\u00F7", "*" : "\u00D7", "-" : "-", "+" : "+"}

        self.button_frame = self.create_button_frame()
        
        #for expanding the zeroth row to fit the size of the application
        self.button_frame.rowconfigure(0, weight=1)
        #for expanding the entire grid to fit the size of the application 
        for x in range(1,5):
            self.button_frame.rowconfigure(x, weight=1)     #what is the difference between weight=1 and weight=2?
            self.button_frame.columnconfigure(x, weight=1)
        
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        
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
        frame = tk.Frame(self.window, bg=SAKURA_PINK)
        frame.pack(expand=True, fill="both")
        return frame

    def create_operator_buttons(self):
        i=0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text=operator, bg=SAKURA_PINK_BORDER, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i+=1
            
    def create_clear_button(self):
            button = tk.Button(self.button_frame, text="C", bg=SAKURA_PINK_BORDER, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
            button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    def create_equals_button(self):
            button = tk.Button(self.button_frame, text="=", bg=SAKURA_PINK_BORDER, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
            button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg=SAKURA_PINK_BORDER, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=0)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()

        
