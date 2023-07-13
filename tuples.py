#  tuple = a collection of elements which is unordered and unchangeable
#  used to group together related data

student = ("Bro", 21, "male")

student.count("Bro")  # prints the amount of times something is present in a tuple
student.index("male")  # prints the index in which an element is present at

for x in student:
    print(x, end=" ")

if "Bro" in student:
    print("Bro is here!")