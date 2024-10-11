class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size) -> None:
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self) -> str:
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}"


class PrintBook(Book):
    def __init__(self, title, author, page_count) -> None:
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self) -> str:
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"



class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        if isinstance(book, (Book, PrintBook, EBook)):
            self.books.append(book)
        else:
            print(f"Error: Cannot add {type(book).__name__}. Only Book, PrintBook, or EBook objects are allowed.")

    def list_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            for book in self.books:
                print(book)
