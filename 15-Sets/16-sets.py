"""
sets = collection which is unordered, unindexed. No duplicate values.
"""

utensils = {"fork", "spoon", "knife", "knife", "knife"}

for x in utensils:
    print(x)

utensils.add("napkin")
print(utensils)

utensils.remove("knife")
print(utensils)
print("==================")

dishes = {"bowl", "plate", "cup", "knife"}

utensils.update(dishes)
print(utensils)

dinner_table = utensils.union(dishes)
print(dinner_table)

print(dishes.difference(utensils))
