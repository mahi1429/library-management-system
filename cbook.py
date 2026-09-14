class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        #when the book is created, it is available by default
        self.available = "available"

    def to_dict(self):
        #this method converts the Book object to a dictionary representation.
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre,
            "available": self.available
        }