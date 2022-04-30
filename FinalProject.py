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


if __name__ == "__main__":
    pass
