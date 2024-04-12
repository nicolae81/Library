from src.book import Book
from src.library import Library
import json
def display_menu():
    print("Welcome to the Library Management System!")
    print("Menu:")
    print("1. Add Book")
    print("2. Delete Book")
    print("3. Display All Books")
    # print("4. Modify only the Book title")
    # print("5. Sort Books from the Library by ISBN")
    print("4. Exit")


def add_book(library):
    print("Add Book:")
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    publication_date = input("Enter the publication date: ")
    ISBN = input("Enter the ISBN: ")
    publishing_house = input("Enter the publishing house: ")
    number_pages = input("Enter the number of pages: ")
    book = Book(title, author, publication_date, ISBN, publishing_house, number_pages)
    library.add_book(book)
    print("Book added successfully!")
    
    
def delete_book(library):
    print("Delete Book:")
    ISBN = input("Enter the ISBN of the book to delete: ")
    library.delete_book(ISBN)
    
    
def display_all_books(library):
    print("All Books in the Library:")
    for book in library.list_of_books:
        print(book)


# Function to save books to a JSON file
def save_books(library):
    with open("library_books.json", "w") as file:
        json.dump([book.__dict__ for book in library.list_of_books], file)

# Function to load books from a JSON file
def load_books(library):
    try:
        with open("library_books.json", "r") as file:
            books_data = json.load(file)
            library.list_of_books = [Book(**book_data) for book_data in books_data]
            print("Books loaded successfully!")
    except FileNotFoundError:
        print("No library books data found. Starting with an empty library.")

# Usage
if __name__ == "__main__":
    library = Library("My Library")
    
    # Load books from JSON file if available
    load_books(library)
    
    # Your existing code for menu and actions
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            delete_book(library)
        elif choice == "3":
            display_all_books(library)
        elif choice == "4":
            save_books(library)  # Save books before exiting
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")