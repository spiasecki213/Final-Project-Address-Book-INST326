from tkinter import *
import tkinter
from ttkwidgets.autocomplete import AutocompleteCombobox
import tkinter.messagebox as mb
import sqlite3 as sql
import address_book 
import unittest

class TestMainWindow(unittest.TestCase):
    #This tests the add_contact method
    def test_add_contact(self):
        pass

    def test_edit_contact(self):
        """""Tests that the function accurately updates a name"""""
        self.normal_fields()
        new_fname = self.fname_strvar.get("John") #updated first name of the person is John
        self.assertEqual(new_fname, "John") #checks that the new stored name is John
        self.assertNotEqual(new_fname, "Josh") #checks that the new stored name is not the original name
        assert new_fname is not None #checks that there is a value entered for the first name 
        new_lname = self.lname_strvar.get("Doe") #updated last name of the person is Doe
        self.assertEqual(new_lname, "Doe") #checks that the new stored name is Doe
        self.assertNotEqual(new_lname, "Done") #checks that the new stored name is not the original name
        assert new_lname is not None #checks that there is a value entered for the last name

    def test_list_contacts(self):
        pass

    def test_delete_contact(self):
        pass

    def test_delete_all_contacts(self):
        pass

    def test_view_contact(self):
        pass

    def test_clear_fields(self):
        """""Tests that the function actually deletes the information in the box while a person is editing a contact"""""
        self.normal_fields() 
        self.listbox.selection_clear(0, END)
        empty_fname = self.fname_strvar.set('') #clears first name box
        self.assertEqual(empty_fname, '') #checks that the first name is equal to blank space
        self.assertNotEqual(empty_fname, 'name') #checks that the first name is not equal to a name
        empty_lname = self.lname_strvar.set('') #clears last name box
        self.assertEqual(empty_lname, '') #checks that last name is equal to blank space
        self.assertNotEqual(empty_lname, 'name') #checks that last name is not equal to a name
        empty_phone = self.phone_strvar.set('') #clears phone number box
        self.assertEqual(empty_phone, '') #checks that phone number is equal to blank space
        self.assertNotEqual(empty_phone, '2405555555') #checks that phone number is not equal to a number
        empty_email = self.email_strvar.set('') #clears email box
        self.assertEqual(empty_email, '') #checks that email is equal to blank space
        self.assertNotEqual(empty_email, 'randomemail@umd.edu') #checks that email is not equal to an email
        empty_altmail = self.altemail_strvar.set('') #clears alternative email box
        self.assertEqual(empty_altmail, '') #checks that alternative email is equal to blank space
        self.assertNotEqual(empty_altmail, 'randomaltmail@umd.edu') #checks that alternative email is not equal to an email
        empty_pronouns = self.pronouns_strvar.set('') #clears pronoun box
        self.assertEqual(empty_pronouns, '') #checks that pornouns is equal to blank space
        self.assertNotEqual(empty_fname, 'she/her') #checks that pronouns is not equal to one or more pronouns
        empty_group = self.group_entry.set('') #clears contact group box
        self.assertEqual(empty_group, '') #checks that there is no selected contact group
        self.assertNotEqual(empty_fname, 'TA') #checks that contact group is not equal to any option in dropdown
        empty_address = self.address_entry.delete(1.0, END) #clears address box
        empty_notes = self.notes_entry.delete(1.0, END) #clears notes box
    
    def test_search(self):
        """""This tests if the person enters a name or nothing into the search box"""""
        search_ab1 = str(self.search_strvar.get("John Doe")) #sample search is a name in the address book
        self.assertEqual(search_ab1, "John") #search should return the first name that matches the search
        search_ab2 = str(self.search_strvar.get('')) #sample search is blank space indicating that user didn't enter a value
        self.assertEqual(search_ab2, '') #search should return error and prompt user to enter a value
        search_ab_3 = str(self.search_strvar.get('Search Contacts...')) #sample search is the initial text in search box, indicating no value was entered
        self.assertEqual(search_ab_3, 'Search Contacts...') #search should return error and prompt user to enter a value

    def test_read_only_fields(self):
        """""Tests that all of the address book fields can only be read, and can't be edited"""""
        read_fname = self.fname_entry.configure(state='readonly') #sets field to a read-only state
        self.assertEqual(read_fname, state = "readonly") #checks that the state is read-only/disabled and can't be edited
        self.assertNotEqual(read_fname, state = "normal") #checks that the state is not normal, which means the field can be edited by users
        read_lname = self.lname_entry.configure(state='readonly')
        self.assertEqual(read_lname, state = "readonly")
        self.assertNotEqual(read_lname, state = "normal")
        read_address = self.address_entry.configure(state='disabled')
        self.assertEqual(read_address, state = "disabled")
        self.assertNotEqual(read_address, state = "normal")
        read_phone = self.phone_entry.configure(state='readonly')
        self.assertEqual(read_phone, state = "readonly")
        self.assertNotEqual(read_phone, state = "normal")
        read_email = self.email_entry.configure(state='readonly')
        self.assertEqual(read_email, state = "readonly")
        self.assertNotEqual(read_email, state = "normal")
        read_altemail = self.altemail_entry.configure(state='readonly')
        self.assertEqual(read_altemail, state = "readonly")
        self.assertNotEqual(read_altemail, state = "normal")
        read_pronouns = self.pronouns_entry.configure(state='readonly')
        self.assertEqual(read_pronouns, state = "readonly")
        self.assertNotEqual(read_pronouns, state = "normal")
        read_notes = self.notes_entry.configure(state='disabled')
        self.assertEqual(read_notes, state = "disabled")
        self.assertNotEqual(read_notes, state = "normal")
        read_group = self.group_entry.configure(state='disabled')
        self.assertEqual(read_group, state = "disabled")
        self.assertNotEqual(read_group, state = "normal")

    def test_normal_fields(self):
         """""Tests that all of the address book fields are set to normal so they can be edited again"""""
        norm_fname = self.fname_entry.configure(state='normal') #sets field to normal
        self.assertEqual(norm_fname, state = "normal") #checks if field is set to normal so user can edit
        self.assertNotEqual(norm_fname, state = "readonly") #checks if field is not set to readonly (or disabled), which means user won't be able to edit
        norm_lname = self.lname_entry.configure(state='normal')
        self.assertEqual(norm_lname, state = "normal")
        self.assertNotEqual(norm_lname, state = "readonly")
        norm_address = self.address_entry.configure(state='normal')
        self.assertEqual(norm_address, state = "normal")
        self.assertNotEqual(norm_address, state = "readonly")
        norm_phone = self.phone_entry.configure(state='normal')
        self.assertEqual(norm_phone, state = "normal")
        self.assertNotEqual(norm_phone, state = "readonly")
        norm_email = self.email_entry.configure(state='normal')
        self.assertEqual(norm_email, state = "normal")
        self.assertNotEqual(norm_email, state = "readonly")
        norm_altemail = self.altemail_entry.configure(state='normal')
        self.assertEqual(norm_altemail, state = "normal")
        self.assertNotEqual(norm_altemail, state = "readonly")
        norm_pronouns = self.pronouns_entry.configure(state='normal')
        self.assertEqual(norm_pronouns, state = "normal")
        self.assertNotEqual(norm_pronouns, state = "readonly")
        norm_notes = self.notes_entry.configure(state='normal')
        self.assertEqual(norm_notes, state = "normal")
        self.assertNotEqual(norm_notes, state = "disabled")
        norm_group = self.group_entry.configure(state='normal')
        self.assertEqual(norm_group, state = "normal")
        self.assertNotEqual(norm_group, state = "disabled")

    def test__init__(self, root):
        pass

if __name__ == "__main__":
    unittest.main()
