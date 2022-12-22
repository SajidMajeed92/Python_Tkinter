from tkinter import *

root = Tk()

# geometry use to make window (width,height)
root.geometry("655x344")
root.maxsize(1200, 989)  # Max size of window (width,height)
root.minsize(200, 100)  # Min size of window (width , height)

root.title(" Geometry window")

r = Label(text="This is my first tkinter program", bg="Gray", fg="white", padx=113, pady=94, font="comicsansms 19 bold",
          borderwidth=30, relief=RIDGE)

# r.pack(fill= BOTH, expand=True) # fill = BOTH and expand = True use to fit in the screen.

r.pack(side=BOTTOM, anchor="se")  # anchor to move in (s = south ,e = east , n = north ,w = west)

root.mainloop()
