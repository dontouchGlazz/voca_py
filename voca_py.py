#vocab flashcard practice
#table of contents
#1. csv set up
#2. tkinter set up

import random

#CSV SET UP
import csv
def read_csv_file():
    global unknown_list, known_list
    unknown_list = []
    known_list = []
    
    with open('vocab_listing.csv') as vocab_csv:
        #read original file
        line_reader = csv.reader(vocab_csv, delimiter=',')
        line_counter=0

        for row in line_reader:
            if len(row) > 1:
                if row[0] != "" and row[1] != "":
                    #insert reading code here
                    unknown_list.append(row[0])
                    known_list.append(row[1])
            
                line_counter+=1

def place_writer_at_end():
    global unknown_list, known_list
    
    with open('vocab_listing.csv') as vocab_csv:
        #read file
        read_csv_file()

    #rewrite whole file
    with open('vocab_listing.csv', 'w') as vocab_csv:
        line_writer = csv.writer(vocab_csv, delimiter=',')

        for i in range(0,len(unknown_list)):
            line_writer.writerow([unknown_list[i], known_list[i]])

def generate_test_values():
    place_writer_at_end()
    
    with open('vocab_listing.csv', 'w') as vocab_csv:
        line_writer = csv.writer(vocab_csv, delimiter=',')
        
        #add one new line
        line_writer.writerow(['skibidi', 'toilet'])
        line_writer.writerow(['ohio', 'six seven'])
        line_writer.writerow(['diddy', 'blud'])

def add_vocab():
    global unknown_list, known_list
    #GET FROM TKINTER
    entered_word = add_word_var.get()
    #slices must be index integers
    comma_index = entered_word.index(',')
    unknown_word = entered_word[:comma_index]
    known_word = entered_word[comma_index+1:]

    unknown_list.append(unknown_word)
    known_list.append(known_word)
    
    place_writer_at_end()
    
    with open('vocab_listing.csv', 'w') as vocab_csv:
        line_writer = csv.writer(vocab_csv, delimiter=',')
        #add one new line
        line_writer.writerow([unknown_word, known_word])

    unknown_list_var.set(unknown_list)
    known_list_var.set(known_list)

def delete_vocab():
    #find index of listbox
    #read csv file
    #copy to list
    #delete that index from list
    #recreate whole csv file
    pass

def generate_flashcards():
    global unknown_list, known_list

    displayable_unknown_list = []
    displayable_known_list = []

    #read csv file and update unkown_list and known_list
    read_csv_file()
    
    #scramble both lists
    while len(displayable_unknown_list) != len(unknown_list):
        random_index = random.randint(0, len(unknown_list))
        
        if unknown_list[random_index] not in displayable_unknown_list:
            displayable_unknown_list.append(unknown_list[random_index])
            displayable_known_list.append(known_list[random_index])
    
    #display to tkinter

def next_card():
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
####vocab frame (listbox, add, delete, entry)
edit_vocab_frame = LabelFrame(mainframe, text="Edit Vocab List")

#FIX THIS LISTBOX
read_csv_file()

unknown_list_var = StringVar()
unknown_list_var.set(unknown_list)

known_list_var = StringVar()
known_list_var.set(known_list)

unknown_lb_label = Label(edit_vocab_frame, text="Unknown Words")
unknown_vocab_display_lb = Listbox(edit_vocab_frame, listvariable=unknown_list_var, \
                                   selectmode=SINGLE, height=10)
known_lb_label = Label(edit_vocab_frame, text="Definitions")
known_vocab_display_lb = Listbox(edit_vocab_frame, listvariable=known_list_var, \
                                   selectmode=SINGLE, height=10)

add_button = Button(edit_vocab_frame, text="Add word", command = add_vocab)
delete_button = Button(edit_vocab_frame, text="Delete word", command=delete_vocab)

add_word_var = StringVar()
add_word_var.set('Enter word here...')
word_entry = Entry(edit_vocab_frame, textvariable=add_word_var)

####flashcard frame (flashcards, refresh, next)
flashcard_frame = LabelFrame(mainframe, text='Flashcards')

unknown_word_frame = LabelFrame(flashcard_frame, text="Unknown word")
known_word_frame = LabelFrame(flashcard_frame, text="Definition")

unknown_word_var = StringVar()
unknown_word_var.set('skibidi')
known_word_var = StringVar()
known_word_var.set('toilet')

unknown_word_label = Label(unknown_word_frame, textvariable=unknown_word_var)
known_word_label = Label(known_word_frame, textvariable=known_word_var)

refresh_button = Button(flashcard_frame, text="Refresh flashcards", command=generate_flashcards)
next_button = Button(flashcard_frame, text="Next card", command=next_card)

#test
generate_test = Button(mainframe, text="generate testing values", command = generate_test_values)

#gridding
mainframe.grid(padx=50, pady=20)

####edit vocab frame
edit_vocab_frame.grid(row=1, column=1)

unknown_lb_label.grid(row=1, column=1)
unknown_vocab_display_lb.grid(row=2, column=1)

known_lb_label.grid(row=1, column=2)
known_vocab_display_lb.grid(row=2, column=2)

add_button.grid(row=3, column=1)
delete_button.grid(row=3, column=2)
word_entry.grid(row=4, column=1, columnspan=2)

###flashcard frame
flashcard_frame.grid(row=1, column=2)

unknown_word_frame.grid(row=1, column=1)
known_word_frame.grid(row=1, column=2)

unknown_word_label.grid(row=1, column=1, sticky = EW)
known_word_label.grid(row=1, column=1, sticky = EW)

refresh_button.grid(row=2, column=1)
next_button.grid(row=2, column=2)

#test
generate_test.grid(row=3, column=1)










