"""
Lists = used to store multiple items in a single variable.
"""

food = ["pizza", "hamburgers", "hotdog", "spaghetti"]
print(food)
print(food[0])
print(food[2])

food[0] = "Sushi"
print(food)

for i in food:
  print(i)
print("==================")

food.append("ice cream") # adds value at the end
print(food)

food.remove("hotdog") # removes value 
print(food)

food.pop() # removes last value in the list 
print(food)

food.insert(0, "Cake")
print(food)

food.sort()
print(food)