def user_age_in_secs():
    user_age = int(input("Please Enter your age"))
    age_secs = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_secs}.")

#user_age_in_secs()

def add(a,b):
    pass

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend/divisor)
    else:
        print("you can't divide something by 0")
# calling fuction with keyword argument
divide(divisor=13, dividend=0)   