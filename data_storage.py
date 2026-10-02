import json
from cbook import Book
import logging

logger = logging.getLogger(__name__)

# loads the saved books from data.json and returns a dictionary of Book objects.
def load_lib():
    try:
        with open('data.json', 'r') as file:
            file_data = json.load(file)
            library = {}

            for book_id, book_data in file_data.items():
                book = Book(
                    book_data["title"],
                    book_data["author"],
                    book_data["year"],
                    book_data["genre"]
                )
                book.available = book_data["available"]
                
                library[int(book_id)] = book
            logger.info("Library data loaded successfully.")
            return library
        
    except FileNotFoundError:
        #if the data.json file does not exist, log a message and return an empty library
        logger.info("data.json file not found. Starting with an empty library.")
        return {}
    
    except json.JSONDecodeError:
        #if the data.json file contains invalid JSON, log an error message and raise the exception
        logger.error("Invalid JSON data in data.json")
        raise

# saves the library data to data.json file.
def save_lib(library):
    #create an empty dictionary to store the library data
    lib_data ={}

    #iterate through the items in the library dictionary and convert each Book object to a dictionary using the to_dict method
    for book_id, book in library.items():
        lib_data[book_id] = book.to_dict()
        
    #open file in write mode
    try:
        with open('data.json', 'w') as file:
            #converts the dictionary into a json string and writes it to the file
            json.dump(lib_data, file, indent=4)
            logger.info("Library data saved successfully.")
            
    except OSError:
        logger.error("Failed to save library data.")
        raise