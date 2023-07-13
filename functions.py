#  function = a block of code that is executed only when it is called

# this process is called invoking

def hello(first_name, last_name, age):  # def is how you define a function - inside () is a variable that can have
    # information passed
    # into it
    print("Hello, " + first_name + " " + last_name)
    print("You are " + str(age) + " years old!")
    print("Have a nice day!")


x = "Robert"
y = "Burdsall"

# hello("Robert")  # information being sent to the function
hello(x, y, 16)
