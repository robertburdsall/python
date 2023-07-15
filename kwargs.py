# **kwargs = parameter that packs all args into a dictionary
# useful so that a function can accept a varying number of keyword arguments

def hello(**kwargs):
    print("Hello, ", end="")
    for key, value in kwargs.items():
        print(value, end=" ")


# print("Hello, " + kwargs["first"] + " " + kwargs["last"] + "!")

hello(title="Mr.", first="Robert", middle="Dude", last="Burdsall")
