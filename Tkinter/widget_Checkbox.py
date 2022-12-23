from tkinter import *

root = Tk()
root.geometry("655x344")


def get_value():
    print("It works!\n")
    print("Name:-", nameValue.get(), "\nPhone:- ", phoneValue.get(), "\nGender:-", genderValue.get(),
          "\nEmergency Number:-", emergencyValue.get(), "\n Payment Mode:-", payment_modeValue.get(),
          "\n food Service :- ", food_serviceValue.get())


# Heading.
label1 = Label(root, text="Creating Checkbox GUI", font="comicsansms 13 bold", pady=10, fg="black").grid(column=2)

# Text for the form.
name = Label(root, text="Name ")
name.grid(row=1, column=1)

phone = Label(root, text="Phone ")
phone.grid(row=2, column=1)

gender = Label(root, text="Gender ")
gender.grid(row=3, column=1)

emergency = Label(root, text="Emergency Number ")
emergency.grid(row=4, column=1)

payment_mode = Label(root, text="Payment Mode ")
payment_mode.grid(row=5, column=1)

# tkinter value to storing enties.
nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
emergencyValue = StringVar()
payment_modeValue = StringVar()
food_serviceValue = IntVar()  # IntVar because it would be 0 or 1.

# Entries for our form

nameEntry = Entry(root, textvariable=nameValue)
nameEntry.grid(row=1, column=2)

phoneEntry = Entry(root, textvariable=phoneValue)
phoneEntry.grid(row=2, column=2)

genderEntry = Entry(root, textvariable=genderValue)
genderEntry.grid(row=3, column=2)

emergencyEntry = Entry(root, textvariable=emergencyValue)
emergencyEntry.grid(row=4, column=2)

payment_modeEntry = Entry(root, textvariable=payment_modeValue)
payment_modeEntry.grid(row=5, column=2)

# making checkbox and packing
food_service = Checkbutton(root, text="Check here", variable=food_serviceValue)
food_service.grid(row=6, column=2)

button1 = Button(root, text="Submit", command=get_value)
button1.grid(row=7, column=2, pady=10)

root.mainloop()
