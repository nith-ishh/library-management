# Simple Library Management System

library = []

def add_book(book_name):
    library.append(book_name)
    print(f"Book '{book_name}' added successfully.")

def view_books():
    if not library:
        print("Library is empty.")
    else:
        print("Books available in library:")
        for book in library:
            print("-", book)

def issue_book(book_name):
    if book_name in library:
        library.remove(book_name)
        print(f"Book '{book_name}' issued successfully.")
    else:
        print("Book not available.")

def return_book(book_name):
    library.append(book_name)
    print(f"Book '{book_name}' returned successfully.")

# Menu-driven program
while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        add_book(name)

    elif choice == "2":
        view_books()

    elif choice == "3":
        name = input("Enter book name to issue: ")
        issue_book(name)

    elif choice == "4":
        name = input("Enter book name to return: ")
        return_book(name)

    elif choice == "5":
        print("Exiting Library System.")
        break

    else:
        print("Invalid choice. Try again.")

