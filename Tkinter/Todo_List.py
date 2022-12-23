from tkinter import *
window = Tk()

label= Label(window,text = "TO-DO-LIST")
label.pack()

list = Listbox(window,bg = 'yellow')
list.insert(1,'Clean your stuff')
list.insert(2,'Create a Tkinter program')
list.insert(3,'Finish application')
list.insert(4,'Get a Refill')
list.pack()

window.config(bg='black')
window.geometry("300x300")
window.title('LIST')
window.mainloop()