# Overview

As a software engineer, I want to always be expanding my skillset and up to date with technology. Databases are used everywhere in software, so for this program, I wanted to expirament with using a cloud database.

The program I wrote is a simple to-do list program. The user can add items to the to do list, check them off, and delete items. When an item is added to the to-do list, it is added to the cloud database. When the item is checked off, the database item is edited, and when the user deletes an item from their list, it is likewise deleted from the database. The database is used when the user closes the list and then restarts the program. Since all of the data is stored in the database, the list is repopulated with every item that was on the list when the user closed it.

To-do lists are handy for remembering tasks one needs to complete, and for keeping track of which tasks have been completed. 

[Software Demo Video](https://youtu.be/3_nNYYQg41Q)

# Cloud Database

The cloud database I'm using is google Firebase.

Google firebase is a simple NoSQL firebase. This means that it doesn't have columns, rows, or even any tables. Everything is stored in key value pairs, similar to a python dictionary, or a json object.

# Development Environment

The development environement I used is VS Code.

The language I used to program is python. I used the Tkinter library for the GUI.

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [How to Connect Your Python Application to Firebase Realtime Database](https://www.youtube.com/watch?v=BnrkTpgH5Vc)
- [GeeksforGeeks Forum](https://www.geeksforgeeks.org)
- [Google Firebase official site](https://console.firebase.google.com)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- Fix the load function so that list items that were previously checked off will be checked off when they are loaded from save. 
- Add a feature so that the user can create multiple lists
- More customization options (like the ability to change the background color).
