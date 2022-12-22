from tkinter import *

root = Tk()

root.geometry("655x434")
root.maxsize(1200, 989)
root.minsize(200, 100)

f1 = Frame(root, bg="gray", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, bg="grey", borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill=X)

label_1 = Label(f1, text="Project", fg="green")
label_1.pack(pady=14)

label_2 = Label(f2, text="Welcome to PyCharm IDE", font="Helvetica 16 bold", fg="green", pady=22)
label_2.pack()

root.mainloop()
