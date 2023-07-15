import os

source = "test.txt"
destination = "C:\\Users\\admin\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file here!")
        x = input("Type 'ok' if you are okay with overriding this file!")
        if x == "ok":
            os.replace(source, destination)
            print(source + " was moved!")
    else:
        os.replace(source, destination)
        print(source + " was moved!")
except FileNotFoundError as e:
    print(e)
    print(source + " was not found!")

# works with folders as well!