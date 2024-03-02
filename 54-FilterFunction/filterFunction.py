"""
filter() = creates a collection of elements from an iterable for which a function returns true

filter(function, iterable)
"""

# list of tuples
friends = [
    ("Ryan", 19),
    ("Bryson", 18),
    ("Jake", 17),
    ("Carson", 16),
    ("Andrew", 21),
    ("Dan", 20),
]

age = lambda data: data[1] >= 18

drinking_friends = list(filter(age, friends))
for i in drinking_friends:
    print(i)
