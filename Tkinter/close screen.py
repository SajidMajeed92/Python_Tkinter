from tkinter import *


# create close method that includes the root.destroy command
def close():
    root.destroy()


# To create the tkinter window
root = Tk()
root.geometry('200x100')

# create the button and pass the close method as the command.
# the close method contains the root.destroy
# we can directly pass the destroy command instead of creating a close method
button = Button(root, text='Close the window', command=close)
button.pack(pady=20)

root.mainloop()
