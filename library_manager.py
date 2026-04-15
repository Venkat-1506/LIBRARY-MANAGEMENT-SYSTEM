import os

FILE_NAME = "books.txt"

def initialize_books():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            file.write("Python=Available\n")
            file.write("Java=Available\n")
            file.write("C++=Available\n")
            file.write("AI=Available\n")

def load_books():
    books = {}
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, status = line.strip().split("=")
            books[name] = status
    return books

def save_books(books):
    with open(FILE_NAME, "w") as file:
        for name, status in books.items():
            file.write(f"{name}={status}\n")

def view_books():
    books = load_books()
    for name, status in books.items():
        print(name, "-", status)

def borrow_book(book_name):
    books = load_books()
    if book_name in books and books[book_name] == "Available":
        books[book_name] = "Borrowed"
        save_books(books)
        print("Book borrowed!")
    else:
        print("Book not available")

def return_book(book_name):
    books = load_books()
    if book_name in books:
        books[book_name] = "Available"
        save_books(books)
        print("Book returned!")