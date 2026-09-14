import cbook
import logging
logger = logging.getLogger(__name__)

def add_book(library):
    #get the book details from the user
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of publication: ")
    while not year.isdigit() or len(year) != 4:
        print("Invalid year input. Please enter a 4-digit year.")
        year = input("Enter the year of publication: ")
    genre = input("Enter the genre of the book: ")

    #transform the user input into a Book object
    new_book = cbook.Book(title, author, year, genre)

    #check if the book already exists in the library. A book is considered to exist if both the title and author match an existing book in the library.
    for book in library.values():
        if book.title.lower() == new_book.title.lower() and book.author.lower() == new_book.author.lower():
            logger.warning(f"Attempted to add a book that already exists: {new_book.title} by {new_book.author}")
            print("Book already exists.")
            return
        
    #if the library is empty, the book id will be 1. If the library is not empty, the book id will be one more than the previous book id in the library.
    if not library:
        book_id = 1
    else:
        book_id = max(library.keys()) + 1

    #with the assigned book id, the new book object is added to the library
    library[book_id] = new_book
    logger.info(f"Book added successfully: {new_book.title} by {new_book.author}")
    print("Book added successfully!")

def view_books(library):
    #if library is empty, print a message and exit the function
    if not library:
        print("The library is empty.")
        return
    
    #Print the book_id and its details of each book in the library
    for book_id, book in library.items():
        print(f"Book ID: {book_id}")
        print(f"Book Details: {book.title}, {book.author}, {book.genre}, {book.year}, {book.available}")

def search_book(library):
    if not library:
        print("The library is empty.")
        return

    while True:
        #ask the user to choose the search criteria
        print("1. Search for book by title.")
        print("2. Search for book by author.")
        print("3. Search for book by genre.")
        print("4. Exit")


        ans = input("Enter your choice (1-4): ")
        found = False
        
        if ans == "1":
            title = input("Title: ")

            for book in library.values():
                if book.title.lower() == title.lower():
                    #change found status to true and print the book details of all books with this title
                    found = True
                    print(f"Book: {book.title}, {book.author}, {book.genre}, {book.year}")
            if not found:
                print("No books found with this title.")
            break

        elif ans == "2":
            author = input("Author: ")

            for book in library.values():
                if book.author.lower() == author.lower():
                    found = True
                    print(f"Book: {book.title}, {book.author}, {book.genre}, {book.year}")
            if not found:
                print("No books found by this author.")
            break

        elif ans == "3":
            genre = input("Genre: ")

            for book in library.values():
                if book.genre.lower() == genre.lower():
                    found = True
                    print(f"Book: {book.title}, {book.author}, {book.genre}, {book.year}")
            if not found:
                print("No books found in this genre.")
            break

        elif ans == "4":
            print("Exiting search.")
            logger.info("Exiting search.")
            break
        else:
            print("Invalid choice.Please choose from the given choices (1-4).")


def find_book(library): 
#This functionis specifically designed for other fuctions.
    if not library:
        print("The library is empty.")
        return
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    for book_id, book in library.items():
        if book.title.lower() == title.lower() and book.author.lower() == author.lower():
            return book_id, book

def borrow_book(library):

    result = find_book(library)
    if result is None:
        print("Book not found.")
        return
    book_id, book = result
    if book.available == "borrowed":
        print("Book is currently unavailable.")
        print("would you like to see suggestions from the same author or genre? (yes/no)")
        ans = input().lower()
        if ans == "yes":
            print("1. Suggestions from the same author")
            print("2. Suggestions from the same genre")
            choice = input("Enter your choice (1-2): ")
            if choice == "1":
                for b in library.values():
                    if b.author.lower() == book.author.lower() and b.title.lower() != book.title.lower():
                        print(f"Suggestion: {b.title}, {b.author}, {b.genre}, {b.year}")
            elif choice == "2":
                for b in library.values():
                    if b.genre.lower() == book.genre.lower() and b.title.lower() != book.title.lower():
                        print(f"Suggestion: {b.title}, {b.author}, {b.genre}, {b.year}")
            else:
                print("Invalid choice.")
        elif ans == "no":
            print("exiting suggestions.")
            logger.info("Exiting suggestions.")
        return
    
    book.available = "borrowed"
    logger.info(f"Book borrowed: {book.title} by {book.author}")
    print("Book borrowed successfully!")

def return_book(library):
    result = find_book(library)
    if result is None:
        print("Book not found.")
        return
    book_id, book = result
    if book.available == "borrowed":
        book.available = "available"
        logger.info(f"Book returned: {book.title} by {book.author}")
        print("Book returned successfully!")
    else:
        print("Book is not currently borrowed.")

def update_book(library):
    result = find_book(library)
    if result is None:
        print("Book not found.")
        return
    
    book_id, book = result

    while True:
        print("What would you like to update? 1. Title 2. Author 3. Genre 4. Year 5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            logger.info(f"Updating title for book: {book.title} by {book.author}")
            new_title = input("Enter the new title: ")
            book.title = new_title
            logger.info(f"Title updated successfully to: {book.title}")
            print("Title updated successfully!")

        elif choice == "2":
            logger.info(f"Updating author for book: {book.title} by {book.author}")
            new_author = input("Enter the new author: ")
            book.author = new_author
            logger.info(f"Author updated successfully to: {book.author}")
            print("Author updated successfully!")

        elif choice == "3":
            logger.info(f"Updating genre for book: {book.title} by {book.author}")
            new_genre = input("Enter the new genre: ")
            book.genre = new_genre
            logger.info(f"Genre updated successfully to: {book.genre}")
            print("Genre updated successfully!")

        elif choice == "4":
            logger.info(f"Updating year for book: {book.title} by {book.author}")
            new_year = input("Enter the new year: ")
            book.year = new_year
            logger.info(f"Year updated successfully to: {book.year}")
            print("Year updated successfully!")
             
        elif choice == "5":
            break
        else:

            print("Invalid choice. Please try again.")

def delete_book(library):
    result = find_book(library)

    if result is None:
        print("Book not found.")
        return
    book_id, book = result

    logger.info(f"Deleting book: {book.title} by {book.author}")
    del library[book_id]
    logger.info(f"Book deleted successfully: {book.title} by {book.author}")

    print("Book deleted successfully!")

