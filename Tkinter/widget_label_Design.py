import tkinter as tk

window = tk.Tk()
window.title('Label Widget')


label = tk.Label(
    text="We are learning PYTHON-101",
    foreground="white",  # Set the text color to white
    background="gray",  # Set the background color to black
    width=50,
    height=50
)
label.pack()
# closing widget
window.mainloop()
