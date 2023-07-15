import os

path = "C:\\Users\\admin\\Desktop\\test.txt"
path2 = "C:\\Users\\admin\\Desktop\\test"

if os.path.exists(path2):
    print("This location exists!")
    if os.path.isfile(path2):
        print("That is a file!")
    elif os.path.isdir(path2):
        print("That is a directory!")
else:
    print("That location doesn't exist!")