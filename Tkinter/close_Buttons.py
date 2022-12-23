from tkinter import *

# tkinter window
root = Tk()

# This button can close the window
button_1 = Button(root, text=" Close the Window", command=root.destroy)

button_1.pack(pady=50)

# This button closes the first button
button_2 = Button(root, text=" Close the first button", command=button_1.destroy)
button_2.pack(pady=50)

# This button closes the second button
button_3 = Button(root, text=" Close the second button", command=button_2.destroy)
button_3.pack(pady=50)

mainloop()
