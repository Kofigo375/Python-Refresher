class ClassTest:
    def instance_method(self):
        print(f"called an instance_method of {self}")
    @classmethod
    def class_method(cls):
        print(f"called class_method of {cls}")
    @staticmethod
    def static_method():
        print("called static_me.")


'''
test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)
ClassTest.class_method()
ClassTest.static_method()
'''

class Book:
    types = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}>"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, Book.types[0], page_weight + 100)
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.types[1], page_weight)


book = Book.hardcover("Merlin", 10000)
book_1= Book.paperback("Teen Wolf", 200)
#print(book.weight)

print(book)
print(book_1)






