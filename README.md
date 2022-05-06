## What our project does
For our final project of INST326, we created an address book application that is designed to run using Python. Our address book is specifically designed to be used by students and/or staff of the University of Maryland that wish to keep a record of student, TA, professor, or staff contacts. Users will be able to add, view, delete, and search through their contacts.

## How to run our program
We designed our program so that the only requirement to run the program from the command line is by simply navigating to the correct file path and entering whichever version of python you're running, followed by "FinalProject.py". Any other commands or method-calls are handled within the GUI of the program.

## How to use the program and interpret its output
We've created a user interface that is simple and easy enough for any person to understand. The various entry fields and buttons are specifically labeled so that their purpose is communicated by reading each attribute's title. For example, the "Add Contact" button adds the contact to both the database and the list of contacts. Also, we've added various message and error boxes that pop up and keep the user updated on their various actions throughout their usage of the program. For example, if the user tries to add a contact that doesn't include a first or last name, the following message pops up for the user:

<img src="https://user-images.githubusercontent.com/102698713/167064171-1090c2cb-d720-46e0-b138-7e3ac588fca4.png" alt="Name field error message" height=25% width=25%/>


### Note: Code needed to run our program
One of our import statement includes the code `from ttkwidgets.autocomplete import AutocompleteCombobox`. This widget can be installed with the following code in your command line:
>`pip install ttkwidgets`
