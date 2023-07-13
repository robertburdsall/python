#  index operator [] = gives access to a sequence's element (str, list, tuples)

name = "Robert Burdsall!"

if name[0].islower():  # [x] gets a specific character inside a string
    name = name.capitalize()

first_name = name[:6].upper()
last_name = name[7:].lower()
last_character = name[-1]  # negative indexing - last character in a string is -, goes up from there


print(first_name)
print(last_name)
print(last_character)
# print(name)