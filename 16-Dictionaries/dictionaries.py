"""
dictionary = a changeable, unordered collection of unique key:value pairs
            Fast because they use hashing, allow us to access a value quickly.
"""

capitals = {
    "USA": "Washington DC",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
}

print(capitals)
print(capitals.get("Russia"))
print(capitals.get("Germany"))  # use get method
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)

capitals.update({"Germany": "Berlin"})
print(capitals)

capitals.pop("China")
print(capitals)
