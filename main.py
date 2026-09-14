from unittest import case

from functions import add_book, view_books, borrow_book, return_book, update_book, delete_book, search_book 
from data_storage import load_lib, save_lib
import logging

logging.basicConfig(filename = "library.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

library = load_lib()

def main():
    logging.info("Program started")
    print("Welcome to the Library Management System!")

    while True:
        print("\nPlease choose an option:")
        print("1. Add a book")
        print("2. View all books")
        print("3. Search for a book")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. Update a book")
        print("7. Delete a book")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        match choice:
            case "1":
                add_book(library)
                save_lib(library)
            case "2":
                view_books(library)
            case "3":
                search_book(library)
            case "4":
                borrow_book(library)
                save_lib(library)           
            case "5":
                return_book(library)
                save_lib(library)
            case "6":
                update_book(library)
                save_lib(library)
            case "7":
                delete_book(library)
                save_lib(library)
            case "8":
                logging.info("Program exited")
                print("Exiting the program...")
                break
            case _:
                logging.warning(f"Invalid choice: {choice}")
                print("Invalid choice. Please choose from the given choices (1-8).")

main()
