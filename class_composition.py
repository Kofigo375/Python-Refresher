class Bookshelf:
    def __init__(self, *books):
        self.books = books 

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."

class Book:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Book {self.name}"

book = Book("Atomic Habbits")
book_2 = Book("The miracle morning")
book_3 = Book("The power of unwavering focus")



shelf = Bookshelf(book, book_2, book_3)
print(shelf)

# composition means a class has many classes( eg. a bookshelf has many books)
# while inheritance is a class is another class(eg. a bookshelf is a book)