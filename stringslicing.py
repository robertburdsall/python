# slicing = create a substring by extracting elements from another string
# either indexing[] or slice()
# [start:stop:step]

name = "Robert Burdsall"

first_name = name[0:6]  # first num is inclusive, other is exclusive
# you could also do name[:6] (python assumes that you start at 0)

last_name = name[7:15]
# you could also do name[7:] (python would just do all remaining characters

funky_name = name[:15:3]
# you could also do name[::3]

reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

# Slice function starts here

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)
# negative index - character at the very end of a string has a negative index value of -1, and it increases from there.
print(website1[slice])
print(website2[slice])
