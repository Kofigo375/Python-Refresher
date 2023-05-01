class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"This is {self.name}, he is {self.age} years old"

    def __repr__(self):
        return f"<Person{self.name}, is {self.age} year old>"


bob = Person("bob", 40)
print(bob)