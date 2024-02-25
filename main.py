import tkinter

class MainWindow(tkinter.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("První GUI aplikace")
        self.create_widgets()

root = tkinter.Tk()
app = MainWindow(root)
app.mainloop()