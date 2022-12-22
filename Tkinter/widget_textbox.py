# The interesting bit about Entry widgets isn’t how to style them, though. It’s how to use them to get input from a user. There are three main operations that you can perform with Entry widgets:
#
# Retrieving text with .get()
# Deleting text with .delete()
# Inserting text with .insert()
import tkinter as tk

window = tk.Tk()
window.title('Text Box Widget')

# Add button widget
label = tk.Label(text="Enter Here")
entry = tk.Entry()
label.pack()
entry.pack()
# closing widget
window.mainloop()

