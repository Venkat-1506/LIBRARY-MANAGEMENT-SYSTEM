import library_manager

def main():
    library_manager.initialize_books()

    while True:
        print("\n===== Library Menu =====")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            library_manager.view_books()

        elif choice == '2':
            book = input("Enter book name: ")
            library_manager.borrow_book(book)

        elif choice == '3':
            book = input("Enter book name: ")
            library_manager.return_book(book)

        elif choice == '4':
            break

if __name__ == "__main__":
    main()