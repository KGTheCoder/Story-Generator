from tkinter import *

window = Tk()
window.geometry("600x600")
window.title("Create your story")

def printProtag():
    protag = protag_entry.get()
    verb = verb_entry.get()
    noun1 = noun1_entry.get()
    noun2 = noun2_entry.get()
    Label(window, text=f'{protag} {verb} a {noun1} and a {noun2}.',
    pady=20).pack()

protag_label = Label(text="Enter the protagonist's name")
protag_entry = Entry()
verb_label = Label(text="Enter a verb")
verb_entry = Entry()
noun1_label = Label(text="Enter a noun")
noun1_entry = Entry()
noun2_label = Label(text="Enter another noun")
noun2_entry = Entry()

protag_label.pack()
protag_entry.pack()
verb_label.pack()
verb_entry.pack()
noun1_label.pack()
noun1_entry.pack()
noun2_label.pack()
noun2_entry.pack()

Button(
    window,
    text="Create Your Story!",
    command=printProtag
    ).pack()

window.mainloop()

