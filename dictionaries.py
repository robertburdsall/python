#  dictionary = a changeable, unordered collection of unique key:value pairs.
#  very fast because it uses hashing, allowing us to access a value quickly

capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

capitals.update({"Germany": "Berlin"})  # adds a new key:value pair
capitals.update({"USA": "Charlotte"})  # you can use that same method to update already existing key:value pairs
capitals.pop("China")  # removes a specific key:value pair from the dictionary
capitals.clear()  # clears an entire dictionary

# print(capitals["Germany"])  # gives an error because germany is not present in dictionary
# print(capitals.get("Germany"))  # gives no error - a much safer way to see if something is present

capitals.keys()  # gets all the keys in a dictionary
capitals.values()  # gets all the values in a dictionary
capitals.items()  # gets all the keys and values in a dictionary (prints the whole dictionary)

for key, value in capitals.items():
    print(key, value)
