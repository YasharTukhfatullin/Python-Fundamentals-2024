"""
scope = The region that a variable is recognized 
        A variable is only available from inside the region it is created.
        A global and locally scoped versions of a variable can be created.

L = Local
E = Enclosing
G = Global
B = Built-in
"""
name = "Bro" # Global scope (available inside & outside function)

def display_name():
  name = "Code" # Local scope (available inside this function)
  print(name)

display_name()
print(name)