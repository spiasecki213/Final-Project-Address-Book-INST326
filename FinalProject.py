from tkinter import *

""" Create new address book window """
root = Tk()
root.title("Address Book")

contact_list = []

# initialize contact variables
first_name = StringVar()
last_name = StringVar()
street1 = StringVar()
street2 = StringVar()
city = StringVar()
state = StringVar()
zipcode = StringVar()
homephone = StringVar()
cellphone = StringVar()
email = StringVar()
alt_email = StringVar()
birthday = StringVar()
notes = StringVar()

# scrollbar and list of contacts displayed
scrollbar = Scrollbar(root)
box = Listbox(root, yscrollcommand=scrollbar.set, height=18)
box.grid(row=1, column=0, rowspan=13, padx=18)
scrollbar.config(command=box.yview)

""" Functions """



""" Labels, Entries, and Buttons """


if __name__ == "__main__":
    pass