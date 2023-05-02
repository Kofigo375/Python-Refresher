from typing import list

# do not use default parameter values that are mutable
class Student:
    def __init__(self, name:str, grades: list[int] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(sef, result):
        self.grades.append(result)

bob = Student("bob")
bob.take_exam(90)
