#  while loop = a statement that will execute its block of code, as long as it's condition remains true

#while 1==1:
#    print("Help! I am eternally stuck in a loop!")

# ^^ infinite loop

name = ""

while len(name) == 0:
    name = input("Enter your name: ")


print("Hello, " + (name.capitalize()) + "!")