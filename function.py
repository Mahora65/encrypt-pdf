import PyPDF2
import os
import pandas as pd


#excel_path = r"C:\Users\z003yw3a\Desktop\01 Projects\Personal\encrypt-pdf\Test.xlsm"
#pdf_path = r"C:\Users\z003yw3a\Desktop\01 Projects\Personal\encrypt-pdf\Test data"


def add_encryption(input_pdf, password):
    output = PyPDF2.PdfFileWriter()
    input_stream = PyPDF2.PdfFileReader(open(input_pdf, "rb"))

    for i in range(0, input_stream.getNumPages()):
        output.addPage(input_stream.getPage(i))

    output_path = input_pdf[:-4]+"-Encrypted.pdf"
    output_stream = open(output_path, "wb")

    output.encrypt(password, use_128bit=True)
    output.write(output_stream)
    output_stream.close()


def main(excel_path, pdf_path):
    df = pd.read_excel(excel_path)
    pass_df = df[["E-Name", "Protection"]].copy()
    pass_df = pass_df.set_index("E-Name")
    for name in pass_df.index:
        for path in os.listdir(pdf_path):
            full_path = os.path.join(pdf_path, path)
            if os.path.isfile(full_path) and name + ".pdf" == path:
                add_encryption(full_path, pass_df.loc[name, "Protection"])