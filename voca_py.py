#vocab flashcard practice
#table of contents
#1. csv set up
#2. tkinter set up

import random

#CSV SET UP
import csv

def update_listbox():
    global unknown_list, known_list
    read_csv_file()
    
    unknown_list_var.set(unknown_list)
    known_list_var.set(known_list)
    #print('listbox was updated')

def read_csv_file():
    #clear "memory"
    global unknown_list, known_list
    unknown_list=[]
    known_list=[]
    
    with open('vocab_listing.csv', encoding="utf-8") as vocab_csv:
        #read original file
        line_reader = csv.reader(vocab_csv, delimiter=',')

        for row in line_reader:
            if len(row) > 1:
                if row[0] != "" and row[1] != "":
                    #insert reading code here
                    unknown_list.append(row[0])
                    known_list.append(row[1])

    #overwriting file to clean it does not work
                
    #print('\ncsv file was read')

def place_writer_at_end():
    #print("placing writer at end....")
    global unknown_list, known_list
    read_csv_file()

    #rewrite whole file
    with open('vocab_listing.csv', 'w', encoding="utf-8") as vocab_csv:
        line_writer = csv.writer(vocab_csv, delimiter=',')
        line_countby = 0

        for i in range(0,len(unknown_list)):
            line_writer.writerow([unknown_list[i], known_list[i]])
            print(f'{unknown_list[i]} and {known_list[i]} was in row {line_countby}')
            line_countby+=1
        #print('writer placed at end')

    update_listbox()

def generate_test_values():
    place_writer_at_end()
    
    with open('vocab_listing.csv', 'w', encoding="utf-8") as vocab_csv:
        line_writer = csv.writer(vocab_csv, delimiter=',')
        
        line_writer.writerow(['skibidi', 'toilet'])
        line_writer.writerow(['ohio', 'six seven'])
        line_writer.writerow(['diddy', 'blud'])
    #print('test values generated')
    
    #testing
    with open('vocab_listing.csv', encoding="utf-8") as vocab_csv:
        line_countby = 0
        line_reader = csv.reader(vocab_csv, delimiter=',')
        for row in line_reader:
            print(f'{row} was written in row {line_countby}')
            line_countby += 1
            
    update_listbox()

def add_vocab():
    global unknown_list, known_list
    read_csv_file()

    #setting up word to add
    entered_word = add_word_var.get()
    if entered_word == "Enter word here..." or entered_word == "":
        unknown_word = ""
        known_word = ""
    else:
        #not very flexible
        
        comma_index = entered_word.index(',')
        
        unknown_word = entered_word[:comma_index]

        if entered_word[comma_index+1] == " ":
            known_word = entered_word[comma_index+2:]
        else:
            known_word = entered_word[comma_index+1:]

    #rewrite whole file
    with open('vocab_listing.csv', 'w', encoding="utf-8") as vocab_csv:
        line_writer = csv.writer(vocab_csv, delimiter=',')
        line_countby = 0

        for i in range(0,len(unknown_list)):
            line_writer.writerow([unknown_list[i], known_list[i]])
            #print(f'{unknown_list[i]} and {known_list[i]} was in row {line_countby}')
            line_countby+=1
            
        #print('writer placed at end')
        line_writer.writerow([unknown_word, known_word])
        #print(f'added {unknown_word} and {known_word}')

    update_listbox()
    add_word_var.set("")

def delete_vocab():
    global unknown_list, known_list
    
    #find index of listbox
    if unknown_vocab_lb.curselection():
        index = unknown_vocab_lb.curselection()[0]
    elif known_vocab_lb.curselection():
        index = known_vocab_lb.curselection()[0]
    else:
        pass
    
    #read csv file and store values in mutable python list
    read_csv_file()
    
    #delete that index from python list
    unknown_list.pop(index)
    known_list.pop(index)
    
    #rewrite whole csv file
    with open('vocab_listing.csv', 'w', encoding="utf-8") as vocab_csv:
        line_writer = csv.writer(vocab_csv, delimiter=',')

        for i in range(0,len(unknown_list)):
            line_writer.writerow([unknown_list[i], known_list[i]])

    update_listbox()

