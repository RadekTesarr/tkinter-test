import tkinter

class MainWindow(tkinter.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("Tkinter GUI test")
        self.parent.rowconfigure(0, weight=500) # row set
        self.parent.rowconfigure(1, weight=500) # row set
        self.parent.columnconfigure(0, weight=1000) # column set
        self.parent.minsize(500, 200)   # min. window size
        self.create_widgets()

    def create_widgets(self):
        self.label_1 = tkinter.Label(text="Hello world!", bg="white")
        self.label_2 = tkinter.Label(text="Hello world!", bg="yellow")
        
        # '''GEOMETRY SETTINGS'''
        # self.label_1.pack(side=tkinter.TOP, fill=tkinter.X, expand=True)
        # self.label_2.pack(side=tkinter.BOTTOM, fill=tkinter.Y, expand=True)
        
        # '''METOD PLACE'''
        # self.label_1.place(x=40, y=60, anchor=tkinter.N)
        # self.label_2.place(x=40, y=60, anchor=tkinter.S)
        
        '''METOD GRID'''
        self.label_1.grid(row=0, column=0, sticky=tkinter.NSEW)
        self.label_2.grid(row=1, column=0, sticky=tkinter.NSEW)



root = tkinter.Tk()
app = MainWindow(root)
app.mainloop()