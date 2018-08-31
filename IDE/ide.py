from tkinter import *
from tkinter import filedialog


class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("IDE")
        self.pack(fill=BOTH, expand =1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        menu.add_cascade(label = "File", menu = file)

        file.add_command(label="Open", command = self.open_file)
        file.add_command(label="Save", command = self.save_file)
        file.add_command(label="Exit", command = self.client_exit)


        runButton = Button(self, text="RUN", command = self.run_file)
        runButton.place (x = 0, y = 0)
        


    def client_exit(self):
        exit()

    def open_file(self):
        print("open_file(self)")
        root.filename = filedailog.askopenfilename(initialdir = "C:/Users/curso/Desktop",title = "Select file",filetypes = (("text file","*.txt"),("all files","*.*")))
        print (root.filename)

    def save_file(self):
        print("save_file(self)")

    def run_file(self):
        print("run_file(self)")
        
    





root = Tk()
root.geometry ("720x480")
app = Window(root)

root.mainloop()
