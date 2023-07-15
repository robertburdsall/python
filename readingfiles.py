try:
    with open("test.tx") as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("Invalid file name/path!")
