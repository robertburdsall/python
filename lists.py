#  list = something used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

food[0] = "sushi"

food.append("ice cream")  # adds an element to the end of a list
food.remove("hotdog")  # removes a specific specified element
food.pop()  # removes the last element
food.insert(0, "cake")  # adds an element at a specific position
food.sort()  # sorts a list alphabetically
food.clear()  # removes all the elements in a list

for x in food:
    print(x, end=" ")
