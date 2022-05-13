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
        pass

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
