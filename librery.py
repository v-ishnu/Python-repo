# Initialize library dictionary and genre dictionary
library = {}
genres = {}

# Main loop
while True:
    print("\nLibrary Management System")
    print("1. Add book")
    print("2. Check out book")
    print("3. Return book")
    print("4. Search by title")
    print("5. Search by author")
    print("6. Search by genre")
    print("7. Display all books")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # Add book
    if (choice == "1" or "a"):
        isbn = input("Enter ISBN: ")
        title = input("Enter title: ")
        author = input("Enter author: ")
        genre = input("Enter genre (optional): ")
        library[isbn] = (title, author, True)
        if genre:
            if isbn not in genres:
                genres[isbn] = []
            genres[isbn].append(genre)
        print(f"'{title}' by {author} has been added.")

    # Check out book
    elif choice == "2":
        isbn = input("Enter ISBN: ")
        if isbn in library:
            title, author, _ = library[isbn]
            library[isbn] = (title, author, False)
            print(f"'{title}' by {author} has been checked out.")
        else:
            print("Book not found.")
            
    
    # Return book
    elif choice == "3":
        isbn = input("Enter ISBN: ")
        if isbn in library:
            title, author, _ = library[isbn]
            library[isbn] = (title, author, True)
            print(f"'{title}' by {author} has been returned.")
        else:
            print("Book not found.")

    # Search by title
    elif choice == "4":
        title = input("Enter title: ")
        results = [(isbn, book[0], book[1], book[2]) for isbn, book in library.items() if title.lower() in book[0].lower()]
        for book in results:
            print(f"ISBN: {book[0]}, Title: {book[1]}, Author: {book[2]}, Available: {book[3]}")

    # Search by author
    elif choice == "5":
        author = input("Enter author: ")
        results = [(isbn, book[0], book[1], book[2]) for isbn, book in library.items() if author.lower() in book[1].lower()]
        for book in results:
            print(f"ISBN: {book[0]}, Title: {book[1]}, Author: {book[2]}, Available: {book[3]}")

    # Search by genre
    elif choice == "6":
        genre = input("Enter genre: ")
        results = [(isbn, library[isbn][0], library[isbn][1], library[isbn][2]) for isbn, genres_list in genres.items() if genre.lower() in [g.lower() for g in genres_list]]
        for book in results:
            print(f"ISBN: {book[0]}, Title: {book[1]}, Author: {book[2]}, Available: {book[3]}")

    # Display all books
    elif choice == "7":
        sorted_books = sorted(library.items(), key=lambda x: x[1][0])
        for isbn, book in sorted_books:
            print(f"ISBN: {isbn}, Title: {book[0]}, Author: {book[1]}, Available: {book[2]}")

    # Exit
    elif choice == "8":
        break

    else:
        print("Invalid choice. Please try again.")