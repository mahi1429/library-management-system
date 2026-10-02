Library Management System

A CLI Python-based Library Management System that allows users to manage books, search the library, and handle borrowing and returning. The project uses Object-Oriented Programming, modular design, JSON persistence, and logging.

Features

* Add new books
* View all books
* Search books by:
    - Title
    - Author
    - Genre
* Borrow books
* Return books
* Update book information
* Delete books
* Prevent duplicate books
* Store library data in a JSON file
* Log important program events

Project Structure

library-management
-- cbook.py
-- functions.py
-- data_storage.py
-- main.py
-- data.json
-- README.md
-- .gitignore

File Descriptions

cbook.py
Contains the Book class, which represents individual books and their properties.

functions.py
Contains the main library operations such as adding, searching, borrowing, returning, updating, and deleting books.

data_storage.py
Handles loading library data from JSON and saving library data back to JSON.

main.py
Runs the program and handles the menu and user interaction.

data.json
Stores the library data so that books remain available after the program is closed.

The program will display a menu where you can choose the operation you want to perform.

Technologies Used:
* Python
* Object-Oriented Programming (OOP)
* JSON
* Python Logging
* Git & GitHub


What I Practiced:

This project helped me practice:
* Classes and objects
* Functions and modules
* Dictionaries
* Loops and conditionals
* Exception handling
* File handling
* JSON serialization and deserialization
* Logging
* CRUD operations
* Basic software project structure


Possible future improvements include:
* Adding automated tests
* Adding a graphical user interface
* Improving input validation
* Adding user accounts and authentication
* Adding database support