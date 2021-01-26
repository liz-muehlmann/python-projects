############# Create 10 weeks of Folders #############
## UCI is on the quarter system and I like to keep my readings organized.
## This file uses a file dialog GUI to let you select where you want 10 folders created
## I have them named by weeks (Line 17) because that's easiest for me.

#import
import os, sys, tkinter.filedialog, getpass, tkinter
from tkinter import *
from tkinter.filedialog import askdirectory


gui = tkinter.Tk()
def click():
    root = tkinter.Tk()
    dir = tkinter.filedialog.askdirectory(parent=root,initialdir='/',title='Please select a directory')
    os.chdir(dir)
    folders = ["Week 1","Week 2","Week 3","Week 4","Week 5","Week 6","Week 7","Week 8","Week 9","Week 10"]

    for folder in folders:
        os.mkdir(folder)


click()
