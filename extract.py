from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
import os

GUI = Tk()
GUI.title('Text Extractor')
GUI.geometry('500x400')

L1 = Label(GUI, text='Choose the .txt file')
L1.place(x=20,y=60)

def openfile():
    input_filename = fd.askopenfilename(title="Select Input file")
    if input_filename == '':
        return
    output_dir = fd.askdirectory(title='Select Output Directory')
    if output_dir == '':
        return
    input_basename = os.path.basename(input_filename)
    output_filename = os.path.join(output_dir, os.path.splitext(input_basename)[0] + '_new.txt')
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for line in input_file:
                if "Text" in line:
                    output_file.write(line)
    messagebox.showinfo('Success', 'Finished Extraction')

#showsign warning error
FB1 = Frame(GUI)
FB1.place(x=20,y=80)
B1 = ttk.Button(FB1,text='Choose', command=openfile)
B1.pack(ipadx=20,ipady=20)


GUI.mainloop()

#B1 = ttk.Button(FB1,text='Choose', command=openfile)
#B1.pack(ipadx=20,ipady=20)
#B1.place(x=20,y=80)
# output_filename = os.path.splitext(os.path.basename(input_filename))[0] + ".txt"
#output_filename = fd.askdirectory(title="Select Output Directory", defaultextension=".txt", initialdir=os.getcwd())