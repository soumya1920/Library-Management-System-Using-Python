library = []

def add_book():
    book = input("Enter the Book Name: ")
    library.append(book)
    print("Book added successfully\n")

def display_books():
    if len(library) == 0:
        print("Library is empty\n")
    else:
        print("Library ki books:")
        for book in library:
            print(book)
        print()

def issue_book():
    book = input("Enter the Book Name to issue: ")
    if book in library:
        library.remove(book)
        print("Book issued successfully\n")
    else:
        print("Book is not available\n")

def return_book():
    book = input("Enter the Book Name to return: ")
    library.append(book)
    print("Book returned successfully\n")

while True:
    print(" Library Management System ")
    print("1. Book Add")
    print("2. Book Display")
    print("3. Book Issue")
    print("4. Book Return")
    print("5. Exit")

    choice = input("Eneter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Program exited successfully\n")
        break
    else:
        print("Invalid choice. Please try again.\n")