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
        #nastavení geometrie
        self.label_1.pack(side=tkinter.TOP, fill=tkinter.X, expand=True)
        self.label_2.pack(side=tkinter.BOTTOM, fill=tkinter.Y, expand=True)


root = tkinter.Tk()
app = MainWindow(root)
app.mainloop()