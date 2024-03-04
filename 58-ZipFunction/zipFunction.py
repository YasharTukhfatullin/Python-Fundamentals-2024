"""
zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc)
creates a zip objects with paired elements stored in tuples for each elements.
"""

usernames = ["Dude", "Bro", "Mister"]  # list
passwords = ("p@ssword", "abc123", "guest")  # tuples
login_date = ["1/1/2021", "1/2/2022", "1/3/2023"]

users_zip = zip(usernames, passwords)
for i in users_zip:
    print(i)

print(type(users_zip))
print("==============")

users_list = list(zip(usernames, passwords))
for i in users_list:
    print(i)
print(type(users_list))
print("==============")

users_dict = dict(zip(usernames, passwords))
for key, value in users_dict.items():
    print(key, value)
print(type(users_dict))
print("==============")

users = zip(usernames, passwords, login_date)
for i in users:
    print(i)  # tuple