def generate_flashcards():
    global unknown_list, known_list, flashcard_index, displayable_unknown_list, displayable_known_list

    displayable_unknown_list = []
    displayable_known_list = []

    #read csv file and update unkown_list and known_list
    read_csv_file()
    
    #scramble both lists
    while len(displayable_unknown_list) != len(unknown_list):
        random_index = random.randint(0, len(unknown_list)-1)
        
        if unknown_list[random_index] not in displayable_unknown_list:
            displayable_unknown_list.append(unknown_list[random_index])
            displayable_known_list.append(known_list[random_index])
    
    #display to tkinter
    flashcard_index=0
    unknown_word_var.set(displayable_unknown_list[0])
    known_word_var.set(displayable_known_list[0])

    next_button.config(state=NORMAL)

def next_card():
    global flashcard_index, displayable_unknown_list, displayable_known_list

    flashcard_index +=1

    if flashcard_index == len(displayable_unknown_list):
        next_button.config(state=DISABLED)
    else:
        unknown_word_var.set(displayable_unknown_list[flashcard_index])
        known_word_var.set(displayable_known_list[flashcard_index])
    
        
#TKINTER SET UP
from tkinter import *
from tkinter.font import Font

#tkinter functions

#set up mainframe
root = Tk()
mainframe = Frame(root)
root.title("Voca\'py (name work in progress)")

#set up fonts
flashcard = Font(family="Arial", size=14)

#set up widgets
####vocab frame (listbox, add, delete, entry)
edit_vocab_frame = LabelFrame(mainframe, text="Edit Vocab List")

#FIX THIS LISTBOX

unknown_list_var = StringVar()
known_list_var = StringVar()

unknown_lb_label = Label(edit_vocab_frame, text="Unknown Words")
unknown_vocab_lb = Listbox(edit_vocab_frame, listvariable=unknown_list_var, \
                                   selectmode=SINGLE, height=10)
known_lb_label = Label(edit_vocab_frame, text="Definitions")
known_vocab_lb = Listbox(edit_vocab_frame, listvariable=known_list_var, \
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

unknown_word_label = Label(unknown_word_frame, textvariable=unknown_word_var, font=flashcard, wraplength=200)
known_word_label = Label(known_word_frame, textvariable=known_word_var, font=flashcard, wraplength=200)

refresh_button = Button(flashcard_frame, text="Refresh flashcards", command=generate_flashcards)
next_button = Button(flashcard_frame, text="Next card", command=next_card, state=DISABLED)

#test
generate_test = Button(mainframe, text="generate testing values", command = generate_test_values)

#gridding
mainframe.grid(padx=50, pady=20)

####edit vocab frame
edit_vocab_frame.grid(row=1, column=1, padx=20)

unknown_lb_label.grid(row=1, column=1, padx=10, pady=10)
unknown_vocab_lb.grid(row=2, column=1, padx=10)

known_lb_label.grid(row=1, column=2, padx=10, pady=10)
known_vocab_lb.grid(row=2, column=2, padx=10)

add_button.grid(row=3, column=1)
delete_button.grid(row=3, column=2)
word_entry.grid(row=4, column=1, columnspan=2, pady=10)

###flashcard frame
flashcard_frame.grid(row=1, column=2, padx=20)

unknown_word_frame.grid(row=1, column=1, padx=10)
unknown_word_frame.config(bg="#ffffff")

known_word_frame.grid(row=1, column=2, padx=10)
known_word_frame.config(bg="#ffffff")

unknown_word_label.grid(row=1, column=1, sticky = EW, padx=76, pady=50)
unknown_word_label.config(bg="#ffffff")
known_word_label.grid(row=1, column=1, sticky = EW, padx=76, pady=50)
known_word_label.config(bg="#ffffff")

refresh_button.grid(row=2, column=1, pady=10)
next_button.grid(row=2, column=2, pady=10)

#test
#generate_test.grid(row=3, column=1)

#main()
read_csv_file()
update_listbox()










