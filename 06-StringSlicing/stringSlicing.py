"""
slicing = create a substring by extracting elements from another string
          indexing[] or slice()
          [start:stop:step]
"""
# Index function
name = "Yashar Tukhfatullin"

first_name = name[0:3]
last_name = name[7]
funky_name = name[::3]
reverse_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reverse_name)
print("===========================")

# Slicing Function
website1 = "http://google.com"

sliceWeb = slice(7, -4)
print(website1[sliceWeb])
