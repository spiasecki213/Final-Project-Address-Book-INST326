from tkinter import *
import tkinter
from ttkwidgets.autocomplete import AutocompleteCombobox
import tkinter.messagebox as mb
import sqlite3 as sql

# Connect and initialize the database that will store all of the contacts
connector = sql.connect('contacts.db')
cursor = connector.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS ADDRESS_BOOK (S_NO INTEGER PRIMARY KEY 
                AUTOINCREMENT NOT NULL, FIRSTNAME TEXT, LASTNAME TEXT, ADDRESS TEXT, 
                PHONENUMBER TEXT, EMAIL TEXT, ALTEMAIL TEXT, PRONOUNS TEXT, NOTES TEXT, 
                GROUPS TEXT)"""
)

class MainWindow(object):

    def add_contact(self):
        pass

    def list_contacts(self):
        pass

    def delete_contact(self):
        pass

    def delete_all_contacts(self):
        pass

    def view_contact(self):
        pass

    def clear_fields(self):
        pass

    def search(self):
        pass

    def __init__(self, root):
        # Initialize the GUI window
        self.root = root
        root.title("Address Book")
        root.geometry('700x550')
        root.resizable(0,0)

        # Create the StringVar contact info variables
        self.fname_strvar = StringVar()
        self.lname_strvar = StringVar()
        self.phone_strvar = StringVar()
        self.email_strvar = StringVar()
        self.altemail_strvar = StringVar()
        self.pronouns_strvar = StringVar()
        self.group_strvar = StringVar()
        self.search_strvar = StringVar() #stringvar for search bar

        # Title label
        Label(self.root, text="UMD Address Book", font=('Times New Roman', 24, "bold"), 
                    bg='red4', fg='White').pack(side=TOP, fill=X)

        # Color and font variables
        lf_bg = 'light goldenrod'  # Lightest Shade
        cf_bg = 'gold2'
        rf_bg = 'gold3'  # Darkest Shade
        frame_font = ("Garamond", 13, "bold")
        entry_font = ("Arial", 10)
        button_font = ("Garamond", 11, "bold")
        group_values = ["Student", "Professor", "TA", "AMP", "Administrator", "Other"]

        # Left Frame
        left_frame = Frame(root, bg=lf_bg)
        left_frame.place(relx=0, relheight=1, y=37, relwidth=0.35)
        Label(left_frame, text="Contact Info", font=('Times New Roman', 14, "italic"), 
                    bg='Maroon', fg='White').pack(side=TOP, fill=X) # left frame label
        # Center Frame
        center_frame = Frame(root, bg=cf_bg)
        center_frame.place(relx=0.35, relheight=1, y=37, relwidth=0.3)
        Label(center_frame, text="Search/Edit", font=('Times New Roman', 14, "italic"), 
                    bg='Maroon', fg='White').pack(side=TOP, fill=X) # center frame label
        # Frame on the right
        right_frame = Frame(root, bg=rf_bg)
        right_frame.place(relx=0.65, relwidth=0.35, relheight=1, y=37)

        """ LEFT FRAME COMPONENTS """
        # first name
        Label(left_frame, text="First Name:", bg=lf_bg, font=frame_font).place(relx=0.03, rely=0.1)
        fname_Entry = Entry(left_frame, width=17, font=entry_font, textvariable=self.fname_strvar)
        fname_Entry.place(relx=0.44, rely=0.1)
        # last name
        Label(left_frame, text="Last Name:", bg=lf_bg, font=frame_font).place(relx=0.03, rely=0.15)
        lname_Entry = Entry(left_frame, width=17, font=entry_font, textvariable=self.lname_strvar)
        lname_Entry.place(relx=0.44, rely=0.15)
        # address
        Label(left_frame, text="Address:", bg=lf_bg, font=frame_font).place(relx=0.03, rely=0.2)
        self.address_entry = Text(left_frame, width=17, font=entry_font, height=4)
        self.address_entry.place(relx=0.44, rely=0.2)
        # phone number
        Label(left_frame, text="Phone #:", bg=lf_bg, font=frame_font).place(relx=0.03, rely=0.35)
        phone_Entry = Entry(left_frame, width=17, font=entry_font, textvariable=self.phone_strvar)
        phone_Entry.place(relx=0.44, rely=0.35)
        # email address
        Label(left_frame, text="Email:", bg=lf_bg, font=frame_font).place(relx=0.03, rely=0.4)
        email_Entry = Entry(left_frame, width=17, font=entry_font, textvariable=self.email_strvar)
        email_Entry.place(relx=.44, rely=0.4)
        # alternate email address
        Label(left_frame, text="Alt. Email:", bg=lf_bg, font=frame_font).place(relx=0.03, rely=0.45)
        altemail_Entry = Entry(left_frame, width=17, font=entry_font, textvariable=self.altemail_strvar)
        altemail_Entry.place(relx=.44, rely=0.45)
        # pronouns
        Label(left_frame, text="Pronouns:", bg=lf_bg, font=frame_font).place(relx=0.03, rely=0.5)
        pronouns_Entry = Entry(left_frame, width=17, font=entry_font, textvariable=self.pronouns_strvar)
        pronouns_Entry.place(relx=.44, rely=0.5)
        # notes
        Label(left_frame, text="Notes:", bg=lf_bg, font=frame_font).place(relx=0.03, rely=0.55)
        self.notes_entry = Text(left_frame, width=17, font=entry_font, height=5)
        self.notes_entry.place(relx=.44, rely=0.55)
        # group
        Label(left_frame, text="Group:", bg=lf_bg, font=frame_font).place(relx=0.03, rely=0.72)
        group_Entry = AutocompleteCombobox(left_frame, width=15, font=entry_font, completevalues=group_values)
        group_Entry.place(relx=.44, rely=0.72)

        # clear fields button
        Button(left_frame, text="Clear Fields", font=button_font, width=12, command=self.clear_fields).place(relx=0.3, rely=0.82)

        """ CENTER FRAME COMPONENTS """
        # function to delete temporary text when the entry box is clicked
        def temp_text(e):
            """ Deletes the temporary text in the
            search bar

            Args:
                e (arg): positional argument
            """ 
            self.search_entry.delete(0,"end")

        # search bar
        self.search_entry = Entry(center_frame, width=18, 
            font=("Arial", 12), textvariable=self.search_strvar)
        self.search_entry.insert(0, "Search Contacts...")
        self.search_entry.bind("<FocusIn>", temp_text)
        self.search_entry.place(relx=0.1, rely=0.2)
        # search button
        Button(center_frame, text="Search", font=button_font, width=12, command=self.search).place(relx=0.23, rely=0.25)

        # add contact button
        Button(center_frame, text="Add Contact", font=button_font, width=12, command=self.add_contact).place(relx=0.24, rely=0.4)
        # view contact button
        Button(center_frame, text="View Contact", font=button_font, width=12, command=self.view_contact).place(relx=0.24, rely=0.5)
        # delete contact button
        Button(center_frame, text="Delete Contact", font=button_font, width=12, command=self.delete_contact).place(relx=0.24, rely=0.6)
        # delete all contacts button
        Button(center_frame, text="Delete All Contacts", font=button_font, width=15, command=self.delete_all_contacts).place(relx=0.168, rely=0.7)


        """ RIGHT FRAME COMPONENTS """
        # frame label
        Label(right_frame, text="Saved Contacts", bg=rf_bg, font=('Garamond', 16)).place(relx=0.2, rely=0.07)
        # contact listbox
        self.listbox = Listbox(right_frame, selectbackground='Gray82', 
                bg='white smoke', font=entry_font, height=20, width=27)
        self.scroller = Scrollbar(self.listbox, orient=VERTICAL, command=self.listbox.yview)
        self.scroller.place(relx=0.93, rely=0, relheight=1)
        self.listbox.config(yscrollcommand=self.scroller.set)
        self.listbox.place(relx=0.1, rely=0.15)

        self.list_contacts()

if __name__ == "__main__":
    root = tkinter.Tk()
    r = MainWindow(root)
    root.update()
    root.mainloop()