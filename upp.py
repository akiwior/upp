import pyperclip
from tkinter import *
from win32clipboard import *

# def upp():
#     tekst = input(': ')
#     tekst = tekst.upper()
#     print(tekst)
#     pyperclip.copy(tekst)
#     return tekst
# upp()

def take_sch():
    OpenClipboard()
    schowek = str(GetClipboardData())
    CloseClipboard()
    return schowek


def upp1():
    tekst = take_sch()
    
    # tekst = entry.get()
    tekst = tekst.upper()
    pyperclip.copy(tekst)
    return tekst


root = Tk()
label = Label(root, text="wklej i kliknij")
label.grid(padx=0, pady=0)
button = Button(root, padx=10, pady=10, bg='red', text="POWIĘKSZ", command=upp1)
button.grid(padx=1, pady=2)
# entry = Entry(root)
# entry.grid(padx=0, pady=1)




root.mainloop()

