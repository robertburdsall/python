# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

# print("The "+animal+" jumped over the "+item)
#print("The {} jumped over the {}".format(animal, item))
#print("The {1} jumped over the {0}".format(animal, item)) #  positional argument < - this is my favorite
#print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))   # keyword argument


text = "The {0} jumped over the {1}".format(animal, item)
print(text)


name = "Robert"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}".format(name))  # adds padding
print("Hello, my name is {:<10}".format(name))  # adds padding (left align)
print("Hello, my name is {:>10}".format(name))  # adds padding (right align)
print("Hello, my name is {:^10}".format(name))  # adds padding (center align)

number = 1000

print("The number pi is {:.2f}".format(number))  # displays the first 2 floating point numbers - 2i would be for ints
print("The number pi is {:,}".format(number))  # automatically adds commas at the 1000's places
print("The number pi is {:b}".format(number))  # shows the number in binary
print("The number pi is {:o}".format(number))  # shows the number in octal
print("The number pi is {:x}".format(number))  # shows the number in hexadecimal (uppercase for all uppercase)
print("The number pi is {:e}".format(number))  # shows the number in scientific notation (uppercase for all uppercase)




