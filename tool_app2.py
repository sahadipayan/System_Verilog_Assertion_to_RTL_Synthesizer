# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 18:19:22 2022

@author: dipay
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 03:38:47 2022

@author: dipay
"""

import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

from RTL_Generator2 import RTL_Generator2
from sva_parser2 import sva_parser2

root=tk.Tk()

canvas = tk.Canvas(root, width=300, height=300,bg="#2820be")
canvas.grid(columnspan=5, rowspan =6 )
#canvas.pack()
frame=tk.Frame(root,bg="#2820be")
frame.place(relwidth=1,relheight=1, relx=0,rely=0)


instructions=tk.Label(root, text = "System Verilog Assertion (SVA) to RTL Synthesizer",font=("Arial", 24),foreground='white',bg="#2820be")

instructions.grid(column=0,row=0)


logo=Image.open('universityofflorida3.jpg')
logo= ImageTk.PhotoImage(logo)

logo_lable =tk.Label(image=logo)
logo_lable.image = logo
logo_lable.grid(column=0,row=1,sticky="N")
#logo_lable.tag_configure("certer",justify="center")
        #text_box.tag_add("center", 1,"end")
#logo_lable.pack()

#logo2=Image.open('C:\\Users\\dipay\\Downloads\\cad_project\\ECE-Avatar.png')
#logo2= ImageTk.PhotoImage(logo2, size=[30,30])
#logo_lable2 =tk.Label(image=logo2)
#logo_lable2.image = logo2
#logo_lable2.grid(column=1,row=1,sticky="N")


instructions=tk.Label(root, text = "Step 1: Click 'Browse' to select file to generate synthesized RTL", font=20,foreground='white',bg="#2820be")

instructions.grid(column=0,row=2,sticky="W")

instructions2=tk.Label(root, text = "Step 2: Click 'Open' to view generated verilog module", font=20,foreground='white',bg="#2820be")

instructions2.grid(column=0,row=3,sticky="W")

import subprocess as sp

global file1

def open_file():
    browse_text.set("Loading...")
    file1 = askopenfile(parent=root, mode='rb', title="Choose a file",filetypes=[(("SVA file", "*.sv"),("All Files","*.*"))])
    
    if file1:
        browse_text.set("Uploaded")
        #print(file1)
        

        file=open(file1.name,'r')
    #file=io.BufferedReader(file)
        lines=file.readlines()
        #print(lines)
        lines2=[]
        for line in lines:
            line=line.strip()
            lines2.append(line+'\n')
            
    
        text_box=tk.Text(root, height=10, width=80)
        text_box.insert(1.0,lines2)
        #text_box.tag_configure("certer",justify="center")
        #text_box.tag_add("center", 1,"end")
        text_box.grid(column=0,row=5)
        
        
        #import numpy as np 
        #file=open(file1.name,'r')

        #lines=file.readlines()
 
        
        count=0
        for line in lines:
            line=line.strip()
            if line.find('property') == -1 and len(line) !=0:
                RTL_Generator2(line,count)
                count=count+1
        browse_text.set("Browse")
   

    #filepath='C:/Users/dipay/Downloads/cad_project/sv_property1.sv'

def open_file2():
    browse_text2.set("Opening")
    #filepath2 = askopenfile(initialkinzer dir="C:/Users/dipay/Downloads/cad_project/",parent=root, mode='rb', title="Choose a file",filetypes=[("SVA file", "*.sv")])
    
    #file=open(filepath2.name,'r')
    #file.close()
    
    programName = "notepad.exe"
    filename='genarated_module_0'
    filepath = filename+".v"
    sp.Popen([programName, filepath])
        #text_box=tk.Text(root, height=5, width=80,padx=10,pady=10)
        #text_box.insert(1.0,lines)
        #text_box.tag_configure("certer",justify="center")
        #text_box.tag_add("center", 1,"end")
        #text_box.grid(column=1,row=3)
        
    browse_text2.set("Opened")

    
    
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font=("Raleway",12),bg="#2820be", fg="white", height=1, width=15)

browse_text.set("Browse")

browse_btn.grid(column=0, row=2,sticky="E")

global file1
#file3=file1.name
#filename=file3.split('/')[-1][0:-3]


browse_text2 = tk.StringVar()
browse_btn2 = tk.Button(textvariable=browse_text2, command=lambda:open_file2(), font=("Raleway",12), bg="#2820be", fg="white", height=1, width=15)

browse_text2.set("Open")

browse_btn2.grid(column=0, row=3,sticky="E")

canvas = tk.Canvas(root, width=60, height=60,bg="#2820be")
canvas.config(highlightbackground = "#2820be", highlightcolor= "#2820be")
#canvas = tk.Canvas(root, width=300, height=300)
canvas.grid(columnspan=4)
root.mainloop()
