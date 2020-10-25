import PyPDF2
import os
import pandas as pd

class function():
    def __init__(self,excel_path,pdf_path):
        self.pdf_path = pdf_path
        self.df = pd.read_excel(excel_path)
        self.pass_df = self.df[["E-Name","Protection"]].copy()
        self.pass_df = self.pass_df.set_index("E-Name")
        for name in self.pass_df.index:
            for path in os.listdir(self.pdf_path):
                self.full_path = os.path.join(self.pdf_path,path)
                if os.path.isfile(self.full_path) and name + ".pdf" == path:
                    self.add_encryption(self.full_path, self.pass_df.loc[name, "Protection"])


    def add_encryption(self,input_pdf,password):
        self.input_pdf = input_pdf
        self.password = password
        self.output = PyPDF2.PdfFileWriter()
        self.input_stream = PyPDF2.PdfFileReader(open(self.input_pdf,"rb"))

        for i in range(0, self.input_stream.getNumPages()):
            self.output.addPage(self.input_stream.getPage(i))

        self.output_path = self.input_pdf[:-4]+"-Encrypted.pdf"
        self.output_stream = open(self.output_path,"wb")
        self.output.encrypt(self.password,use_128bit=True)
        self.output.write(self.output_stream)
        self.output_stream.close()