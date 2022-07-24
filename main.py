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

        self.total_expr = ""
        self.current_expr = ""

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
        self.bind_keys()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()
        
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
            button = tk.Button(self.button_frame, text=symbol, bg=SAKURA_PINK_BORDER, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i+=1
            
    def create_clear_button(self):
            button = tk.Button(self.button_frame, text="C", bg=SAKURA_PINK_BORDER, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.clear)
            button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_square_button(self):
            button = tk.Button(self.button_frame, text="x\u00b2", bg=SAKURA_PINK_BORDER, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.square)
            button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_sqrt_button(self):
            button = tk.Button(self.button_frame, text="\u221ax", bg=SAKURA_PINK_BORDER, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.sqrt)
            button.grid(row=0, column=3, sticky=tk.NSEW)

    def create_equals_button(self):
            button = tk.Button(self.button_frame, text="=", bg=SAKURA_PINK_BORDER, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.evaluate)
            button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg=SAKURA_PINK_BORDER, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=0, command=lambda x=digit: self.add_to_expr(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    #Implementing functionality from here

    def add_to_expr(self, value):
        self.current_expr += str(value)
        self.update_label()

    def update_total_label(self):
        expression = self.total_expr
        for operator,symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expr[:9])

    def append_operator(self, operator):
        self.current_expr += operator
        self.total_expr += self.current_expr
        self.current_expr = ""
        self.update_total_label()
        self.update_label()

    def clear(self):
        self.current_expr = ""
        self.total_expr = ""
        self.update_label()
        self.update_total_label()

    def evaluate(self):
        self.total_expr += self.current_expr
        self.update_total_label()

        try:
            self.current_expr = str(eval(self.total_expr))

            self.total_expr = ""

        except Exception as e:
            self.current_expr = "Error"

        finally:
            self.update_label()

    def square(self):
        self.current_expr = str(eval(f"{self.current_expr}**2"))
        self.update_label()

    def sqrt(self):
        self.current_expr = str(eval(f"{self.current_expr}**0.5"))
        self.update_label()
        
    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        self.window.bind("=", lambda event: self.evaluate())

        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expr(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()

        
