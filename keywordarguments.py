# keyword arguments - arguments that are preceded by an identifier when we pass them to a function
# the order doesn't matter here

# example of positional args (order matters)

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)


# hello("Code","Dude","Bro") < - example of positional
hello(last="Code", middle="Dude", first="Bro")  # < - example of keywords - you just identify which value is which
