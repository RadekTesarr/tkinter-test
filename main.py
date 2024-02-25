import tkinter

class MainWindow(tkinter.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("První GUI aplikace")
        self.parent.rowconfigure(0, weight=500) # nastavení řádku
        self.parent.rowconfigure(1, weight=500) # nastavení řádku
        self.parent.columnconfigure(0, weight=1000) # nastavení sloupce
        self.parent.minsize(500, 200)   # minimální velikost okna
        self.parent.resizable(True) # měnitelnost okna
        self.create_widgets()

    def create_widgets(self):
        self.label_1 = tkinter.Label(text="Hello world!", bg="white") # bílý label
        self.label_2 = tkinter.Label(text="Hello world!", bg="yellow") # žlutý label
        '''NASTAVENÍ GEOMETRIE
        self.label_1.pack(side=tkinter.TOP, fill=tkinter.X, expand=True)
        self.label_2.pack(side=tkinter.BOTTOM, fill=tkinter.Y, expand=True)'''
        '''METODA PLACE
        self.label_1.place(x=40, y=60, anchor=tkinter.N)
        self.label_2.place(x=40, y=60, anchor=tkinter.S)'''
        '''METODA GRID'''
        self.label_1.grid(row=0, column=0, sticky=tkinter.NSEW)
        self.label_2.grid(row=1, column=0, sticky=tkinter.NSEW)



root = tkinter.Tk()
app = MainWindow(root)
app.mainloop()