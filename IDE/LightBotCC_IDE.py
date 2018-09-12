import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from tkinter import Frame
from tkinter import Menu
from tkinter import Toplevel
from tkinter import BOTH
from tkinter import Label
from tkinter import END
from tkinter import Tk


class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)

class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or 
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result 



class Window(Frame):

    def __init__(self, master = None, *args, **kwargs):
        Frame.__init__(self, master, *args, *kwargs)
        self.master = master
        
        self.textField = CustomText(self)
        self.verticalScrollBar = tk.Scrollbar(orient = "vertical",
            command = self.textField.yview)
        self.textField.configure(yscrollcommand = self.verticalScrollBar.set)
        self.textField.tag_configure("bigfont", font = ("Helvetica", "24", "bold"))
        self.lineNumbers = TextLineNumbers(self, width = 30)
        self.lineNumbers.attach(self.textField)

        self.verticalScrollBar.pack(side = "right", fill = "y")
        self.lineNumbers.pack(side = "left", fill = "y")
        self.textField.pack(side = "right", fill = "both", expand = True)

        self.textField.bind("<<Change>>", self._on_change)
        self.textField.bind("<Configure>", self._on_change)

        self.init_window()

    def _on_change(self, event):
        self.lineNumbers.redraw()

    def init_window(self):
        self.master.title("IDE")
        self.pack(fill=BOTH, expand =1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        options = Menu(menu)
        run = Menu(menu)
        menu.add_cascade(label = "File", menu = file)
        menu.add_cascade(label = "Options", menu = options)
        menu.add_cascade(label = "Run", menu = run)

        file.add_command(label="Open", command = self.open_file)
        file.add_command(label="Save", command = self.save_file)

        options.add_command(label = "Theme", command = self.client_theme)
        options.add_command(label="Exit", command = self.client_exit)

        run.add_command(label = "Run...", command = self.run_file)

    def client_theme(self):
        toplevel = Toplevel()
        label1 = Label(toplevel, text = "Te mamaste", height=10, width=40)
        label1.option_add("Ok", "Ok")
        label1.pack()

    def client_exit(self):
        exit()

    def open_file(self):
        name = askopenfilename(initialdir = "~/Desktop",
                                filetypes = (("Text File", "*.txt"), 
                                    ("All Files", "*.*")),
                                    title = "Choose a file.")
        try:
            with open(name, 'r') as UseFile:
                self.textField.delete('1.0', END)
                self.textField.insert('1.0', UseFile.read())
        except:
            return

    def save_file(self):
        file = asksaveasfile(mode = 'w', defaultextension = ".txt")
        text2save = self.textField.get('1.0', END)
        file.write(text2save)
        file.close()

    def run_file(self):
        print("run_file(self)")
        
    


root = Tk()
root.geometry ("745x720")
app = Window(root)
root.mainloop()
