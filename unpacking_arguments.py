def multiply(*args): # collects arguments and keep them in a tuple
    print(args)
    total = 1
    for arg in args:
        total = total*arg
    return total

#print(multiply(2,4,6,8,10))

nums = [2,4]
def add(x,y):
    return x+y

#print(add(*nums))
#dict_num = {"x": 12, "y": 44}
#print(add(**dict_num))

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"

print(apply(1,2,3,4,6, operator="*"))


