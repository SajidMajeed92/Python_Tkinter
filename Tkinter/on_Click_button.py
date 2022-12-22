from tkinter import *

root = Tk()
root.title("Display GUI")
root.geometry("400x400")


def clickme():
    hello = "Hello " + nameLabel.get()
    Label(root, text=hello).pack(pady=10)
    nameLabel.delete(0, 'end')


nameLabel = Entry(root, width=10, font=('Helvetica', 30))
nameLabel.pack(padx=10, pady=10)

Button(root, text="Enter Your Name", command=clickme).pack(pady=10)

root.mainloop()
