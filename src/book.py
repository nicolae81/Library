class Book:
    def __init__(self, title, author, publication_date,  ISBN, publishing_house, number_pages):
       self.title = title
       self.author = author
       self.publication_date = publication_date
       self.ISBN = ISBN
       self.publishing_house = publishing_house
       self.number_pages = number_pages
       self.books_read = False
           
    def __str__(self):
       return f"{self.title} by {self.author}, published in {self.publication_date}, ISBN: {self.ISBN}, published by {self.publishing_house}, {self.number_pages} pages"
