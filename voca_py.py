#vocab flashcard practice
#table of contents
#1. csv set up
#2. tkinter set up

import random

#CSV SET UP
import csv

def read_file():
    with open('vocab_listing.csv') as vocab_csv:
        pass
    
def generate_flashcards():
    unknown_list = []
    known_list = []

    #read csv file
    #update two lists
    #scramble both lists
    #display to tkinter

def add_vocab():
    with open('vocab_listing.csv') as vocab_csv:
        #read original file

        #rewrite whole file
        #add one new line
        line_writer=csv.writer(vocab_csv, delimiter=',')

def delete_vocab():
    #find index of listbox
    #read csv file
    #copy to list
    #delete that index from list
    #recreate whole csv file
    pass
        
#TKINTER SET UP
from tkinter import *
from tkinter.font import Font

#tkinter functions

#set up mainframe
root = Tk()
mainframe = Frame(root)
root.title("Voca\'py (name work in progress)")

#set up widgets
vocab_list = ['example', 'example2']
vocab_list_var = StringVar()
vocab_list_var.set(vocab_list)

vocab_display_lb = Listbox(mainframe, listvariable=vocab_list_var, selectmode=SINGLE, height=10)

edit_vocab_frame = LabelFrame(mainframe, text="Edit Vocab List")

flashcard_frame = Label

#gridding
mainframe.grid(padx=50, pady=20)

vocab_display_lb.grid(row=1, column=1)
