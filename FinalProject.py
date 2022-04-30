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
def selected_contact():
    return int(box.curselection()[0])
 
 
def add_contact():
    contact_list.append([first_name.get(), last_name.get(), street1.get(),
                        street2.get(), city.get(), state.get(), zipcode.get(),
                        homephone.get(), cellphone.get(), email.get(),
                        alt_email.get(), birthday.get(), notes.get()])  
    display_contacts()
 
# edit contact
def edit_contact():
    contact_list[selected_contact()] = [first_name.get(), last_name.get(),
                        street1.get(), street2.get(), city.get(),
                        state.get(), zipcode.get(),homephone.get(),
                        cellphone.get(), email.get(),alt_email.get(),
                        birthday.get(), notes.get()]
    display_contacts()
 
def delete_contact():
    del contact_list[selected_contact()]
    display_contacts()
 
 
def view_contact():
    fn,ln,s1,s2,cit,sta,zi,hp,cp,em,ae,bd,n= contact_list[selected_contact()]
    first_name.set(fn)
    last_name.set(ln)
    street1.set(s1)
    street2.set(s2)
    city.set(cit)
    state.set(sta)
    zipcode.set(zi)
    homephone.set(hp)
    cellphone.set(cp)
    email.set(em)
    alt_email.set(ae)
    birthday.set(bd)
    notes.set(n)
 
def exit_window():
    root.destroy()
 
def reset_fields():
    for x in contact_list:
        for y in contact_list[x]:
            y.set('')
 
def display_contacts():
    contact_list.sort()
    box.delete(0, END)
    for fn,ln,s1,s2,cit,sta,zi,hp,cp,em,ae,bd,notes in contact_list:
        box.insert(END, fn)
 
display_contacts()

""" Labels, Entries, and Buttons """
# First Name
fnameLabel = Label(root, text="First Name:").grid(row=1,column=3)
fnameEntry = Entry(root, textvariable=first_name).grid(row=1,column=4)
# Last Name
lnameLabel = Label(root, text="Last Name:").grid(row=2,column=3)
lnameEntry = Entry(root, textvariable=last_name).grid(row=2,column=4)
# Address 1
street1Label = Label(root, text="Address 1:").grid(row=3,column=3)
street1Entry = Entry(root,textvariable=street1).grid(row=3,column=4)
# Address 2
street2Label = Label(root, text="Address 2:").grid(row=4,column=3)
street2Entry = Entry(root,textvariable=street2).grid(row=4,column=4)
# City
cityLabel = Label(root, text="City:").grid(row=5,column=3)
cityEntry = Entry(root,textvariable=city).grid(row=5,column=4)
# State
stateLabel = Label(root, text="State:").grid(row=6,column=3)
stateEntry = Entry(root,textvariable=state).grid(row=6,column=4)
# Zipcode
zipcodeLabel = Label(root, text="Zipcode:").grid(row=7,column=3)
zipcodeEntry = Entry(root,textvariable=zipcode).grid(row=7,column=4)
# Home Phone
homeLabel = Label(root, text="Home Phone:").grid(row=8,column=3)
homeEntry = Entry(root,textvariable=homephone).grid(row=8,column=4)
# Cell Phone
cellLabel = Label(root, text="Cell Phone:").grid(row=9,column=3)
cellEntry = Entry(root,textvariable=cellphone).grid(row=9,column=4)
# Email Address
emailLabel = Label(root, text="Email:").grid(row=10,column=3)
emailEntry = Entry(root,textvariable=email).grid(row=10,column=4)
# Alternate Email Address
altemailLabel = Label(root, text="Alternate Email:").grid(row=11,column=3)
altemailEntry = Entry(root,textvariable=alt_email).grid(row=11,column=4)
# Birthday
bdayLabel = Label(root, text="Birthday:").grid(row=12,column=3)
bdayEntry = Entry(root,textvariable=birthday).grid(row=12,column=4)
# Notes
notesLabel = Label(root, text="Notes:").grid(row=13,column=3)
notesEntry = Entry(root,textvariable=notes).grid(row=13,column=4,rowspan=2, pady=10)
 
 
addButton = Button(root, text="Add", command=add_contact()).grid(row=16,column=3, padx=10)
#editButton = Button(root, text="Edit",command=edit_contact()).grid(row=16,column=4, padx=10)
#viewButton = Button(root, text="View",command=view_contact()).grid(row=16,column=5,padx=10)
deleteButton = Button(root, text="Delete",command=delete_contact()).grid(row=17,column=3,padx=10)
 
def display_contacts():
    contact_list.sort()
    box.delete(0, END)
    for fn,ln,s1,s2,cit,sta,zi,hp,cp,em,ae,bd,notes in contact_list:
        box.insert(END, fn)
 
display_contacts()


if __name__ == "__main__":
    pass
