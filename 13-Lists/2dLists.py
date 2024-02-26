"""
2d lists = a list of lists
"""

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["ice cream", "cake"]

food = drinks, dinner, dessert
print(food)

print(food[0][1])
print(food[2][0])
