def divide (dividend, divisor):
    if divisor == 0:
       raise ZeroDivisionError("Divisor cannot be 0")
    return dividend/divisor

grades = [78, 99, 85, 100]
grade = []
print("Welcome to the average grade program")
try:
    average = divide(sum(grade), len(grade))
except ZeroDivisionError as e:
    print("there are no grades yet in your list")
else:
     print(f"The average grade is {average}")
finally:
    print("Thank you for using my program")

#divide(15, 0)