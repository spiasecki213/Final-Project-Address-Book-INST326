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

# Bibliography
*We used these sources to get a better understanding of some aspects of Tkinter and Python, and to help resolve any issues that came up.*


Amos, D. (2022, March 30). Python GUI programming with Tkinter. Real Python. Retrieved May 4, 2022, from https://realpython.com/python-gui-tkinter/ 
  This source was extremely useful as a starting point for our project. We were not too familiar with Tkinter at the start of the project. It provided examples on how 
  to build a GUI and use the widgets to customize our project. 
  
Colors. wikiPython. (2022, March 22). Retrieved May 1, 2022, from https://www.wikipython.com/tkinter-ttk-tix/summary-information/colors/ 

Create UI using tkinter in Python. Create UI using Tkinter in Python. (n.d.). Retrieved May 1, 2022, from https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python

Fitzpatrick, M. (2021, November 17). QComboBox - Drop-down selection widget. Python GUIs. Retrieved May 3, 2022, from https://www.pythonguis.com/docs/qcombobox/ 
  This source was particulalry useful reagarding how to make drop down menus using the QComboBox widget. The nature of our projct requires us to use them regularly. 
  Having a source that focuses on this widget was extremely helpful as it provided us with different ways and methods we could utalize for our program, as opposed to 
  the introductory basics.
  
Jarana, N. (2021, June 10). How to get selected value from Listbox in Tkinter? GeeksforGeeks. Retrieved May 6, 2022, from https://www.geeksforgeeks.org/how-to-get-selected-value-from-listbox-in-tkinter/ 
  This was another specified website that helped explain what Listbox was in Tkniter and how we could retreieve the selected value our prospective users would make. 
  It provided us with example code and an explanantion that detailed the purpose behind it. This was a nice model we used throughout our code. 

Kumar, B., &amp; KumarEntrepreneur, B. (2022, February 7). Python Tkinter messagebox + 19 Examples. Python Guides. Retrieved May 5, 2022, from https://pythonguides.com/python-tkinter-messagebox/ 

Rathod, A. K. (2020, December 11). How to hide, recover and delete tkinter widgets? GeeksforGeeks. Retrieved May 5, 2022, from https://www.geeksforgeeks.org/how-to-hide-recover-and-delete-tkinter-widgets/ 

Rora, R. (2021, September 23). PyQt5 – Hide push button on click. GeeksforGeeks. Retrieved May 6, 2022, from https://www.geeksforgeeks.org/pyqt5-hide-push-button-on-click/ 
