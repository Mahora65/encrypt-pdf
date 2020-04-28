import tkinter as tk
import function


HEIGHT = 300
WIDTH = 600




root = tk.Tk()

canvas = tk.Canvas(root, height =HEIGHT, width=WIDTH)
canvas.pack()

excel_frame = tk.Frame(root, bg="blue")
excel_frame.place(relwidth = 0.8, relheight = 0.3, relx = 0.1, rely = 0.1)

excel_lable = tk.Label(excel_frame, text='The configurated file path:')
excel_lable.place(relx = 0.1, rely=0.2)

excel_entry = tk.Entry(excel_frame)
excel_entry.place(relx = 0.1, rely =0.5, relwidth = 0.6, height = 25)

excel_button = tk.Button(excel_frame, text = 'Browse')
excel_button.place(relx = 0.75, rely =0.5, width = 100, height = 25)

pdf_frame = tk.Frame(root, bg="red")
pdf_frame.place(relwidth = 0.8, relheight=0.3, relx =0.1, rely = 0.4)

pdf_lable = tk.Label(pdf_frame, text='The PDF files path:')
pdf_lable.place(relx = 0.1, rely=0.2)

pdf_entry = tk.Entry(pdf_frame)
pdf_entry.place(relx = 0.1, rely =0.5, relwidth = 0.6, height = 25)

pdf_button = tk.Button(pdf_frame, text = 'Browse')
pdf_button.place(relx = 0.75, rely =0.5, width = 100, height = 25)

load_frame = tk.Frame(root, bg="green")
load_frame.place(relwidth = 0.8, relheight=0.2, relx = 0.1, rely = 0.7)

load_button = tk.Button(load_frame, text = 'Encrypt')
load_button.pack()

root.mainloop()