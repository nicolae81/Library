class Library:
       def __init__(self, name):
              self.name = name
              self.list_of_books = []
              
       def add_book(self, book):
              self.list_of_books.append(book)
              
       def delete_book(self, ISBN):
              for book in self.list_of_books:
                     if book.ISBN == ISBN:
                            self.list_of_books.remove(book)
                            print("Book deleted successfully.")
                            return
              print("Book with ISBN", ISBN, "not found.")
              
       def modify_book(self, ISBN, title):  #Modify the book title
              pass
              
       def modify_book_author(self, ISBN, author):
              pass 
       
       def modify_book_publication_date(self, ISBN, publication_date):
              pass
       
       def display_total_number_of_books_from_the_library(self): #only the number of books
              pass
       
       def display_number_of_books_from_the_library_by_ISBN(self, ISBN):
              pass
       
       def displaying_all_books_from_the_library(self):
              pass