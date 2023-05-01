list_1 = ['kofi', 'ama', 'yaw']
tup_1 = ("kofi", "ama" , "Yaa")
set_1 = {"kofi", "ama", "Yaa"}

print(list_1[2])
list_1.append("happy")
print(list_1)
list_1.remove("ama")
print(list_1)

## advanced set operations
friends = {"kofi", "ama", "Yaa", "Bob", "Anne"}
abroad = {"Bob", "Anne"}
local_friends = friends.difference(abroad)
print(local_friends)

## union
local = {"kofi", "ama", "Yaa"}
abroad = {"Bob", "Anne", "kofi", "ama"}
all_friends = local.union(abroad)
print(all_friends)

# list comprehensions
numbers = [1, 2, 3, 4]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print(doubled)

# list comprehensions
doubled_compre  = [num * 2 for num  in numbers]
print(doubled_compre)

## non-list comprehension
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)

## using list comprehension
start_with_s = [friend for friend in friends if friend.startswith("S")]
print(start_with_s)