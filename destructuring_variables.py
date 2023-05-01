name, age = "kofi", 23

student_attendance = {"Rolf": 96, "Bob": 80, "Anne":100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

print(student_attendance.items())
print(list(student_attendance.items()))

people = [("bob",42,"Mechanic"), ("James",24,"Artist"), ("Harry",32,"Lecturer")]

for name, age, profession in people:
    print(f"Name:{name}, Age:{age}")

head, *tail = [1,2,3,4,5,6,7,8,9,10]
print(head)
print(tail)