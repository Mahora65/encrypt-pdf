from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import function


class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("PDF Encrypter")
        self.minsize(600,400)
        self.excel_frame()
        self.pdf_frame()
        self.load_frame()


    def excel_frame(self):
        self.x = 10
        self.labelframe = ttk.LabelFrame(self)
        self.labelframe.place(relwidth = 0.8, relheight = 0.3, relx = 0.1, rely = 0.1)
        self.button = ttk.Button(self.labelframe, text="Select File", command = self.fileDialog)
        self.button.place(relx = 0.75, rely =0.5, width = 100, height = 25)
        self.label = ttk.Label(self.labelframe, text='The configurated file path:')
        self.label.place(relx = 0.1, rely=0.2)
        self.e_entry = ttk.Entry(self.labelframe)
        self.e_entry.place(relx = 0.1, rely =0.5, relwidth = 0.6, height = 25)


    def pdf_frame(self):
        self.labelframe = ttk.LabelFrame(self)
        self.labelframe.place(relwidth = 0.8, relheight=0.3, relx =0.1, rely = 0.4)
        self.button = ttk.Button(self.labelframe, text="Select Path", command = self.dirDialog)
        self.button.place(relx = 0.75, rely =0.5, width = 100, height = 25)
        self.label = ttk.Label(self.labelframe, text='The PDF files path:')
        self.label.place(relx = 0.1, rely=0.2)
        self.p_entry = ttk.Entry(self.labelframe)
        self.p_entry.place(relx = 0.1, rely =0.5, relwidth = 0.6, height = 25)

    def load_frame(self):
        self.labelframe = ttk.LabelFrame(self)
        self.labelframe.place(relwidth = 0.8, relheight=0.2, relx = 0.1, rely = 0.7)
        self.button = ttk.Button(self.labelframe, text="Encrypt", command = lambda: function.main(self.e_entry.get(),self.p_entry.get()))
        self.button.place(relx=0.75, rely=0.4, width=100, height=25)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("Excel Workbook","*.xlsx"),
         ("Excel Marco-Enabled Workbook","*.xlsm"),
         ("Excel Template","*.xltx"),
         ("Excel Marco-Enabled Template","*.xltm"),
         ("Excel 97-2003 Worksheet","*.xls"),
         ("Excel 97-2003 Template","*.xlt"),
         ("Excel 97-2003 Macro",".xlm"),
         ("all files","*.*")))
        self.e_entry.insert(0,self.filename)


    def dirDialog(self):
        self.dirpath = filedialog.askdirectory()
        self.p_entry.insert(0,self.dirpath)

    def popup(self):
        root = Tk()
        root.title('Pop-Up windows')
        w = 300
        h = 200
        sw=root.winfo_screenwidth()
        sh=root.winfo_screenheight()
        x=(sw-w)/2
        y=(sh-h)/2
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))


root=Root()
root.mainloop()