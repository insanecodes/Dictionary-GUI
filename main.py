from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PyDictionary import PyDictionary
from englisttohindi.englisttohindi import EngtoHindi


def get_meaning():
    dictionary = PyDictionary()
    get_word = txt_input.get()
    format = language_format.get()
    if get_word == "":
        messagebox.showerror('Dictionary', 'Please enter the word')
    elif format == 'English-to-English':
        outputbox.delete("1.0", "end")
        d = dictionary.meaning(get_word)
        outputbox.insert('end', d['Noun'])
    elif format == 'English-to-Hindi':
        d = dictionary.meaning(get_word)
        res = EngtoHindi(d['Noun']).convert
        outputbox.delete("1.0", "end")
        outputbox.insert('end', res)


# Driver Code
if __name__ == "__main__":
    # Create root window
    root = Tk()
    # Change the title
    root.title('Dictionary')
    # Change the window size
    root.geometry('300x400')
    # no resize for both directions
    root.resizable(False, False)
    # Change icon
    root.iconbitmap('icon.ico')

    # set gui widgets
    lbl_format = Label(root, text="Select Format :",
                       font=("Times New Roman", 12))
    lbl_word = Label(root, text="Enter Word :",
                     font=("Times New Roman", 12))
    txt_input = Entry(root, width=20, bd="2", font="18", relief=RIDGE)
    btn_get_meaning = Button(root, text='Search', width=6,
                             command=get_meaning, font=("Times New Roman", 14), relief=RIDGE)
    lbl_means = Label(root, text="Meaning :",
                      font=("verdana", 14, 'bold'))
    outputbox = Text(root, width=29, height=11,
                     relief=RIDGE, bd="2", pady=5, padx=3, spacing2=3, font=("Times New Roman", 13))

    # Place Geometry
    lbl_format.place(x=10, y=13)
    lbl_word.place(x=10, y=60)
    txt_input.place(x=100, y=60)
    btn_get_meaning.place(x=213, y=100)
    lbl_means.place(x=10, y=130)
    outputbox.place(x=12, y=165)

    # Combobox creation
    n = StringVar()
    language_format = ttk.Combobox(root, width=25, textvariable=n,)

    # Adding combobox drop down list
    language_format['values'] = ('English-to-English',
                                 'English-to-Hindi')

    language_format.place(x=115, y=15)
    language_format.current(0)

    # start mainloop
    root.mainloop()
