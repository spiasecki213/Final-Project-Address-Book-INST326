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
        pass

    def test_read_only_fields(self):
        pass

    def test_normal_fields(self):
        pass

    def test__init__(self, root):
        pass

if __name__ == "__main__":
    unittest.main()
