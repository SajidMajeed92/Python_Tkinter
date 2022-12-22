import tkinter as tk

window = tk.Tk()
window.title('Button Widget')

# opening widget
button = tk.Button(
    text="Click Me!",
    foreground="white",  # Set the text color to white
    background="gray",  # Set the background color to black
    width=25,
    height=5
)
button.pack()
# closing widget
window.mainloop()
