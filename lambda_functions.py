add = lambda a, b: a + b
print(add(2,5))

# uses of lambda functions
def double(x):
    return x * 2

# list comprehension version
sequence = [1,2,3,4,5,6]
doubled = [double(x) for x in sequence]
simple_doubled = map(double, sequence)

# lambda version
doubled_lambda = [(lambda x: x*2)(x) for x in sequence]
doubled_map_lambda = list(map(lambda x: x*2, sequence))  # map fuction returns a map object so we cast it into a list and print it 
print(doubled, doubled_map_lambda)