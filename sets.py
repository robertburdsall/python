# Set = collection that is unordered, and unindexed. No duplicate values are allowed

utensils = {"fork", "spoon", "knife"}

dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")  # adds something to the set
utensils.remove("spoon")  # removes an element from the set
utensils.clear()  # clears an entire set
utensils.update(dishes)  # adds all the elements in one set to another
dinner_table = utensils.union(dishes)  # combines 2 sets
utensils.difference(dishes)  # prints what one list has that the other doesn't
utensils.intersection(dishes)  # prints what 2 lists have in common

for x in utensils:
    print(x)
