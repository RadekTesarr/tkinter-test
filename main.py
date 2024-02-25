import tkinter

class MainWindow(tkinter.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("První GUI aplikace")
        self.create_widgets()

    def create_widgets(self):
        self.label_1 = tkinter.Label(text="Hello world!", bg="white") # bílý label
        self.label_2 = tkinter.Label(text="Hello world!", bg="yellow") # žlutý label
        self.label_1.place(x=40, y=60, anchor=tkinter.N)
        self.label_2.place(x=40, y=60, anchor=tkinter.S)


root = tkinter.Tk()
app = MainWindow(root)
app.mainloop()