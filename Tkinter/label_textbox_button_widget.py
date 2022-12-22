# Program to make a simple
# login screen


import tkinter as tk

root = tk.Tk()
root.title('Login Screen')

# setting the windows size
root.geometry("600x400")

# declaring string variable
# for storing name and password
name_var = tk.StringVar()
password_var = tk.StringVar()


# defining a function that will
# get the name and password and
# print them on the screen
def submit():
    name = name_var.get()
    password = password_var.get()

    print("The name is : " + name)
    print("The password is : " + password)

    name_var.set("Enter Your Name")
    password_var.set("Enter Your Password")


# creating a label for
# name using widget Label
name_label = tk.Label(root, text='Username', font=('calibre', 10, 'bold'))

# creating an entry for input
# name using widget Entry
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))

# creating a label for password
password_label = tk.Label(root, text='Password', font=('calibre', 10, 'bold'))

# creating a entry for password
password_entry = tk.Entry(root, textvariable=password_var, font=('calibre', 10, 'normal'), show='*')

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Submit', command=submit)

# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

# performing an infinite loop
# for the window to display
root.mainloop()
