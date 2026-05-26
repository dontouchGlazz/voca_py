#vocab flashcard practice
#table of contents
#1. csv set up
#2. tkinter set up

import random

#csv set up
#no need to import csv

def generate_vocab_lists(filename):
    unknown_list = []
    known_list = []

    file_in = open(filename, encoding="utf-8")
    #utf-8 can handle chinese character
    file_in.readline()

    for line in file_in:
        line = line.strip().split(",")
        #each line is thing1, thing2, thing3
        #line is a list

        unknown_list.append(line[0])
        known_list.append(line[1])

    return unknown_list, known_list
    
#tkinter
from tkinter import *
from tkinter.font import Font

#tkinter functions

#set up mainframe
root = Tk()
mainframe = Frame(root)
root.title("Voca\'py (name work in progress)")

#set up widgets

#--->display all vocab using listbox

#gridding



#flashcard mode
#--->read from csv
#--->randomly scramble list
#--->then go through this list, 0, 1, 2...

#recording mode
#--->enter new word and add to csv

def main():
    generate_vocab_lists(vocab_listing)

main()
