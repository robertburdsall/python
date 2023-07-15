# scope = the region that a variable is recognized
# a variable is only available from inside the region that it is created
# a global and locally scoped versions of a variable can be created

name = "Bro"  # global scope (available inside & outside of functions)


def display_name():
    name = "Code"  # because this variable is created inside the function, it is a local variable with a local
    # scope (only available inside this function)
    print(name)


print(name)  # since this is outside the function, it'll print bro

# if you have a local and global variable, the function will use the local first and then move to global
# practically local > global
